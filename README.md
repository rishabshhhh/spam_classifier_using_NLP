# SPAM or HAM Classifier API
This repository contains code for a FastAPI-based API that classifies text paragraphs into SPAM or HAM (non-SPAM) using a Multinomial Naive Bayes classifier. The classifier is trained on a dataset of labeled messages, and the API provides an endpoint for making predictions.

# Files
data_get.py: Python script containing Natural Language Processing (NLP) functions, data preprocessing, and model training.
api_app.py: FastAPI script defining the API structure, endpoints, and integration with the NLP functions for text classification.
Setup and Dependencies
Before running the API, ensure you have the required dependencies installed. Run the following commands in your terminal: pip install -r requirements.txt

# Running the API
To start the FastAPI server, run the following command: uvicorn api_app:app --host 127.0.0.1 --port 8000 --reload

This will launch the API at http://127.0.0.1:8000.

# API Endpoints
# 1. /status (GET)
Description: Check the API's connection status.
Endpoint: /status
Response: { "status": "API connected successfully" }
# 2. /spam_classifier_ (POST)
Description: Classify text paragraphs into SPAM or HAM.
Endpoint: /spam_classifier_
Request Method: POST
# Request Payload Format:

{
  "input_text": '["this is your email text which you can simply copy and paste"]'
}

- Response Format: "SPAM" or "HAM".

# Usage
Check the API status: curl -X GET "http://127.0.0.1:8000/status"

Classify text paragraphs (example using cURL): curl -X POST "http://127.0.0.1:8000/spam_classifier_" -H "Content-Type: application/json" -d '{"input_text": "Your text here"}'


# Example Response: "HAM"

Additional Notes
The NLP functions and model training are implemented in data_get.py.
The FastAPI structure and API endpoints are defined in api_app.py.
The model is a Multinomial Naive Bayes classifier trained on a dataset of labeled messages.
Feel free to explore and integrate this API into your projects!
