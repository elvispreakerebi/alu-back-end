#!/usr/bin/python3

""" This is the script """

import requests
import json
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Get employee details
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    employee_response = requests.get(employee_url).json()
    employee_name = employee_response.get('username')

    # Get employee tasks
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todos_response = requests.get(todos_url).json()

    # Prepare JSON data
    tasks = []
    for task in todos_response:
        tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        })

    # Structure the data as required
    json_data = {employee_id: tasks}

    # Prepare JSON filename
    json_filename = "{}.json".format(employee_id)

    # Write data to JSON file
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)

    print("Data exported to {}".format(json_filename))

