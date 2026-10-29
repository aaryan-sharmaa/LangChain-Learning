from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import List, Dict, Optional


class Patient(BaseModel):

    name: str
    email: EmailStr
    firm_url: AnyUrl
    age: int
    weight: float
    diabetic: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @model_validator(mode="after")
    def validate_patient(self):
        if self.age < 18 and "guardian" not in self.contact_details:
            raise ValueError("Guardian contact is required for patients under 18")
        return self


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
print(patient1)