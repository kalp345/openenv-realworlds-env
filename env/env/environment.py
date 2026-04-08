import random
from env.tasks.easy_email import EmailTask
from env.tasks.medium_data_cleaning import DataTask
from env.tasks.hard_code_review import CodeTask

class RealWorldEnv:
    def __init__(self):
        self.tasks = [EmailTask(), DataTask(), CodeTask()]
        self.current_task = None
        self.done = False

    def reset(self):
        self.current_task = random.choice(self.tasks)
        self.done = False
        return self.current_task.get_observation()

    def step(self, action):
        reward = self.current_task.evaluate(action)

        if reward.score >= 0.9:
            self.done = True

        return (
            self.current_task.get_observation(),
            reward,
            self.done,
            {}
        )

    def state(self):
        return {
            "task": self.current_task.name,
            "done": self.done
        }
