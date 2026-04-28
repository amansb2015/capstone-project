from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, field_validator


from pydantic import BaseModel, Field, EmailStr, validator
class UserCreate(BaseModel):
    username: str
    password: str


@field_validator('password')
def validate_password(cls, value):
    if len(value) < 8:
        raise ValueError('Password must be at least 8 characters long')
    if not any(char.isdigit() for char in value):
        raise ValueError('Password must contain at least one digit')
    if not any(char.isupper() for char in value):
        raise ValueError('Password must contain at least one uppercase letter')
    return value


app = FastAPI()


@app.post("/users")
async def create_user_controller(user: UserCreate):
    return {"name": user.username, "message": "Account successfully created"}