import joblib
import pandas as pd

# ============================================================
# Load trained model
# ============================================================

model_path = "models/best_model_full.pkl"
model = joblib.load(model_path)

# ============================================================
# Preprocess input data
# ============================================================

def preprocess(data: dict) -> pd.DataFrame:
    """
    Convert JSON input into a pandas DataFrame.
    """

    return pd.DataFrame([data])

# ============================================================
# Predict property price
# ============================================================

def predict(data: dict) -> float:
    """
    Predict the price of a single property.

    Parameters
    ----------
    data : dict
        Property features received from the API.

    Returns
    -------
    float
        Predicted property price.
    """

    input_data = preprocess(data)

    prediction = model.predict(input_data)

    return float(prediction[0])