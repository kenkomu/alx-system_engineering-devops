#!/usr/bin/python3
"""
Module that extract data from api
"""

import requests
from sys import argv


if __name__ == "__main__":

    emp_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])

    emp_resp = requests.get(emp_url).json()

    emp_name = emp_resp.get('name')

    payload = {'userId': {argv[1]}}
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
               argv[1])

    total_task = requests.get(todo_url).json()

    task_done = 0
    for task in total_task:
        if task.get('completed'):
            task_done += 1

    print("Employee {} is done with tasks({}/{}):".
          format(emp_name, task_done, len(total_task)))

    for task in total_task:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))
