#!/usr/bin/python3
"""
Module that extract data from api
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    filename = 'todo_all_employees.json'
    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    total_user = requests.get(user_url).json()
    total_task = requests.get(todo_url).json()

    records = {}
    user_task = []

    for user in total_user:
        user_task = []
        for task in total_task:
            if user.get("id") == task.get("userId"):
                row = {
                         "task": task.get('title'),
                         "completed": task.get('completed'),
                         "username": user.get('username')
                         }
                user_task.append(row)
        records[user.get("id")] = user_task

    with open(filename, 'w') as jsfile:
        json.dump(records, jsfile)
