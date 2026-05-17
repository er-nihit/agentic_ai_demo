from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()

##-------------- PYDANTIC DATA VALIDATION ----------------

## 3.1. Creating a Pydantic model for POST requests
# ~~> 3.2
class Patient(BaseModel):
    id: Annotated[str, Field(..., description='ID of the patient', examples=["P001"])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City of patient')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female','others'], Field(...,description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in meters')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in KGs')]

    # Using computer_field to calculate bmi
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight/(self.height**2),2)
    
    # Using computed field to categorize verdict
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5: 
            return "Underweight"
        elif self.bmi > 35:
            return "Obese"
        else:
            return "Normal"
        

## 4.1. Pydantic model for PUT Methods
# We are not updating the patient_id because it is being as input and is considered as an immutable unique key.
# All other variables are optional with None as default since we don't know what values will be provided by the user.
# ~~> 4.2
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0, lt=120)]
    gender: Annotated[Optional[Literal['male', 'female','others']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]

##----------------- UTILITY FUNCTIONS -------------------

## 2a. Python function to load data from json file
# ~~> 2b
def load_data():
    with open ('patients.json', 'r') as f:
        data = json.load(f)
    return data

## 3.3b. Utility function to save the json after data updation
# ~~> 3.3c
def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)


##---------------------- ENDPOINTS ----------------------

## 1. Endpoint - Home Page
# ~~> 1.1
@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

## 1.1. Endpoint - Open about section
@app.get("/about")
def about():
    return {'message': 'Fully  functional API to manage patient records'}

## 2b. Endpoint - View all patient data
# ~~> 2.1
@app.get("/view")
def view():
    data = load_data()
    return data

## 2.1. Endpoint - View a particular patient
# ~~> 2.1.2
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., descrition="ID of the patient", examples="P001")):
    # Load all patients
    data = load_data()

    # Checking if the patient_id exists, then return that particular patient else return "patient not found"
    if patient_id in data:
        return data[patient_id]
    
    ## 2.1.2. This ensures to raise a 404 error if the patient data is not available.
    raise HTTPException(status_code=404, detail='Patient Not Found')

## 2.2. Query Parameter
# - ... means it is a mandatory field, it not provided, means treated as optional.
# - primary string means a default value for the query
# - Works same as a Path or Field(pydantic) parameter.
@app.get("/sort")
def sort_patient(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='Sort in ascending or descending order')):
    valid_fields = ['height', 'weight', 'bmi']
    
    # Verify if the sort_by value provided is valid, If not raise HTTPException
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field, Select from {valid_fields}')
    
    # Verify the order is either asc or desc, else raise HTTPException
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail='Invalid order, select either "asc" or "desc"')
    
    data = load_data()
    
    sort_order = True if order=='desc' else False

    # Sorting data according to query reques by the user
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data

## 3.2. Endpoint - Create new entry (POST)
# Here we are already defining the function aargument that the input should be a Pydantic model of class Patient
# ~~> 3.3
@app.post("/create")
def create_patient(patient: Patient):
    # Load exisiting data
    data = load_data()

    ## 3.3a. Check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')

    # Add new patient in DB
    # Use model_dump to add new patient as python dict
    # ~~> 3.3b
    data[patient.id] = patient.model_dump(exclude=['id'])

    ## 3.3c. Save as json
    # ~~> 3.4
    save_data(data)

    # 3.4. Show success HTTP message
    return JSONResponse(status_code=201, content={'message': 'Patient added successfully'})

## 4.2. Endpoint - Update existing values (PUT)
# ~~> 4.3
@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):
    # Load all data
    data = load_data()

    # 4.3. Check if patient is present or not
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    # Fetch data using patient id
    exisiting_data = data[patient_id]

    # Convert New data into python dict
    # exclude_unset=True: Excluding the None values so only the values provided by user is updated.
    new_data = patient_update.model_dump(exclude_unset=True)

    # Updating the current value with new value
    for key, value in new_data.items():
        exisiting_data[key] = value

    # 4.4. Calculate data for computed_field variables
    # If patient updates weight or height, we need to update the BMI as well
    # Add patient_id in the obj, so it can resemble original Patient class
    # Creating a new Patient pydantic object will automatically calculate the bmi and verdict again
    exisiting_data['id'] = patient_id
    updated_data = Patient(**exisiting_data)

    # Convert it into a python dict excluding the id, since it will be used as a unique key to update the data.
    temp = updated_data.model_dump(exclude=['id'])
    data[patient_id] = temp

    # Saving the new data in db
    save_data(data)

    # 4.5. Return Positive response
    return JSONResponse(status_code=200, content={'message':'Patient updated successfully'})

# 5.1. Endpoint - Remove patient detaails from the db
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    # Load Data
    data = load_data()

    # 5.2. Check if patient exists
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    # 5.3. Remove if exists
    del data[patient_id]

    # Save JSON
    save_data(data)

    # 5.4 Send success message
    return JSONResponse(status_code=200, content='Patient deleted')