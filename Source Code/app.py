# app.py

from scheduler import CarbonAwareScheduler


if __name__ == "__main__":

    scheduler = CarbonAwareScheduler()

    scheduler.run()