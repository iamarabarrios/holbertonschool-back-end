#!/usr/bin/python3
"""Export data in the CSV format."""

import requests
import sys
import csv


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"missing employee id as argument")
        sys.exit(1)

    URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    EMPLOYEE_TODOS = requests.get(f"{URL}/users/{EMPLOYEE_ID}/todos",
                                  params={"_expand": "user"})
    data = EMPLOYEE_TODOS.json()

    EMPLOYEE_NAME = data[0]["user"]["name"]
    TOTAL_NUMBER_OF_TASKS = len(data)
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []

    for task in data:
        if task["completed"]:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(task["title"])

    with open(f"{EMPLOYEE_ID}.csv", "w", newline="",
              encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for title in TASK_TITLE:
            csv_writer.writerow([EMPLOYEE_ID, EMPLOYEE_NAME, "True", title])
