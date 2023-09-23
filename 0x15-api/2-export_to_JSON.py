#!/usr/bin/python3
import requests
import json

def export_employee_todo_json(employee_id):
    # Make request to API
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    # Parse response
    todos = response.json()
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user = user_response.json()
    employee_name = user["username"]

    # Create JSON object
    tasks = []
    for todo in todos:
        task = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": employee_name
        }
        tasks.append(task)
    data = {f"{employee_id}": tasks}

    # Write to JSON file
    with open(f"{employee_id}.json", mode="w") as json_file:
        json.dump(data, json_file)

# Example usage
export_employee_todo_json(1)
