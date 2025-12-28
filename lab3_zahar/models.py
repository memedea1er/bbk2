from typing import Dict, Tuple, List
from pydantic import BaseModel

class Hypothesis(BaseModel):
    name: str
    prior: float
    evidence_map: Dict[int, Tuple[float, float]]

class AnswerDto(BaseModel):
    evidence_id: int  # Используем evidence_id (с подчеркиванием)
    rating: int