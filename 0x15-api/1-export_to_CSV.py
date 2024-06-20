#!/usr/bin/python3
"""
Python script that uses REST API,
for a given employee ID,
to information about his/her TODO list progress.
and exports to csv file
"""

import csv
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]

    employee = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    employee_data = employee.json()

    all_todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    )
    todos_list = all_todos.json()

    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode="w", newline="") as csv_fp:
        csv_writer = csv.writer(csv_fp, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        )

        for task in todos_list:
            task_status = task["completed"]
            task_title = task["title"]
            csv_writer.writerow(
                [user_id, employee_data["name"], task_status, task_title]
            )
