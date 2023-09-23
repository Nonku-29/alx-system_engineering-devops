import requests
import json

def export_all_employees_todo_json():
    # Make request to API
    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    # Parse response
    todos = response.json()
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users_response.json()

    # Create JSON object
    data = {}
    for user in users:
        user_id = user["id"]
        employee_name = user["username"]
        tasks = []
        for todo in todos:
            if todo["userId"] == user_id:
                task = {
                    "username": employee_name,
                    "task": todo["title"],
                    "completed": todo["completed"]
                }
                tasks.append(task)
        data[f"{user_id}"] = tasks

    # Write to JSON file
    with open("todo_all_employees.json", mode="w") as json_file:
        json.dump(data, json_file)

# Example usage
export_all_employees_todo_json()
