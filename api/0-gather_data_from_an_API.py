#!/usr/bin/python3
"""Python script that, using REST API"""
import json
import requests
import sys

def get_employee_todo_list(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch user data
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch user's todos
    todo_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todo_list = todo_response.json()

    # Calculate progress
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task['completed'])

    # Print progress and completed tasks
    print(f'Employee Name: {employee_name} {"OK" if len(employee_name) == 18 else "Incorrect"}')

    # Print titles of completed tasks
    print(f'Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):')

    # Print titles of completed tasks
    for task in todo_list:
        if task['completed']:
            print(f'\t{task["title"]}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list(employee_id)

