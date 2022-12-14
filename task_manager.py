# ===== importing libraries =====
from datetime import date


# ===== Functions =====
# Function to convert and return date formatted as DD MON YYYY
# Args passed should be integers
def date_format(yy, mm, dd):
    cal_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Convert due month int to words
    for count, month in enumerate(cal_months, 1):
        if count == mm:
            mm = month

    # Return formatted date
    return f"{dd} {mm} {yy}"


# Function to register a new user
def reg_user():

    # For loop gets list of existing usernames in user.txt file
    with open('user.txt', 'r') as f:
        existing_usernames = [line.split(', ')[0] for line in f]

    # While loop gets new username and password input from user
    while True:

        # Get new username from user
        new_username = input("Enter a new username: ").lower()

        # Check if username already exists in
        if new_username in existing_usernames:
            print(f"Username {new_username} already exists. Try again...")

        else:
            # Variable to store result from password check
            done_pass_check = False

            # While loop gets password for username from user
            while not done_pass_check:
                new_password = input(f"Enter a new password for {new_username}: ")
                confirm_password = input(f"Confirm password for {new_username}: ")

                if confirm_password == new_password:

                    # Write new line to end of user.txt file and display feedback
                    with open('user.txt', 'a') as f:
                        f.write(f"\n{new_username}, {new_password}")

                    print(f"New user with username {new_username} has been successfully registered!")

                    # Update done password check
                    done_pass_check = True
                else:
                    print("Password does not match, try again.")

            break


# Function to add a new task with task title and task description as parameters
def add_task(t_title, t_description):

    # Set up for loop to get and confirm the username the task is assigned to from user
    while True:

        assigned_to = input("Enter the username the task is assigned to: \n").lower()

        # Boolean to confirm if username is available in user.txt
        confirm_username = False

        # Check lines in user.txt file and update confirm_username to True if match is found
        with open('user.txt', 'r') as f:
            for line in f:
                if assigned_to == line.split(", ")[0]:
                    confirm_username = True

        # Confirm if username entered matches a user and break the while loop
        if confirm_username:
            break
        else:
            print("Username not found.")

    # Get the current day, month, year using now method from imported datetime
    current_date = date.today()
    day, mon, yr = current_date.day, current_date.month, current_date.year

    # Set assigned date as formatted current date
    assigned_date = date_format(yr, mon, day)

    # Get due date input from user and checks entry using try and except.
    # Date must not be in the past
    while True:

        due_date_input = input("Enter the due date for the task (DD-MM-YYYY): \n").split('-')

        try:
            # For loop casts list items in due date input to int and assigns them to day, month and year variables
            due_day, due_mon, due_yr = [int(item) for item in due_date_input]

            # Create a new date object
            due_date = date(due_yr, due_mon, due_day)

        except ValueError as error:
            print(f"Oops! Wrong date entered — {error}")

        finally:
            # Check if date is less than current
            if not due_date < date.today():
                # Get formatted due date
                due_date = date_format(due_yr, due_mon, due_day)
                break
            else:
                print("Due date must not be in the past.")

    # Set task status
    completed_task = 'No'

    # Write new entry at the end of the tasks.txt file
    with open('tasks.txt', 'a') as f:
        f.write(f"\n{assigned_to}, {title}, {description}, {assigned_date}, {due_date}, {completed_task}")

    # Display feedback to user
    print("New task successfully added! \n")


# Function to view and manipulate a single task
def view_single(task_index):
    # Allow user to view specific task by ID No. (indexes) in the current list
    # Get user input and check for correct entry using try and except
    while True:
        try:
            sub_menu = int(input("Enter the ID No. of the task you want to view or -1 to return to the main menu\n: "))

        except ValueError:
            print("Wrong input! Try again...")

        finally:
            if sub_menu == -1:
                break

            elif sub_menu in task_index:
                # Loop through the tasks file and keep count of index
                with open('tasks.txt', 'r') as f:

                    for count, line in enumerate(f):

                        # Get the task details at index number (sub_menu)
                        if count == sub_menu:
                            line = line.split(', ')
                            task_status = line[5].replace('\n', '')

                            # Display formatted single task
                            print("———————————————————————————————————————————————————————————————————————————— \n"
                                  f"Task:                   {line[1]} \n"
                                  f"Assigned to:            {line[0]} \n"
                                  f"Date assigned:          {line[3]} \n"
                                  f"Due date:               {line[4]} \n"
                                  f"Task Complete?          {task_status} \n"
                                  f"Task description:       \n {line[2]} \n"
                                  "————————————————————————————————————————————————————————————————————————————")

                if username == "admin":
                    while True:
                        # Allow user to edit/mark task as complete or return to previous menu
                        task_menu = input("Enter 'E' to edit this task, 'C' to mark as complete, "
                                          "or '-1' to return to previous menu: \n").lower()

                        if task_menu == "e":

                            # Only uncompleted tasks can be edited
                            if task_status == "Yes":
                                print("Oops! Only uncompleted tasks can be edited.")

                            else:
                                # Set up for loop to get and confirm the username the task is reassigned to from user
                                while True:

                                    # Username the task is assigned to and due date of task can be edited
                                    new_user = input("Enter the username you want to reassign this task to: \n").lower()

                                    # Boolean to confirm if username is available in user.txt
                                    confirm_username = False

                                    # Check lines in user.txt file and update confirm_username to True if match is found
                                    with open('user.txt', 'r') as f:
                                        for line in f:
                                            if new_user == line.split(", ")[0]:
                                                confirm_username = True

                                    # Confirm if username entered matches a user and break the while loop
                                    if confirm_username:
                                        break
                                    else:
                                        print("Username not found.")

                                # Get due date input from user and checks entry using try and except.
                                # Date must not be in the past
                                while True:

                                    new_due_date = input("Change the due date for the task (DD-MM-YYYY): \n").split(
                                            '-')

                                    try:
                                        # For loop casts list items in due date input to int and
                                        # assigns them to day, month and year variables
                                        due_day, due_mon, due_yr = [int(item) for item in new_due_date]

                                        # Create a new date object
                                        due_date = date(due_yr, due_mon, due_day)

                                    except ValueError as error:
                                        print(f"Oops! Wrong date entered — {error}")

                                    finally:
                                        # Check if date is less than current
                                        if not due_date < date.today():
                                            # Get formatted due date
                                            due_date = date_format(due_yr, due_mon, due_day)
                                            break
                                        else:
                                            print("Due date must not be in the past.")

                                # Access the tasks file and read the lines
                                # Get the line with index of current task in view and split the line
                                # Update [0] and [4] indexes of line, join list
                                with open('tasks.txt', 'r') as f:
                                    tasks_data = f.readlines()
                                    edited_data = tasks_data[sub_menu].split(', ')
                                    edited_data[0] = new_user
                                    edited_data[4] = due_date
                                    tasks_data[sub_menu] = ", ".join(edited_data)

                                # Overwrite tasks.txt file with updated data
                                with open('tasks.txt', 'w') as f:
                                    f.writelines(tasks_data)

                                    # Display feedback
                                    print(f"Awesome! You have updated the task with ID {sub_menu}.")
                                    break

                        elif task_menu == "c":

                            if task_status == "Yes":
                                print("Task is already marked as completed.")

                            else:
                                # Access the tasks file and read the lines
                                # Get the line with index of the current task in view and split the line
                                # Update last index of line, join list
                                with open('tasks.txt', 'r') as f:
                                    tasks_data = f.readlines()
                                    edited_data = tasks_data[sub_menu].split(', ')
                                    edited_data[5] = "Yes\n"
                                    tasks_data[sub_menu] = ", ".join(edited_data)

                                # Overwrite tasks.txt file with updated data
                                with open('tasks.txt', 'w') as f:
                                    f.writelines(tasks_data)

                                    # Display feedback
                                    print(f"Awesome! You have marked the task with ID {sub_menu} as complete.")
                                    break

                        elif task_menu == '-1':
                            break

                        else:
                            print("Wrong input! Try again...")

                else:
                    # Go back to main menu if task is completed or mark uncompleted task
                    if task_status == "Yes":
                        break

                    else:
                        while True:
                            # Get input from user to mark task as complete or not
                            status = input("Do you want to mark this task as complete? Enter Yes/No: \n").lower()

                            if status == "yes":

                                # Check if user can mark task as complete. Only admins can edit other's tasks.
                                if username == line[0]:

                                    # Access the tasks file and read the lines
                                    # Get the index of the current task in view and split the line
                                    # Update last index of line, join list and overwrite tasks.txt file with new data
                                    with open('tasks.txt', 'r') as f:
                                        tasks_data = f.readlines()
                                        edited_data = tasks_data[sub_menu].split(', ')
                                        edited_data[5] = "Yes\n"
                                        tasks_data[sub_menu] = ", ".join(edited_data)

                                    with open('tasks.txt', 'w') as f:
                                        f.writelines(tasks_data)

                                        # Display feedback
                                        print(f"Awesome {username}! You have completed the task with ID {sub_menu}.")
                                else:
                                    print("You don't have access to mark other's tasks as complete.")

                                break
                            elif status == "no":
                                break
                            else:
                                print("Wrong input! Try again...")

                        break
            else:
                print("The ID No. you entered is out of range.")


# Function to view all tasks
def view_all():
    # Heading
    print(f"""ID No.   Task                                      Due Date        Completed
————————————————————————————————————————————————————————————————————————————""")
    # Keep list of indexes associated with user's tasks
    task_index = []

    # For loop keeps count of indexes in tasks.txt file associated with user
    with open('tasks.txt', 'r') as f:
        for count, line in enumerate(f):

            # Split the line and get the title, due_date, task_status
            line = line.split(', ')
            title, due_date, task_status = line[1], line[4], line[5].replace('\n', '')

            # Gets the first 30 chars of task title and appends spaces; and if less than 30, appends needed spacing
            if len(title) > 30:
                task_title = f"{title[:35]}...\t  "
            else:
                task_title = f"{title} {' ' * (40 - len(title))}"

            # Append index to task_index and display formatted strings
            task_index.append(count)

            print(f"{count}        {task_title} {due_date}\t   {task_status}")

    # Call the view_single function and pass in the task_index list
    view_single(task_index)


# Function to view tasks assigned to the signed-in user
def view_mine():

    # Heading
    print(f"""ID No.   Task                                      Due Date          Completed
————————————————————————————————————————————————————————————————————————————""")

    # Keep list of indexes associated with user's tasks
    task_index = []

    # For loop keeps count of indexes in tasks.txt file associated with user
    with open('tasks.txt', 'r') as f:
        for count, line in enumerate(f):

            if line.split(', ')[0] == username:

                # Split the line and get the title, due_date, task_status
                line = line.split(', ')
                title, due_date, task_status = line[1], line[4], line[5].replace('\n', '')

                # Gets the first 30 chars of task title and appends spaces; and if less than 30, appends needed spacing
                if len(title) > 30:
                    task_title = f"{title[:35]}...\t  "
                else:
                    task_title = f"{title} {' ' * (40 - len(title))}"

                # Append index to task_index and display formatted strings
                task_index.append(count)

                print(f"{count}        {task_title} {due_date}\t   {task_status}")

    # Call the view_single function and pass in the task_index list
    view_single(task_index)


# Function to generate reports
def generate_report():
    # ----------- Read the lines in tasks.txt and user.txt files -----------
    with open('tasks.txt', 'r') as tasks_f:
        tasks = tasks_f.readlines()

    with open('user.txt', 'r') as user_f:
        users = user_f.readlines()
        # Get list of usernames
        users = [user.split(', ')[0] for user in users]

    # ----------- Get total number of tasks generated and tracked -----------
    total_tasks = len(tasks)

    # ----------- Get total number of completed tasks -----------
    completed_tasks_list = [task for task in tasks if task.split(', ')[5].replace('\n', '') == "Yes"]
    completed_tasks = len(completed_tasks_list)

    # ----------- Get total number of uncompleted tasks -----------
    uncompleted_tasks_list = [task for task in tasks if task.split(', ')[5].replace('\n', '') == "No"]
    uncompleted_tasks = len(uncompleted_tasks_list)

    # ----------- Get total number of tasks that haven't been completed and are overdue -----------
    # Empty list to store tasks
    uncompleted_overdue_tasks_list = []

    for task in uncompleted_tasks_list:

        # Get the formatted due date string
        due_date_items = task.split(', ')[4].split()

        # Convert the due_date_items to date object by replacing the month with corresponding number 1 - 12
        cal_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        for count, month in enumerate(cal_months, 1):
            if month == due_date_items[1]:
                due_date_items[1] = str(count)

        # Convert due date items to int
        due_date_items = [int(item) for item in due_date_items]

        # Create new date object from due date items
        due_date = date(due_date_items[2], due_date_items[1], due_date_items[0])

        # Check if due date is in the past and append task to uncompleted overdue tasks list
        if due_date < date.today():
            uncompleted_overdue_tasks_list.append(task)

    # Number of tasks that haven't been completed and are overdue
    uncompleted_overdue_tasks = len(uncompleted_overdue_tasks_list)

    # ----------- Percentage of tasks that are incomplete -----------
    percent_uncompleted = round(uncompleted_tasks / total_tasks * 100, 2)

    # ----------- Percentage of overdue tasks -----------
    percent_overdue = round(uncompleted_overdue_tasks / total_tasks * 100, 2)

    # ----------- Total number of users -----------
    total_users = len(users)

    # Write/overwrite a task_overview.txt file and generate task overview report
    to_file = open('task_overview.txt', 'w')
    to_file.write(f"""TASK OVERVIEW REPORT
———————————————————————————————————————————————————————————
Total number of tasks:                              {total_tasks}
Total number of completed tasks:                    {completed_tasks}
Total number of uncompleted tasks:                  {uncompleted_tasks}
Total number of uncompleted and overdue tasks:      {uncompleted_overdue_tasks}
% of uncompleted tasks:                             {percent_uncompleted}
% of overdue tasks:                                 {percent_overdue}""")

    # Write/overwrite a user_overview.txt file and generate users overview report
    uo_file = open('user_overview.txt', 'w')
    uo_file.write(f"""USER OVERVIEW REPORT
———————————————————————————————————————————————————————————
Total number of users:              {total_users}
Total number of tasks:              {total_tasks}

Username        Tasks #       Total Tasks %      Completed %      Uncompleted %     Overdue %
—————————————————————————————————————————————————————————————————————————————————————————————\n""")

    # For each user in user.txt file
    for user in users:

        # _____ list of users tasks
        user_tasks_list = [task for task in tasks if task.split(', ')[0] == user]

        # ----- total number of user's tasks
        user_tasks = len(user_tasks_list)

        try:
            # ----- percentage of total number of tasks assigned to user
            user_tasks_percent = round(user_tasks / total_tasks * 100, 2)

        except ZeroDivisionError:
            user_tasks_percent = 0.0

        # ----- completed user tasks
        user_completed_tasks_list = [task for task in user_tasks_list if
                                     task.split(', ')[5].replace('\n', '') == "Yes"]
        user_completed_tasks = len(user_completed_tasks_list)

        # ----- uncompleted user tasks
        user_uncompleted_tasks_list = [task for task in user_tasks_list if
                                       task.split(', ')[5].replace('\n', '') == "No"]
        user_uncompleted_tasks = len(user_uncompleted_tasks_list)

        try:
            # ----- percentage of completed tasks assigned to user
            user_percent_completed = round(user_completed_tasks / user_tasks * 100, 2)

            # ----- percentage of uncompleted tasks assigned to user
            user_percent_uncompleted = round(user_uncompleted_tasks / user_tasks * 100, 2)

        except ZeroDivisionError:
            user_percent_completed = 0.0
            user_percent_uncompleted = 0.0

        # ----- percentage of uncompleted and overdue tasks assigned to user
        user_uncompleted_overdue_tasks_list = []

        for task in user_uncompleted_overdue_tasks_list:

            # Get the formatted due date string
            due_date_items = task.split(', ')[4].split()

            # Convert the due_date_items to date object by replacing the month with corresponding number 1 - 12
            cal_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

            for count, month in enumerate(cal_months, 1):
                if month == due_date_items[1]:
                    due_date_items[1] = str(count)

            # Convert due date items to int
            due_date_items = [int(item) for item in due_date_items]

            # Create new date object from due date items
            due_date = date(due_date_items[2], due_date_items[1], due_date_items[0])

            # Check if due date is in the past and append task to uncompleted overdue tasks list
            if due_date < date.today():
                user_uncompleted_overdue_tasks_list.append(task)

        # number of uncompleted and overdue tasks assigned to user
        user_uncompleted_overdue_tasks = len(uncompleted_overdue_tasks_list)

        try:
            # percentage of uncompleted and overdue tasks assigned to user
            user_percent_uncompleted_overdue = round(user_uncompleted_overdue_tasks / user_tasks * 100, 2)

        except ZeroDivisionError:
            user_percent_uncompleted_overdue = 0.0

        # write the user's overview line
        uo_file.write(f"{user}\t\t\t {user_tasks}\t\t\t\t {user_tasks_percent}\t\t\t {user_percent_completed}\t\t\t "
                      f"{user_percent_uncompleted}\t\t\t\t {user_percent_uncompleted_overdue}\n")

    # Display Feedback and close files
    print("Success! task_overview.txt and user_overview.txt files generated in program directory.")

    uo_file.close()
    to_file.close()


# ===== Login Section =====
print("TASK MANAGER: SIGN IN \n"
      "————————————————————————————————————————————————————————————————————————————")

# Initialise empty string to temporarily store user's details from text file
user_details = ""

# Loop runs while the user_details remains an empty string
while user_details == "":

    username = input("Enter Username: ").lower()

    # For loop through the users.txt file and update user_details with line with a matching username
    with open('user.txt', 'r') as f:
        for line in f:
            if username == line.split(",")[0]:
                user_details = line.replace("\n", "")

    # If user_details is empty, we don't have a match, and back to while loop
    # Else, we have a match. Get user's password and check for match in user_details at index 1 after split
    if user_details == "":
        print("We can't find that username")
    else:
        print("Username found!")
        while True:
            password = input("Enter Password: ")
            if password == user_details.split(", ")[1]:
                print("You're logged in!")
                break
            else:
                print(f"You have entered a wrong password for username {username}.")

while True:

    print("\nTASK MANAGER: MENU \n"
          "————————————————————————————————————————————————————————————————————————————")

    # Presenting different menu options to admin and non-admin users
    # making sure that the user input is converted to lower case.
    if username == 'admin':
        menu = input('''Select one of the following Options below:
r   -   Registering a user
a   -   Adding a task
va  -   View all tasks
vm  -   View my task
gr  -   Generate reports
ds  -   Display statistics
e   -   Exit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()

    if menu == 'r':

        print("TASK MANAGER: REGISTER A NEW USER \n"
              "————————————————————————————————————————————————————————————————————————————")

        # Call the reg_user() function
        reg_user()

    elif menu == 'a':

        print("TASK MANAGER: ADD A NEW TASK \n"
              "————————————————————————————————————————————————————————————————————————————")

        # Get more user inputs about the new task
        title = input("Enter the title of the task: \n")
        description = input("Enter the description of the task: \n")

        # Call the add_task() function pass user inputs as arguments
        add_task(title, description)

    elif menu == 'va':
        print("TASK MANAGER: ALL TASKS \n"
              "————————————————————————————————————————————————————————————————————————————")

        # Call the view_all() function
        view_all()

    elif menu == 'vm':

        print("TASK MANAGER: YOUR TASKS\n"
              "————————————————————————————————————————————————————————————————————————————")

        # Call the view_mine function
        view_mine()

    elif menu == 'gr':
        # Call generate report function
        generate_report()

    elif menu == 'ds':

        print("TASK MANAGER: STATISTICS \n"
              "————————————————————————————————————————————————————————————————————————————")

        # Display reports generated in external files task_overview.txt and user_overview.txt
        try:
            task_report_file = open('task_overview.txt', 'r')
            user_report_file = open('user_overview.txt', 'r')

        except FileNotFoundError:
            # Call generate report function if files are not found in program directory
            generate_report()

            print()

        finally:
            task_report_file = open('task_overview.txt', 'r')
            user_report_file = open('user_overview.txt', 'r')

            # Display the task_overview.txt report to the screen
            for line in task_report_file:
                print(line.replace('\n', ''))

            print()

            # Display the user_overview.txt report to the screen
            for line in user_report_file:
                print(line.replace('\n', ''))

            # Close open files
            task_report_file.close()
            user_report_file.close()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
