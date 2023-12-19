#!/usr/bin/python3
"""Export data in the CSV format."""

import csv
import json
import sys
from urllib.request import urlopen


def export_to_csv(employee_id, tasks):
    """
    Export TODO list progress for a given employee to a CSV file.
    Args: Employee ID.
        tasks (list): List of tasks for the employee.
    """
    file_name = f"{employee_id}.csv"
    headers = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(file_name, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(headers)

        for task in tasks:
            task_row = [
                str(employee_id),
                task["username"],
                str(task["completed"]),
                task["title"]
            ]
            csv_writer.writerow(task_row)

    print(f"Data exported to {file_name}")


def get_employee_todo_progress(employee_id):
    """
    Args: Employee ID, int
    Returns: List of tasks for the employee.
    """
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?" \
               f"userId={employee_id}"

    with urlopen(api_url) as response:
        user_data = json.load(response)

    with urlopen(todo_url) as response:
        todo_data = json.load(response)

    employee_name = user_data.get("name")

    tasks = [
        {"username": employee_name, "completed": task["completed"],
         "title": task["title"]}
        for task in todo_data
    ]

    return tasks


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        tasks = get_employee_todo_progress(employee_id)
        export_to_csv(employee_id, tasks)
