#!/usr/bin/python3
"""
Module that extract data from api
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    emp_id = argv[1]
    filename = '{}.json'.format(emp_id)
    emp_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    emp_resp = requests.get(emp_url).json()
    emp_name = emp_resp.get('username')

    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                                                                        emp_id)

    total_task = requests.get(todo_url).json()

    emp_task = []
    for task in total_task:
        row = {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": emp_name
                    }
        emp_task.append(row)

    with open(filename, 'w') as jsfile:
        js_text = {emp_id: emp_task}
        json.dump(js_text, jsfile)
