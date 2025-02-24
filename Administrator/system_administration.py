import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from function.query import *
from function.account_management import register_account

def manageAccount():
    print("'1' - View Accounts\n'2' - Add Account\n'3' - Update Account\n'4' - Delete Account\n'5' - Back")

    choice = input("Enter your choice: ")
    if choice == '1':
        viewAccounts()
    elif choice == '2':
        addAccount()
    elif choice == '3':
        updateAccount()
    elif choice == '4':
        deleteAccount()
    elif choice == '5':
        from Administrator.menu import administrator_user_page
        administrator_user_page()

def fetchAccounts():
    accounts = fetch_data("data/user_data.txt")

    return accounts

def viewAccounts():
    account_list = fetchAccounts()
    for account in account_list:
        print(f"Username: {account['username']}, Password: {account['password']}, Account Type: {account['accountType']}, Student ID: {account['student_id']}, Fund: {account['fund']}")
        print("-" * 100)  # Add a separator line between accounts

def addAccountIntoDB(username, password, account_type):
    accounts = fetchAccounts()

    for data in accounts:
        if username == data["username"]:
            print("Account already exists, Please try another username!")
            return  # Exit the function early if account exists

    register_account(username, password, account_type)

def updateAccount():
    username = input("Enter username to update: ")
    accounts = fetchAccounts()
    found = False

    for data in accounts:
        if data["username"] == username:
            found = True
            print("\nWhat would you like to update?")
            print("1 - Update Username")
            print("2 - Update Password")
            print("3 - Update Account Type")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                new_username = input("Enter new username: ")
                # Check if new username already exists
                if any(acc["username"] == new_username for acc in accounts):
                    print("Username already exists. Please try another.")
                    return
                data["username"] = new_username
                print("Username updated successfully!")
                
            elif choice == "2":
                new_password = input("Enter new password: ")
                data["password"] = new_password
                print("Password updated successfully!")
                
            elif choice == "3":
                print("\nAvailable account types:")
                print("1 - administrator")
                print("2 - teacher")
                print("3 - student")
                print("4 - staff")
                
                type_choice = input("Enter account type number: ")
                if type_choice == "1":
                    data["accountType"] = "administrator"
                elif type_choice == "2":
                    data["accountType"] = "teacher"
                elif type_choice == "3":
                    data["accountType"] = "student"
                elif type_choice == "4":
                    data["accountType"] = "staff"
                else:
                    print("Invalid account type selected!")
                    return
                print("Account type updated successfully!")
                
            else:
                print("Invalid choice!")
                return
            
            # Save the updated accounts list
            if insert_data("data/user_data.txt", accounts):
                print(f"Account for {username} has been updated successfully.")
            else:
                print("Error saving updates. Please try again.")
            break
    
    if not found:
        print(f"Account with username {username} not found!")

def addAccount():
    username = input("Enter username: ")
    password = input("Enter password: ")
    print("\nAvailable account types:")
    print("1 - Administrator")
    print("2 - Teacher")
    print("3 - Student")
    print("4 - Staff")
    
    type_choice = input("Enter account type number: ")
    
    # Convert choice to actual account type
    if type_choice == "1":
        account_type = "administrator"
    elif type_choice == "2":
        account_type = "teacher"
    elif type_choice == "3":
        account_type = "student"
    elif type_choice == "4":
        account_type = "staff"
    else:
        print("Invalid account type selected!")
        return

    # Try to register the account
    register_account(username, password, account_type)

def deleteAccount():
    username = input("Enter username: ")
    accounts = fetchAccounts()
    found = False

    # Create new list without the account to be deleted
    updated_accounts = []
    for account in accounts:
        if account["username"] == username:
            found = True
        else:
            updated_accounts.append(account)
    
    if found:
        if insert_data("data/user_data.txt", updated_accounts):
            print(f"Account {username} has been deleted successfully.")
        else:
            print("Error deleting account. Please try again.")
    else:
        print(f"Account with username {username} not found!")

def manageCourse():
    print("'1' - View Courses\n'2' - Add Course\n'3' - Update Course\n'4' - Delete Course\n'5' - Back")

    choice = input("Enter your choice: ")
    if choice == '1':
        viewCourses()
    elif choice == '2':
        addCourse()
    elif choice == '3':
        updateCourse()
    elif choice == '4':
        deleteCourse()
    elif choice == '5':
        from Administrator.menu import administrator_user_page
        administrator_user_page()

def viewCourses():
    courses = fetch_data("data/course_data.txt")
    if not courses:
        print("No courses found.")
        return
        
    for course in courses:
        print(f"\nCourse Code: {course['code']}")
        print(f"Course Name: {course['name']}")
        print(f"Instructor: {course['instructor']}")
        print(f"Schedule: {course['schedule']}")
        print("-" * 50)

def addCourse():
    code = input("Enter course code: ")
    courses = fetch_data("data/course_data.txt")
    
    # Check if course code already exists
    for course in courses:
        if code == course["code"]:
            print("Course code already exists!")
            return

    name = input("Enter course name: ")
    instructor = input("Enter instructor username: ")
    
    # Verify instructor exists and is a teacher
    teachers = fetch_data("data/user_data.txt")
    instructor_valid = False
    for teacher in teachers:
        if teacher["username"] == instructor and teacher["accountType"] == "teacher":
            instructor_valid = True
            break
    
    if not instructor_valid:
        print("Invalid instructor! Must be an existing teacher account.")
        return

    # Get schedule
    schedule = []
    print("\nEnter schedule (e.g., 'Mon 10:00-12:00')")
    print("Type 'done' when finished")
    while True:
        time = input("Enter time slot: ")
        if time.lower() == 'done':
            break
        schedule.append(time)

    new_course = {
        "code": code,
        "name": name,
        "instructor": instructor,
        "schedule": schedule
    }

    courses.append(new_course)
    if insert_data("data/course_data.txt", courses):
        print(f"Course {code} successfully added.")
    else:
        print("Error adding course. Please try again.")

def updateCourse():
    code = input("Enter course code to update: ")
    courses = fetch_data("data/course_data.txt")
    found = False

    for course in courses:
        if course["code"] == code:
            found = True
            print("\nWhat would you like to update?")
            print("1 - Update Course Name")
            print("2 - Update Instructor")
            print("3 - Update Schedule")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                course["name"] = input("Enter new course name: ")
                print("Course name updated successfully!")
                
            elif choice == "2":
                new_instructor = input("Enter new instructor username: ")
                # Verify new instructor exists and is a teacher
                teachers = fetch_data("data/user_data.txt")
                instructor_valid = False
                for teacher in teachers:
                    if teacher["username"] == new_instructor and teacher["accountType"] == "teacher":
                        instructor_valid = True
                        break
                
                if not instructor_valid:
                    print("Invalid instructor! Must be an existing teacher account.")
                    return
                    
                course["instructor"] = new_instructor
                print("Instructor updated successfully!")
                
            elif choice == "3":
                schedule = []
                print("\nEnter new schedule (e.g., 'Mon 10:00-12:00')")
                print("Type 'done' when finished")
                while True:
                    time = input("Enter time slot: ")
                    if time.lower() == 'done':
                        break
                    schedule.append(time)
                course["schedule"] = schedule
                print("Schedule updated successfully!")
                
            else:
                print("Invalid choice!")
                return
            
            if insert_data("data/course_data.txt", courses):
                print(f"Course {code} has been updated successfully.")
            else:
                print("Error saving updates. Please try again.")
            break
    
    if not found:
        print(f"Course with code {code} not found!")

def deleteCourse():
    code = input("Enter course code to delete: ")
    courses = fetch_data("data/course_data.txt")
    found = False

    updated_courses = []
    for course in courses:
        if course["code"] == code:
            found = True
        else:
            updated_courses.append(course)
    
    if found:
        if insert_data("data/course_data.txt", updated_courses):
            print(f"Course {code} has been deleted successfully.")
        else:
            print("Error deleting course. Please try again.")
    else:
        print(f"Course with code {code} not found!")