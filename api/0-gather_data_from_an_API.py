#!/usr/bin/python3

import requests
from sys import argv, exit

def inf_empleados():
    if len(argv) < 2:
        print("You must pass an ID parameter")
        exit()
    
    parametro_id = int(argv[1])

    url_tasks = f"https://jsonplaceholder.typicode.com/todos?userId={parametro_id}"
    url_user_info = f"https://jsonplaceholder.typicode.com/users/{parametro_id}"

    response_tasks = requests.get(url_tasks)
    response_user_info = requests.get(url_user_info)

    if response_tasks.status_code == 200 and response_user_info.status_code == 200:
        tasks_data = response_tasks.json()
        user_info_data = response_user_info.json()

        if not tasks_data or not user_info_data:
            print("Error in deserialization")
            return

        employee_name = user_info_data.get("name", "Unknown")

        completed_tasks = [task for task in tasks_data if task["completed"]]
        num_completed_tasks = len(completed_tasks)
        total_num_tasks = len(tasks_data)

        print(f"Employee {employee_name} has completed {num_completed_tasks}/{total_num_tasks} tasks:")
        
        for task in completed_tasks:
            print(f"\t{task['title']}")
    else:
        print("Status error")

if __name__ == '__main__':
    inf_empleados()

