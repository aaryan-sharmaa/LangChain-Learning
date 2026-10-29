from importlib import metadata
from operator import gt

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    
    #metadata
    name: Annotated[
    str,
    Field(
        min_length=2,
        max_length=50,
        description="Patient's full name",
        examples=["Aarav Sharma"]
    )] 
    email: EmailStr
    firm_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[
    float, 
    Field(
        gt=0, 
        strict=True
    )]
    diabetic: bool = False
    allergies: Optional[List[str]] = Field(max_length=5)
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print("Patient Details:")
    print(f"Name: {patient.name}")
    print(f"Email: {patient.email}")
    print(f"Firm URL: {patient.firm_url}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight}")
    print(f"Diabetic: {patient.diabetic}")
    print(f"Allergies: {patient.allergies}")
    print(f"Contact Details: {patient.contact_details}")

    print("\nPatient inserted into database")
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')
        

patient_info = {
    "name": "Aarav Sharma",
    "email": "aarav.sharma@gmail.com",
    "firm_url": "https://www.example.com",
    "age": 24,
    "weight": 68.5,
    "diabetic": False,
    "allergies": ["Peanuts", "Dust"],
    "contact_details": {
        "phone": "9000000000",
        "city": "Delhi",
        "country": "India"
    }
}
    
patient1 = Patient(**patient_info)

insert_patient_data(patient1)