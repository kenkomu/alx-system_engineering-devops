#!/usr/bin/python3
"""
    using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.

"""
import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
response.json()
{'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}
response.status_code
