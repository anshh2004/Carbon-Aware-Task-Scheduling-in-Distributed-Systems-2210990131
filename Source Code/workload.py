# workload.py

import time


def execute_task(step_number):
    print(f"Executing workload step {step_number}...")

    # Simulate computation
    time.sleep(2)

    print(f"Step {step_number} completed.")