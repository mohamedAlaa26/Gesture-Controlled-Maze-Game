
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.predict.logic import predict_label
from app.schemas.input import LandmarkInput
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Add CORS middleware to allow frontend to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Instrumentator().instrument(app).expose(app)

@app.post("/predict")
def predict(data: LandmarkInput):
    return predict_label(data)

# Add a health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}