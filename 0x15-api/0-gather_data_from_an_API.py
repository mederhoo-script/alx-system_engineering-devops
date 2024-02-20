#!/usr/bin/python3
''' A Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.'''

import requests
import sys


def fetch_user_info(emp_id):
    """fetch user data

Args:
    emp_id (int): employee id

Returns:
    user data: dict
"""

    users_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    response = requests.get(users_url)
    if response.status_code == 200:
        user_data = response.json()
        return user_data
    else:
        print(f"Failed to fetch user information for employee ID {emp_id}")
        sys.exit(1)


def fetch_todo_list(emp_id):
    """_summary_
    Args:
        emp_id (_type_): _description_
    Returns:
    emp_id (int)
    """
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    response = requests.get(todos_url)
    if response.status_code == 200:
        todos_data = response.json()
        return todos_data
    else:
        print(f"Failed to fetch TODO list for employee ID {emp_id}")
        sys.exit(1)


def main():
    """main
    """
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    emp_id = int(sys.argv[1])

    user_info = fetch_user_info(emp_id)
    todos = fetch_todo_list(emp_id)

    name = user_info['name']
    total_tasks = len(todos)
    done_tasks = [t.get("title") for t in todos if t.get("completed") is True]
    c = len(done_tasks)

    print(f"Employee {name} is done with tasks ({c}/{total_tasks}):")
    for title in done_tasks:
        print("\t{}".format(title))


if __name__ == "__main__":
    main()
