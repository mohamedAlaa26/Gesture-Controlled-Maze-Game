from pydantic import BaseModel
from typing import List

class LandmarkInput(BaseModel):
    landmarks: List[List[float]]  # 21 landmarks, each with x, y, z
