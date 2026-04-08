from env.models import Observation, Reward
from env.graders.code_grader import grade_code

class CodeTask:
    def __init__(self):
        self.name = "code_review"
        self.code = "def divide(a, b):\n    return a / b"

    def get_observation(self):
        return Observation(
            task_id=self.name,
            content=self.code
        )

    def evaluate(self, action):
        score = grade_code(action.response)
        return Reward(score=score, feedback="Code review graded")
