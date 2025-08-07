import os
from datetime import datetime, date

# Set the datetime string format
DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Define the Task class
class Task:
    def __init__(
        self,
        username=None,
        title=None,
        description=None,
        due_date=None,
        assigned_date=None,
        completed=None
    ):
        self.username = username
        self.title = title
        self.description = description
        self.due_date = due_date
        self.assigned_date = assigned_date
        self.completed = completed

    def to_string(self):
        # Convert task attributes to string format for writing to file
        return f"{self.username};{self.title};{self.description};{self.due_date.strftime(DATETIME_STRING_FORMAT)};{self.assigned_date.strftime(DATETIME_STRING_FORMAT)};{self.completed}"

    def display(self):
        # Return formatted string of task details
        return (
            f"Task: {self.title}\n"
            f"Assigned to: {self.username}\n"
            f"Date Assigned: {self.assigned_date.strftime(DATETIME_STRING_FORMAT)}\n"
            f"Due Date: {self.due_date.strftime(DATETIME_STRING_FORMAT)}\n"
            f"Task Description: {self.description}\n"
            f"Completed: {self.completed}\n"
        )

    def from_string(self, task_str):
        # break down a string to populate the task attributes
        parts = task_str.strip().split(";")
        self.username = parts[0]
        self.title = parts[1]
        self.description = parts[2]
        self.due_date = datetime.strptime(parts[3], DATETIME_STRING_FORMAT)
        self.assigned_date = datetime.strptime(parts[4], DATETIME_STRING_FORMAT)
        self.completed = parts[5] == "True"


# Ensure tasks file exists
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

# Load tasks from file
with open("tasks.txt", 'r') as task_file:
    task_list = []
    for line in task_file:
        task = Task()
        task.from_string(line)
        task_list.append(task)

# Ensure user file exists
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Load users into dictionary
with open("user.txt", 'r') as user_file:
    username_password = {}
    for line in user_file:
        username, password = line.strip().split(';')
        username_password[username] = password

# Prompt for login
logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user in username_password:
        if username_password[curr_user] == curr_pass:
            print("Login Successful!")
            logged_in = True
        else:
            print("Incorrect password")
    else:
        print("User does not exist")


# Validate input string (no semicolons allowed)
def validate_string(input_str):
    return ";" not in input_str and input_str != ""


# Validate username and password inputs
def check_username_and_password(username, password):
    return validate_string(username) and validate_string(password)


# Write updated user credentials to file
def write_usernames_to_file(username_dict):
    with open("user.txt", "w") as out_file:
        for k, v in username_dict.items():
            out_file.write(f"{k};{v}\n")


# Main program loop
while True:
    print("\nSelect one of the following Options:")
    print("r - Registering a user")
    print("a - Adding a task")
    print("va - View all tasks")
    print("vm - View my task")
    if curr_user == "admin":
        print("ds - Display statistics")
    print("e - Exit")
    
    menu = input(": ").lower()

    if menu == 'r':
        if curr_user != "admin":
            print("Only admin can register new users")
            continue
        
        new_username = input("New Username: ")
        if new_username in username_password:
            print("Username already exists")
            continue

        new_password = input("New Password: ")
        confirm_password = input("Confirm Password: ")
        if new_password != confirm_password:
            print("Passwords do not match")
            continue

        if not check_username_and_password(new_username, new_password):
            print("Invalid characters in username or password")
            continue

        username_password[new_username] = new_password
        write_usernames_to_file(username_password)
        print("New user registered successfully!")

    elif menu == 'a':
        task_username = input("Enter the username of the person the task is assigned to: ")
        if task_username not in username_password:
            print("User does not exist")
            continue

        task_title = input("Enter the title of the task: ")
        task_description = input("Enter a description of the task: ")

        while True:
            try:
                task_due_date = input("Enter the due date (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD")

        curr_date = date.today()

        new_task = Task(
            username=task_username,
            title=task_title,
            description=task_description,
            due_date=due_date_time,
            assigned_date=curr_date,
            completed=False
        )

        task_list.append(new_task)
        with open("tasks.txt", "w") as task_file:
            for t in task_list:
                task_file.write(t.to_string() + "\n")

        print("Task successfully added!")

    elif menu == 'va':
        for t in task_list:
            print("-" * 40)
            print(t.display())

    elif menu == 'vm':
        for t in task_list:
            if t.username == curr_user:
                print("-" * 40)
                print(t.display())

    elif menu == 'ds' and curr_user == 'admin':
        num_users = len(username_password)
        num_tasks = len(task_list)
        print("-" * 40)
        print(f"Total users: {num_users}")
        print(f"Total tasks: {num_tasks}")

    elif menu == 'e':
        print("Goodbye!")
        exit()

    else:
        print("Invalid option. Please try again.")
