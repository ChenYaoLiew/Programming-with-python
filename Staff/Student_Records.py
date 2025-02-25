import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from function.query import *

def read_student_file():
    # Read and return all student records from file, Returns list of student dictionaries
    student_list = fetch_data("data/user_data.txt")
    return student_list

def validate_student_id(student_id, student_list):
    # Check if student_id exists in records
    for student in student_list:
        if student['student_id'] == student_id:
            return True, student
    return False

def validate_student_name(student_name, student_list):
    # Check if username exists in records
    for student in student_list:
        if student['username'] == student_name:
            return True, student
    return False, None

def update_student_record(student_list):
    # Trigger when need update to the text.txt file
    file = read_student_file()
    for student in student_list:
        line = f"{student['student_id']},{student['username']},{student['fund']}\n"
        file.write(line)
    file.close()
    return True

def view_records():
    account_list = read_student_file()
    for account in account_list:
        print(f"Username: {account['username']}, Password: {account['password']}, Account Type: {account['accountType']}, student_id: {account['student_id']}, Fund: {account['fund']}")
        print("-" * 100)  # Add a separator line between accounts

def deposit(student_id,name):
    student_list = read_student_file()
    exists, student = validate_student_id(student_id, student_list) or validate_student_name(name, student_list)

    if not exists:
        print("student_id not found.")
        return
    amount = input("Enter deposit amount: $")
    if (amount) < 0:
        print("Invalid amount. Please enter a positive number.")
        return
    for student in student_list:
        student['fund'] += (amount)
        break

    if update_student_record(student_list):
        print(f"Successfully deposited ${(amount):.2f}")
        print(f"New balance: ${student['fund']:.2f}")

def withdrawal(student_id,name):
    student_list = read_student_file()
    exists, student = validate_student_id(student_id, student_list) or validate_student_name(name, student_list)

    if not exists:
        print("student_id not found.")
        return
    amount = input("Enter withdraw amount: $")
    if (amount) < 0:
        print("Invalid amount. Please enter a positive number.")
        return
    if student['fund'] - (amount) < 0:
        print("Insufficient funds. Withdrawal would result in a negative balance.")
        return
    for student in student_list:
        student['fund'] -= (amount)
        break

    if update_student_record(student_list):
        print(f"Successfully withdraw ${(amount):.2f}")
        print(f"New balance: ${student['fund']:.2f}")

def transfer(student_id,name):
    student_list = read_student_file()
    exists, student = validate_student_id(student_id, student_list) or validate_student_name(name, student_list)
    if not exists:
        print("student_id not found.")
        return
    transfer_to_id = input("Transfer to (student_id):")
    transfer_to_name = input("Transfer to (username):")
    amount = input("Enter transfer amount: $")
    if (amount) < 0:
        print("Invalid amount. Please enter a positive number.")
        return
    exists, student_to = validate_student_id(transfer_to_id, student_list) or validate_student_name(transfer_to_name, student_list)
    if not exists:
        print("student_id not found.")
        return

    if student['fund'] - (amount) < 0 or student_to['fund'] - (amount) < 0:
        print("Insufficient funds. Would result in a negative balance.")
        return

    for student in student_list:
        student['fund'] -= (amount)
        student_to['fund'] += (amount)
        break

    if update_student_record(student_list):
        print(f"Successfully transferred ${(amount):.2f}")
        print(f"Sender's new balance: ${student['fund'] - (amount):.2f}")
        print(f"Recipient's new balance: ${student_to['fund'] + (amount):.2f}")

def manage_student_records():
    # starting point(start the loop)
    while True:
        print("\nStudent Records Management")
        print("1. View Student Records")
        print("2. Process Deposit")
        print("3. Process Withdrawal")
        print("4. Process Transfer")
        print("5. Quit")

        choice = input("\nEnter your choice (1-5): ")

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please try again.")
            continue
        if choice == '1':
            view_records()
            continue
        elif choice == '2':
            student_id = input("Enter student_id: ")
            name = input("Enter your name: ")
            deposit(student_id,name)
            continue
        elif choice == '3':
            student_id = input("Enter student_id: ")
            name = input("Enter your name: ")
            withdrawal(student_id,name)
        elif choice == '4':
            student_id = input("Enter student_id: ")
            name = input("Enter your name: ")
            transfer(student_id,name)
        elif choice == '5':
            break

manage_student_records()
#hi