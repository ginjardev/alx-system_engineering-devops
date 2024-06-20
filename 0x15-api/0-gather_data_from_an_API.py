#!/usr/bin/python3
"""
Python script that uses REST API,
for a given employee ID,
to information about his/her TODO list progress.
"""

import sys

import requests

user_id = sys.argv[1]
if __name__ == "__main__":

    employee = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )
    employee_data = employee.json()

    all_todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    )
    todos_list = all_todos.json()

    all_todos_count = len(todos_list)

    completed_tasks = 0
    for task in todos_list:
        if task["completed"] is True:
            completed_tasks = completed_tasks + 1

    print(
        f"Employee {employee_data['name']} is done "
        f"with tasks({completed_tasks}/{all_todos_count}): "
    )
    for task in todos_list:
        if task["completed"] is True:
            print(f"\t {task['title']}")
