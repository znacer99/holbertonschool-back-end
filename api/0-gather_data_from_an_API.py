#!/usr/bin/python3
"""Write a Python script that, using REST API"""
import json
import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"
    emp_id = sys.argv[1]

    res = requests.get("{}/users/{}/todos".format(api_url, emp_id),
                       params={"_expand": "user"})
    data = res.json()
    employee_name = data[0]["user"]["name"]
    done_tasks_number = 0
    done_tasks_list = []
    for task in data:
        if task["completed"]:
            done_tasks_number += 1
            done_tasks_list.append(task)
    total_tasks = len(data)

    print("Employee {} is done with tasks({}/{}):".format
          (employee_name, done_tasks_number, total_tasks))

    for task in done_tasks_list:
        print("\t {}".format(task["title"]))
