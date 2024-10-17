#!/usr/bin/python3

""" This is a script """

import json
import requests

def export_all_tasks_to_json():
    # Fetch the users and tasks data from the API
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    
    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)
    
    # Check if the requests were successful
    if users_response.status_code == 200 and todos_response.status_code == 200:
        users = users_response.json()
        todos = todos_response.json()
        
        # Create the dictionary to hold all tasks
        all_tasks = {}
        
        # Loop through each user and add their tasks
        for user in users:
            user_id = user["id"]
            username = user["username"]
            
            # Filter tasks by user
            user_tasks = [todo for todo in todos if todo["userId"] == user_id]
            
            # Prepare the list of task details
            tasks_list = [{"username": username, "task": task["title"], "completed": task["completed"]} for task in user_tasks]
            
            # Add to the main dictionary
            all_tasks[user_id] = tasks_list
        
        # Write to a JSON file
        with open("todo_all_employees.json", "w") as json_file:
            json.dump(all_tasks, json_file)
        
        print("Data has been successfully exported to todo_all_employees.json")
    else:
        print("Failed to fetch data from the API")

if __name__ == "__main__":
    export_all_tasks_to_json()

