import requests

def get_employee_todo_progress(employee_id):
    # Make request to API
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    # Parse response
    todos = response.json()
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo["completed"]]
    num_done_tasks = len(done_tasks)
    employee_name = todos[0]["userId"]

    # Get user name from API
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user = user_response.json()
    employee_name = user["name"]

    # Print progress report
    print(f"Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")

# Example usage
get_employee_todo_progress(1)
