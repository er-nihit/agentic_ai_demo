from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator, computed_field
from typing import List, Dict, Optional


## 4a NESTED MODELS
# Using Address model as a field model for next patient class.
class Address(BaseModel):
    city: str
    state: str
    pincode: str

## Defining Patient class for type validation (Ensure data is provided in correct format)
class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float # kg
    height: float # mtr
    married: bool
    allergies: List[str]
    address: Address
    contact_details: Dict[str, str]

    # 1. @field_validator()
    # It is used to add additional validations depending on the use case.
    # Example: We can check if the user is a employee of icici or hdfc by validating the email domain.
    # @field_validator is provided with the variable where validation is performed
    # @classmethod is important whenever the function is created for class.
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        # Defining valid domains in a list
        valid_domains = ['hdfc.com', 'icici.com']

        # Extrating domain name using split
        domain_name = value.split('@')[-1]

        # Validating domain name
        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        return value
    
    # It can also be used to make changes in the exisiting data.
    # For example, name should always be a upper case.
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    ## 2. model_validator()
    # It is used when we need to perform multiple validations for the whole class.
    # Example: If age is more than 60, there should be an emergency contact
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model
    
    ## 3. computed_field()
    # It is use to get the value of a variable, which is not required by the user as input.
    # It automatically calculates the value and stores in the model
    # NOTE: @computed_field and @property decorators are mandatory
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.bmi)
    print(patient.address.pincode)
    print("Updated")

# 4b. Nested models
# Creating an address model
address = {
    'state': 'Karnataka',
    'city': 'Bangalore',
    'pincode': '560066'
}

address1 = Address(**address)

patient_info = {
    "name": "Nihit Kumar",
    "email": "nihit@icici.com",
    "age": 62,
    "weight": 75.5,
    "height": 1.62,
    "married": False,
    "address": address1,
    "allergies": ['dust'],
    "contact_details": {
        "email": "nihit@gmail.com",
        "phone": "12321232",
        "emergency": "121212"
    }
}

patient1 = Patient(**patient_info)

update_patient_data(patient1)

## 5. Serialization
# Creating a dump of the data in python dict form.
# paramters:
#   - include=[] : Provide list of variables which is required in dump
#   - exclude=[] : Provide list of variables which needs to be excluded from dump
#   - exclude_unset=bool : (Default False) True will not export the (optional) variables which were not provided by the user 
dict_out = patient1.model_dump()
print(dict_out)
print(type(dict_out))

# Creating a dump of file in json format
# It will return a str which follow json formatting.
json_out = patient1.model_dump_json()
print(json_out)
print(type(json_out))