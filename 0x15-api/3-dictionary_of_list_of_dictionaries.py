#!/usr/bin/python3
"""
Pings a To-Do API for data for all users and writes it to a JSON file
"""

import json
import requests

if __name__ == '__main__':
    users = requests.get("https://jsonplaceholder.typicode.com/users",
                         verify=False).json()
    user_dict = {}
    username_dict = {}
    for user in users:
        user_id = user.get("id")
        user_dict[user_id] = []
        username_dict[user_id] = user.get("username")

    todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                         verify=False).json()
    for task in todos:
        task_dict = {}
        user_id = task.get("userId")
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username_dict.get(user_id)
        user_dict.get(user_id).append(task_dict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(user_dict, jsonfile)
