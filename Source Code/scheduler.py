import requests
import time
import random

from config import (
    USERNAME,
    PASSWORD,
    CARBON_THRESHOLD,
    TOTAL_TASK_STEPS,
)

from workload import execute_task
from emissions import calculate_emission
from checkpoint import save_checkpoint, load_checkpoint


class CarbonAwareScheduler:

    def __init__(self):
        self.token = None
        self.total_emissions = 0

    def authenticate(self):

        url = "https://api2.watttime.org/v2/login"

        response = requests.get(
            url,
            auth=(USERNAME, PASSWORD)
        )

        if response.status_code == 200:
            self.token = response.json()["token"]
            print("Authenticated with WattTime API")

        else:
            print("Authentication failed")
            print("Running in simulation mode")

    def get_current_moer(self):

        # Simulated MOER values
        moer = random.randint(400, 1400)

        return moer

    def run(self):

        self.authenticate()

        start_step = load_checkpoint()

        print(f"Resuming from step {start_step}")

        for step in range(start_step, TOTAL_TASK_STEPS):

            moer = self.get_current_moer()

            print(f"Current MOER: {moer}")

            if moer < CARBON_THRESHOLD:

                print("Green energy available -> RUNNING TASK")

                execute_task(step + 1)

                emission = calculate_emission(moer)

                self.total_emissions += emission

                save_checkpoint(step + 1)

                print(f"Emission for step: {emission:.2f}")
                print(f"Total emissions: {self.total_emissions:.2f}\n")

            else:

                print("High carbon intensity -> PAUSING TASK")
                print("Waiting for cleaner energy...\n")

                time.sleep(5)

                continue

        print("All tasks completed successfully.")
        print(f"Final carbon emissions: {self.total_emissions:.2f}")