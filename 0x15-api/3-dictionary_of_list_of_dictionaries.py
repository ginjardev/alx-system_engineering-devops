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
        emp_tasks = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
        ).json()
        employees_tasks[f"{emp_id}"] = emp_tasks
    
    

    json_filename = "todo_all_employees.json"

    with open(json_filename, mode="w") as json_fp:
        json.dump(employees_tasks, json_fp)
