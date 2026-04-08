import os
from openai import OpenAI
from env.environment import RealWorldEnv
from env.models import Action

client = OpenAI(api_key=os.getenv("HF_TOKEN"))

def run():
    env = RealWorldEnv()
    obs = env.reset()
    total_score = 0

    while True:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": obs.content}]
        )

        action = Action(response=response.choices[0].message.content)

        obs, reward, done, _ = env.step(action)
        total_score += reward.score

        if done:
            break

    print("Final Score:", total_score)

if __name__ == "__main__":
    run()
