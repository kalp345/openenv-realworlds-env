from env.models import Observation, Reward
from env.graders.data_grader import grade_data

class DataTask:
    def __init__(self):
        self.name = "data_cleaning"
        self.data = "name,age\nAlice,25\nBob,??\nCharlie,30"

    def get_observation(self):
        return Observation(
            task_id=self.name,
            content=self.data
        )

    def evaluate(self, action):
        score = grade_data(action.response)
        return Reward(score=score, feedback="Data cleaning graded")
