#!/usr/bin/python3
"""Returns information about his/her TODO list progress using urllib."""

import json
import sys
from urllib.request import urlopen


def get_employee_todo_progress(employee_id):
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    base_url = "https://jsonplaceholder.typicode.com/todos?"
    todo_url = f"{base_url}userId={employee_id}"

    with urlopen(api_url) as response:
        user_data = json.load(response)

    with urlopen(todo_url) as response:
        todo_data = json.load(response)

    employee_name = user_data.get("name")
    completed_tasks = [task for task in todo_data if task.get("completed")]
    total_tasks = len(todo_data)

    output = [
        f"Employee {employee_name} is done with tasks("
        f"{len(completed_tasks)}/{total_tasks}): "
    ]

    for task in completed_tasks:
        output.append(f"\t {task['title']}")

    return "\n".join(output)


if len(sys.argv) != 2:
    print("Usage: python3 script_name.py <employee_id>")
else:
    employee_id = int(sys.argv[1])
    result = get_employee_todo_progress(employee_id)
    print(result)
