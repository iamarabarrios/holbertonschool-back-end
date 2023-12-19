#!/usr/bin/python3
"""Export data in the JSON format."""

import json
import sys
from urllib.request import urlopen
from urllib.error import URLError


def export_to_json(employee_id, tasks):
    """
    Args: Employee ID, int
    List of tasks for the employee.
    """
    file_name = f"{employee_id}.json"
    data = {str(employee_id): tasks}

    with open(file_name, "w") as json_file:
        json.dump(data, json_file, indent=2)

    print(f"Data exported to {file_name}")


def get_employee_todo_progress(employee_id):
    """
    Args: Employee ID
    Returns: List of tasks for the employee.
    """
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?" \
               f"userId={employee_id}"

    try:
        with urlopen(api_url) as response:
            user_data = json.load(response)

        with urlopen(todo_url) as response:
            todo_data = json.load(response)
    except URLError as e:
        print(f"Error connecting to API: {e}")
        return []

    if not todo_data:
        print(f"No tasks found for employee {employee_id}")
        return []

    employee_name = user_data.get("name")
    tasks = [
        {"task": task["title"], "completed": task["completed"], "username":
            employee_name}
        for task in todo_data
    ]

    return tasks


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        tasks = get_employee_todo_progress(employee_id)

        if tasks:
            export_to_json(employee_id, tasks)
        else:
            print("No tasks to export.")
