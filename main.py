from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel

app = FastAPI()

# Modèle pour la requête POST /welcome
class WelcomeRequest(BaseModel):
    name: str

# Endpoint GET /hello
@app.get("/hello", response_class=PlainTextResponse)
async def hello():
    return "Hello, World!"

# Endpoint POST /welcome
@app.post("/welcome")
async def welcome(request: WelcomeRequest):
    return {"message": f"Welcome, {request.name}!"}