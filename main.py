# First, we need to import the necessary libraries
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

# 1. Create the App instance
app = FastAPI()

# 2. Define the Pydantic Model (Validation)
class Utilisateur(BaseModel):
    id: int
    email: EmailStr
    is_pro: bool = False

# 3. Define the Endpoint (The Route)
@app.post("/user")
async def creer(u: Utilisateur):
    # We replaced the "..." with actual logic to return the data
    return {
        "message": "User successfully created",
        "received_data": u
    }

# Note: In a real environment, you run this using: uvicorn main:app --reload
