from fastapi import FastAPI
from app.predict.logic import predict_label
from app.schemas.input import LandmarkInput
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)


@app.post("/predict")
def predict(data: LandmarkInput):
    return predict_label(data)
