#!/usr/bin/python3
"""
Pings a To-Do API for data for a specified user and writes it to a JSON file
"""
import csv
import json
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(user_id), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(user_id), verify=False).json()

    username = user.get('username')
    tasks = []
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)

    json_obj = {}
    json_obj[user_id] = tasks
    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump(json_obj, jsonfile)
