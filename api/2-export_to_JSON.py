#!/usr/bin/python3
"""Exports TODO list progress in JSON format."""

import requests
from sys import argv
import json

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"

    user_id = argv[1]

    user_data = requests.get(api_url + f"users/{user_id}").json()
    user_tasks = requests.get(api_url + f"users/{user_id}/todos").json()

    user_completed_tasks = [{"task": task["title"], "completed": task[
        "completed"], "username": user_data["username"]
                             } for task in user_tasks]

    output_data = {user_id: user_completed_tasks}

    with open(f"{user_id}.json", "w") as json_file:
        json.dump(output_data, json_file, indent=2)
