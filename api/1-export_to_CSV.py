#!/usr/bin/python3
"""Returns information about his/her TODO list progress using urllib."""

import csv
import json
import sys
from urllib.request import urlopen


def export_to_csv(employee_id, tasks):
    """Export to csv"""
    file_name = f"{employee_id}.csv"
    headers = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(file_name, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerow(headers)

        for task in tasks:
            row = [
                str(employee_id),
                task["username"],
                str(task["completed"]),
                task["title"]
            ]
            csv_writer.writerow(row)

    print(f"Data exported to {file_name}")


def get_employee_todo_progress(employee_id):
    """Todo progress"""
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    base_url = "https://jsonplaceholder.typicode.com/todos?"
    todo_url = f"{base_url}userId={employee_id}"

    with urlopen(api_url) as response:
        user_data = json.load(response)

    with urlopen(todo_url) as response:
        todo_data = json.load(response)

    employee_name = user_data.get("username")

    tasks = [
        {"username": employee_name, "completed": task.get("completed"),
         "title": task.get("title")}
        for task in todo_data
    ]

    return tasks


if len(sys.argv) != 2:
    print("Usage: python3 script_name.py <employee_id>")
else:
    employee_id = int(sys.argv[1])
    tasks = get_employee_todo_progress(employee_id)
    export_to_csv(employee_id, tasks)
