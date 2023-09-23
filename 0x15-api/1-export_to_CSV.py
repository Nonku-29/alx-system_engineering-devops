import requests
import csv

def export_employee_todo_csv(employee_id):
    # Make request to API
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    # Parse response
    todos = response.json()
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user = user_response.json()
    employee_name = user["username"]

    # Write to CSV file
    with open(f"{employee_id}.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([todo["userId"], employee_name, todo["completed"], todo["title"]])

# Example usage
export_employee_todo_csv(1)
