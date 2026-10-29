# computed_fields.py

from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List, Dict, Optional


class Patient(BaseModel):

    name: str
    email: EmailStr
    firm_url: AnyUrl
    age: int
    height: float  # in meters
    weight: float  # in kilograms
    diabetic: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)


patient_info = {
    "name": "Aarav Sharma",
    "email": "aarav.sharma@gmail.com",
    "firm_url": "https://www.example.com",
    "age": 24,
    "height": 1.75,
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
print(patient1.model_dump())