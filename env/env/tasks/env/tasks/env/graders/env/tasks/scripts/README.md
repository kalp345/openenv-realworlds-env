# OpenEnv Real-World Environment

## Overview
This environment simulates real-world tasks:
- Email triage
- Data cleaning
- Code review

## Run

pip install -r requirements.txt
python scripts/run_baseline.py

## Docker

docker build -t openenv .
docker run openenv
