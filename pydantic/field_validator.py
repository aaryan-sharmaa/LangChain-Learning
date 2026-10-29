from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import Annotated, List, Dict, Optional


class Patient(BaseModel):

    name: Annotated[str, Field(min_length=2, max_length=50)]
    email: EmailStr
    firm_url: AnyUrl
    age: int
    weight: float
    diabetic: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @field_validator("email", mode='after') #default mode
    @classmethod
    def validate_bank_email(cls, value):
        allowed_domains = ["hdfcbank.com", "icicibank.com"]
        domain = value.split("@")[-1].lower()

        if domain not in allowed_domains:
            raise ValueError("Email must belong to HDFC Bank or ICICI Bank")

        return value
    
    @field_validator("age", mode='before')
    @classmethod
    def validate_age(cls, value):
        if value <= 0:
            raise ValueError("Age must be positive")
        return value


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