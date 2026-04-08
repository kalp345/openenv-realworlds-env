from pydantic import BaseModel
from typing import Any, Dict

class Observation(BaseModel):
    task_id: str
    content: str
    metadata: Dict[str, Any] = {}

class Action(BaseModel):
    response: str

class Reward(BaseModel):
    score: float
    feedback: str
