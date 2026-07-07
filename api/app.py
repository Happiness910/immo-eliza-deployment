from fastapi import FastAPI, HTTPException
from schemas import Property
from predict import predict


# ============================================================
# Create FastAPI application
# ============================================================

app = FastAPI()


# ============================================================
# Health check endpoint
# ============================================================

@app.get("/")
def home():
    """
    Check if the API is running.
    """

    return {"status": "alive"}


# ============================================================
# Prediction endpoint
# ============================================================

@app.post("/predict")
def predict_property(property: Property):
    """
    Predict the price of a property.
    """

    try:

        prediction = predict(property.model_dump())

        return {
            "prediction": prediction,
            "status_code": 200
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )