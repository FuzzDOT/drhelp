from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os

# Setup FastAPI app
app = FastAPI()

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

# Define your API routes
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Custom 404 error
@app.exception_handler(404)
async def not_found(request, exc):
    return {"error": "404 - Not Found"}