#!/usr/bin/python3
"""Export data in the JSON format."""

import json
import sys
from urllib.request import urlopen


def get_employee_todo_progress(employee_id):
    """
    Args: Employee ID for which to retrieve progress.
    Returns: List of dictionaries representing tasks for the employee.
    """
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?" \
               f"userId={employee_id}"

    with urlopen(api_url) as response:
        user_data = json.load(response)

    with urlopen(todo_url) as response:
        todo_data = json.load(response)

    employee_name = user_data.get("username")
    tasks = [
        {"username": employee_name, "task": task["title"],
         "completed": task["completed"]}
        for task in todo_data
    ]

    return tasks


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python3 script_name.py")
        sys.exit(1)

    all_tasks = {}
    for employee_id in range(1, 11):
        tasks = get_employee_todo_progress(employee_id)
        all_tasks[str(employee_id)] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file, indent=2)

    print("Data exported to todo_all_employees.json")
