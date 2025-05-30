import pytest
from app.predict.logic import predict_label
from app.schemas.input import LandmarkInput

def test_predict_label():
    # Create dummy 21 landmark points, each with [x, y, z]
    dummy_landmarks = [[0.1 * i, 0.1 * i, 0.1 * i] for i in range(1, 22)]

    input_data = LandmarkInput(landmarks=dummy_landmarks)
    result = predict_label(input_data)

    assert "label" in result
    assert result["label"] in ["up", "down", "left", "right"]
