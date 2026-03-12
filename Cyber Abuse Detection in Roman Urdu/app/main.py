from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pickle

import joblib

# Load your model
model = joblib.load("app/model.pkl")
vectorizer = joblib.load("app/vectorizer.pkl")

# FastAPI app
app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Prediction route
@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, comment: str = Form(...)):
    # Transform the comment using vectorizer
    comment_vec = vectorizer.transform([comment])
    
    # Make prediction
    prediction_label = model.predict(comment_vec)[0]
    
    # Convert label to readable format (Optional)
    if prediction_label == "A":
        prediction_text = "Abusive"
    else:
        prediction_text = "Not Abusive"
    
    return templates.TemplateResponse("index.html", {"request": request, "prediction": prediction_text})