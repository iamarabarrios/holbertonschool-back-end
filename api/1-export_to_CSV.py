#!/usr/bin/python3
"""Export data in the CSV format."""

import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        pass
    else:
        URL = "https://jsonplaceholder.typicode.com"
        EMPLOYEE_ID = sys.argv[1]

        EMPLOYEE_TODOS = requests.get(f"{URL}/users/{EMPLOYEE_ID}/todos",
                                      params={"_expand": "user"})

        data = EMPLOYEE_TODOS.json()

        EMPLOYEE_NAME = data[0]["user"]["username"]

        fileName = f"{EMPLOYEE_ID}.csv"

        with open(fileName, "w", newline="") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)

            for task in data:
                writer.writerow(
                    [EMPLOYEE_ID, EMPLOYEE_NAME, str(task["completed"]),
                     task["title"]]
                )
