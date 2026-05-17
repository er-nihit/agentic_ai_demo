from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

# 1. Endpoint - Home Page
@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

# 1.1. Endpoint - Open about section
@app.get("/about")
def about():
    return {'message': 'Fully  functional API to manage patient records'}

# 2.1. Python function to load data from json file
def load_data():
    with open ('patients.json', 'r') as f:
        data = json.load(f)
    return data

# 2.2. Endpoint - View all patient data
@app.get("/view")
def view():
    data = load_data()
    return data

# 3. Endpoint - View a particular patient
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., descrition="ID of the patient", examples="P001")):
    # Load all patients
    data = load_data()

    # Checking if the patient_id exists, then return that particular patient else return "patient not found"
    if patient_id in data:
        return data[patient_id]
    
    # 3.1. This ensures to raise a 404 error if the patient data is not available.
    raise HTTPException(status_code=404, detail='Patient Not Found')

# 4. Query Parameter
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

