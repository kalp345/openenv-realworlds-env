from env.models import Observation, Reward
from env.graders.email_grader import grade_email

class EmailTask:
    def __init__(self):
        self.name = "email_triage"
        self.email = "Subject: Refund Request\nI want my money back"

    def get_observation(self):
        return Observation(
            task_id=self.name,
            content=self.email
        )

    def evaluate(self, action):
        score = grade_email(action.response)
        return Reward(score=score, feedback="Email grading complete")
