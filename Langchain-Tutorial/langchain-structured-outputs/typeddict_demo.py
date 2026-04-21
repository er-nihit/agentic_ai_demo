from typing import TypedDict

#This is just an example how typeddict works

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {
    'name':'Nihit',
    'Age':30
}

print(new_person)