# main.py
from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.security.api_key import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from io import BytesIO
from models.input.voice.vToText.vToText import VToText
from models.input.text.preProcessing.preProcess import TextPreprocess
from models.input.image.preProcessing.preProcess import PreProcessing

# Load API key and access token
def load_config(file_path):
    with open(file_path, 'r') as config_file:
        config_data = json.load(config_file)
    return config_data
config = load_config(r'src\config.json')

# Define your API key and access token
API_KEY_NAME = config['API_KEY_NAME']
ACCESS_TOKEN_NAME = config['ACCESS_TOKEN_NAME']
API_KEY = config['API_KEY']
ACCESS_TOKEN = config['ACCESS_TOKEN']

# Define a function to get the API key
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
access_token_header = APIKeyHeader(name=ACCESS_TOKEN_NAME, auto_error=False)

# Check if API and access token are valid
async def get_api_key(
    api_key: str = Depends(api_key_header),
    access_token: str = Depends(access_token_header)
):
    if api_key != API_KEY or access_token != ACCESS_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid API key or access token")
    return api_key

# Setup FastAPI app
app = FastAPI()

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]

# Add CORS middleware
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

# Define a route to upload files
@app.post("/upload/")
async def upload_files(
    api_key_valid: bool = Depends(get_api_key),
    voice: UploadFile = File(None),
    text: UploadFile = File(None),
    image: UploadFile = File(None)
):
    results = {}
    if api_key_valid:
        for file_type, file in [("voice", voice), ("text", text), ("image", image)]:
            if file:
                content = await file.read()
                results[file_type] = {
                    "filename": file.filename,
                    "content_type": file.content_type,
                    "size": len(content)
                }
        return {"success": "Files uploaded successfully", "details": results}
    else:
        return {"error": "Could not validate credentials"}

# Define a route to process uploaded files
@app.post("/process/")
async def process_files(
    api_key_valid: bool = Depends(get_api_key),
    voice_file: UploadFile = File(None),
    text_file: UploadFile = File(None),
    image_file: UploadFile = File(None)
):
    results = {}
    if api_key_valid:
        if voice_file:
            # Process voice file
            voice_processor = VToText()
            voice_content = await voice_file.read()
            voice_bytes = BytesIO(voice_content)
            transcription = voice_processor.voice_to_text(voice_bytes)
            results["voice"] = transcription
        
        if text_file:
            # Process text file
            text_processor = TextPreprocess()
            text_content = await text_file.read()
            text_str = text_content.decode('utf-8')
            cleaned_text = text_processor.clean_text(text_str)
            tokens = text_processor.tokenize_text(cleaned_text)
            keywords, entities = text_processor.extract_features(cleaned_text)
            results["text"] = {
                "cleaned_text": cleaned_text,
                "tokens": tokens,
                "keywords": keywords,
                "entities": entities
            }
        
        if image_file:
            # Process image file
            image_processor = PreProcessing()
            image_content = await image_file.read()
            image_bytes = BytesIO(image_content)
            features = image_processor.extract_features(image_bytes)
            results["image"] = features.tolist()  # Convert tensor to list for JSON serialization
        
        return {"success": "Files processed successfully", "results": results}
    else:
        return {"error": "Could not validate credentials"}

# Custom 404 error
@app.exception_handler(404)
async def not_found(request, exc):
    return {"error": "404 - Not Found"}
