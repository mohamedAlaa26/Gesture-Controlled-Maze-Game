from fastapi import FastAPI
from app.predict.logic import predict_label
from app.schemas.input import LandmarkInput

app = FastAPI()

@app.post("/predict")
def predict(data: LandmarkInput):
    return predict_label(data)
