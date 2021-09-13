#!/usr/bin/python3
"""
Pings a To-Do API for data on a specified user and saves the data to a CSV file
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(user_id), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(user_id), verify=False).json()

    with open("{}.csv".format(user_id), 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            csvwriter.writerow([int(user_id), user.get('username'),
                                task.get('completed'),
                                task.get('title')])
