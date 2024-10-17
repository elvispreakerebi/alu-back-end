#!/usr/bin/python3


import requests
import sys

def get_employee_todo_progress(employee_id):
    # Fetch the employee data from the API using .format() for string formatting
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    employee_response = requests.get(employee_url)
    todos_response = requests.get(todos_url)

    # Check if the request was successful
    if employee_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data from the API")
        return

    # Parse JSON response
    employee_data = employee_response.json()
    todos_data = todos_response.json()

    # Extract employee name
    employee_name = employee_data.get('name')

    # Filter completed tasks and count the total
    completed_tasks = [todo for todo in todos_data if todo.get('completed')]
    total_tasks = len(todos_data)
    completed_count = len(completed_tasks)

    # Output the employee's TODO progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_count, total_tasks))

    # Output the title of each completed task
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))

if __name__ == "__main__":
    # Check if an employee ID was passed as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Convert the employee ID from string to an integer
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Fetch and display the TODO list progress for the given employee ID
    get_employee_todo_progress(employee_id)

