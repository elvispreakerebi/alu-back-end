#!/usr/bin/python3

""" this is a script """

import requests
import csv
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Get employee details
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    employee_response = requests.get(employee_url).json()
    employee_name = employee_response.get('username')

    # Get employee tasks
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todos_response = requests.get(todos_url).json()

    # Prepare CSV filename
    csv_filename = "{}.csv".format(employee_id)

    # Open a CSV file and write data
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_response:
            writer.writerow([employee_id, employee_name, task.get('completed'), task.get('title')])

    print("Data exported to {}".format(csv_filename))

