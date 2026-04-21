from pydantic import BaseModel, EmailStr, Field
from typing import Optional


## Pydantic use cases:
## Normal declaration - Normal forced data type declaration, returns error if diff data type
## Predefined values - We can provide a defeault value in the key, which if not provided is printed in the output
## Optional - Imported from typing, We can provide an optional field which return None
## Forced conversation - If any string value is provided in int (or similar cases), it automatically converts it to the required data type
## EmailStr - Automatically validates the string provided should be in a valid email format.
## Field - Restrict the value as per provided conditions. 'default' parameter is also present.
## Field(description) parameter - It acts same as Annotation in TypedDict, which gives a small decription to LLM. Regex can also be defined to get output in a particular format

class Student(BaseModel):
    name: str # Normal declaration
    subject: str = 'Maths' # Predefined overwriteable value
    age: Optional[int] = None # "Optional" value, returns None if not assigned
    email: EmailStr # EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5) # Field validation, range provided here is 0 to 10


new_student = {
    'name': 'Nihit',
    'email': 'nihit@nihit.com',
    'cgpa': '1'
}
#new_student = {'name':32} # This will create error since name is str

# Creating obj of Student class
student = Student(**new_student)

print(student)

# Output can also be coverted into dict or json format
student_dict = student.model_dump()
student_json = student.model_dump_json()

print("DICT", student_dict)
print("JSON", student_json)