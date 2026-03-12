# Roman Urdu Cyber Abuse Detection

An AI-powered web application that detects cyber abusive comments written in Roman Urdu.  
The system uses a Machine Learning model to classify whether a comment is abusive or not and provides a simple web interface for users to analyze text.

## Features

- Detects abusive language in Roman Urdu comments
- Machine Learning classification model
- FastAPI backend for prediction
- HTML + Bootstrap frontend interface
- Real-time comment analysis
- Clean and aesthetic UI design

## Technologies Used

- Python
- Machine Learning (Scikit-learn)
- FastAPI
- HTML
- Bootstrap
- Jinja2
- Pickle / Joblib for model loading

## Project Structure

cyber-abuse-detection/
│
├── app/
│ ├── main.py
│ ├── model.pkl
│ └── vectorizer.pkl
│
├── Notebook and dataset/
│ ├── Updated Model.ipynb
│ └── updated_dataset.csv
│
└── templates/
  └── index.html



## Installation

1. Clone the repository
git clone https://github.com/YOUR_USERNAME/roman-urdu-cyber-abuse-detection.git

2. Navigate to the project folder
cd roman-urdu-cyber-abuse-detection

3. Install dependencies
pip install fastapi uvicorn scikit-learn jinja2

4. Run the application
python -m uvicorn app.main:app --reload

5. Open in browser
http://127.0.0.1:8000

## Example
Input Comment:
tum bilkul bekar ho

Output:
Prediction: Abusive


## Purpose

The goal of this project is to help detect harmful language in Roman Urdu comments commonly found on social media platforms such as YouTube, Facebook, and Twitter.

## Future Improvements

- Real-time comment moderation
- Abuse severity detection
- Highlight abusive words
- Deep learning model (LSTM/BERT)
- Dashboard for analytics
