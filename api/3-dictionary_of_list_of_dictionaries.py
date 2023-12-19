#!/usr/bin/python3
"""Script to export data in the JSON format.."""

import json
import requests
from sys import argv


def fetch_user_data(api_url, user_id):
    user_data = requests.get(api_url + f"users/{user_id}").json()
    user_tasks = requests.get(api_url + f"users/{user_id}/todos").json()
    user_completed_tasks = [{"username": user_data["username"],
                             "task": task["title"], "completed":
                                 task["completed"]} for task in user_tasks]
    return user_id, user_completed_tasks


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"

    if len(argv) != 1:
        print("Usage: python script.py")
        exit(1)

    all_employees_tasks = {}

    for user_id in range(1, 11):
        user_id, user_completed_tasks = fetch_user_data(api_url, user_id)
        all_employees_tasks[str(user_id)] = user_completed_tasks

    output_file = "todo_all_employees.json"
    with open(output_file, "w") as file:
        json.dump(all_employees_tasks, file, indent=2)
