#!/usr/bin/python3
"""
Python script that uses REST API,
for a given employee ID,
to information about his/her TODO list progress.
and exports to json file
"""

import json
import requests

if __name__ == "__main__":

    employees = requests.get(
        f"https://jsonplaceholder.typicode.com/users/"
    )
    employees_data = employees.json()

    employees_tasks = {}

    for employee in employees_data:
        emp_id = employee["id"]
        all_tasks = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
        ).json()
        emp_tasks = []
        for task in all_tasks:
            emp_tasks.append(
                {
                    "username": employee["username"],
                    "task": task["title"],
                    "completed": task["completed"]
                }
            )
        employees_tasks[emp_id] = emp_tasks

    json_filename = "todo_all_employees.json"

    with open(json_filename, mode="w") as json_fp:
        json.dump(employees_tasks, json_fp)
