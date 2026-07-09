# Immo Eliza - Model Deployment 🏠

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Deployment-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)

## 📌 Project Overview

This project is the deployment phase of the **Immo Eliza machine learning project**.

The objective is to make a trained real estate price prediction model available through a complete deployment architecture.

The final application allows users to:

* access the machine learning model through a REST API
* send property information in JSON format
* receive a predicted property price
* use a simple web interface designed for non-technical users

The project combines:

* a **FastAPI backend API**
* a **Docker container**
* a **Render deployment**
* a **Streamlit frontend application**

---

# 🎯 Objectives

The main learning objectives of this project were:

* Deploy a machine learning model through a FastAPI endpoint
* Create an API handling JSON input and output
* Package an application using Docker
* Deploy an API online using Render
* Build a simple user interface with Streamlit
* Connect a frontend application to a backend API

---

# 🏗️ Architecture

The application follows a separated frontend/backend architecture:

```
                 User
                   |
                   v
        Streamlit Web Application
                   |
             HTTP POST request
                   |
                   v
          FastAPI REST API
        (deployed on Render)
                   |
                   v
          Prediction pipeline
                   |
                   v
          XGBoost Regression Model
                   |
                   v
          Predicted property price
```

The Streamlit application communicates with the API by sending property information as JSON.

The API loads the trained machine learning model and returns the prediction.

---

# 📂 Project Structure

```
immo-eliza-deployment/

│
├── api/
│   │
│   ├── app.py                 # FastAPI application and API routes
│   ├── predict.py             # Model loading and prediction functions
│   ├── schemas.py             # API input validation with Pydantic
│   ├── Dockerfile              # Docker configuration
│   ├── requirements.txt        # API dependencies
│   │
│   └── models/
│       └── best_model.pkl      # Trained XGBoost model
│
│
├── streamlit/
│   │
│   ├── app.py                 # Streamlit user interface
│   └── requirements.txt       # Streamlit dependencies
│
│
└── README.md
```

---

# 🤖 Machine Learning Model

The model used in this deployment was trained during the previous **Immo Eliza Machine Learning project**.

The selected model is:

**XGBoost Regressor**

The model achieved the best performance compared to Linear Regression and Random Forest.

## Features used for prediction

### Numerical features

* livable_surface
* bedrooms
* bathrooms

### Categorical features

* state_of_property
* epc_score
* province
* city

The preprocessing pipeline is included inside the saved model artifact:

```
models/best_model.pkl
```

The model handles preprocessing and prediction directly when receiving new property data.

---

# 🚀 FastAPI Backend

The API was developed using FastAPI.

## Available endpoints

## Health check

### GET `/`

Checks if the API is running.

Response:

```json
{
  "status": "alive"
}
```

---

## Prediction endpoint

### POST `/predict`

Receives property information in JSON format and returns a predicted price.

Example request:

```json
{
  "livable_surface": 120,
  "bedrooms": 3,
  "bathrooms": 1,
  "state_of_property": "good",
  "epc_score": "B",
  "province": "brussels",
  "city" : "brussels"
}
```

Example response:

```json
{
  "prediction": 825000.0,
  "status_code": 200
}
```

FastAPI automatically generates interactive documentation:

```
/docs
```

---

# 🐳 Docker Deployment

The API is packaged using Docker.

The Dockerfile:

* installs Python dependencies
* copies the application files
* starts the FastAPI server with Uvicorn

The Docker image was deployed on Render.

---

# 🌍 Online Deployment

## FastAPI API

The backend API is deployed with Render.

API URL:

```
https://immo-eliza-deployment-jr60.onrender.com
```

Documentation:

```
https://immo-eliza-deployment-jr60.onrender.com/docs
```

---

## Streamlit Application

The frontend application is deployed with Streamlit Community Cloud.

Application URL:

```
https://happiness910-immo-eliza-deployment-streamlitapp-almvzb.streamlit.app
```

---

# 🖥️ Streamlit Application

The Streamlit interface allows non-technical users to predict a property price without interacting directly with the API.

Users can enter:

* surface area
* number of bedrooms
* number of bathrooms
* geographical information
* property condition
* EPC score
* province

The application sends the information to the FastAPI backend and displays the predicted price.

---

# ⚙️ Local Installation

## Clone repository

```bash
git clone <repository_url>
cd immo-eliza-deployment
```

---

# API Installation

Navigate to the API folder:

```bash
cd api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI:

```bash
uvicorn app:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

# Streamlit Installation

Navigate to the Streamlit folder:

```bash
cd streamlit
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* XGBoost
* FastAPI
* Pydantic
* Docker
* Render
* Streamlit
* GitHub

---

# 📌 Future Improvements

Possible improvements:

* Add more input validation
* Improve API error handling
* Add authentication to the API
* Monitor model performance after deployment
* Retrain the model with new real estate data

---

# 👤 Author

Project developed individually as part of the **AI & Data Science Bootcamp at BeCode**.

Connect with me : [LinkedIn - Iness Khatiri](https://www.linkedin.com/in/iness-khatiri-14392a258)