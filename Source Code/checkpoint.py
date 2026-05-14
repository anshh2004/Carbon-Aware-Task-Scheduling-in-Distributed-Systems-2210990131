# checkpoint.py

import json
import os

CHECKPOINT_FILE = "checkpoint.json"


def save_checkpoint(step):
    data = {"last_completed_step": step}

    with open(CHECKPOINT_FILE, "w") as file:
        json.dump(data, file)



def load_checkpoint():
    if not os.path.exists(CHECKPOINT_FILE):
        return 0

    with open(CHECKPOINT_FILE, "r") as file:
        data = json.load(file)

    return data.get("last_completed_step", 0)