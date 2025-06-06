import numpy as np
from app.model.load_model import load_model
from app.schemas.input import LandmarkInput

model = load_model()

label_map = {
    0: "like",      # Thumbs up gesture
    1: "dislike",   # Thumbs down gesture  
    2: "peace",        # OK gesture (thumb and index finger circle)
    3: "ok"      # Peace sign (V with index and middle finger)
}

def preprocess(landmarks: list) -> np.ndarray:
    # Flatten the list of [x, y, z] -> [x1, y1, z1, ..., x21, y21, z21]
    return np.array(landmarks).flatten().reshape(1, -1)

def predict_label(data: LandmarkInput):
    features = preprocess(data.landmarks)
    prediction = model.predict(features)[0]
    label = label_map.get(prediction, None)
    return {"label": label}
