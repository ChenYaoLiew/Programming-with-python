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
    return False, None

def validate_student_name(student_name, student_list):
    # Check if username exists in records
    for student in student_list:
        if student['username'] == student_name:
            return True, student
    return False, None

def update_student_record(student_list):
    """
    Update student records in the file using the query functions
    Args:
        student_list (list): List of student dictionaries to update
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Convert all fund values to float and round to 2 decimals before saving
        for student in student_list:
            student['fund'] = round(float(student['fund']), 2)
            
        # Use insert_data function to write the updated list
        success = insert_data("data/user_data.txt", student_list)
        
        if success:
            print("Student records updated successfully.")
            return True
        else:
            print("Error updating student records.")
            return False
            
    except Exception as e:
        print(f"Error updating student records: {str(e)}")
        return False

def view_records():
    account_list = read_student_file()
    for account in account_list:
        print(f"Username: {account['username']}, Password: {account['password']}, Account Type: {account['accountType']}, student_id: {account['student_id']}, Fund: ${float(account['fund']):.2f}")
        print("-" * 100)  # Add a separator line between accounts

def deposit(student_id,name):
    student_list = read_student_file()
    exists, student = validate_student_id(student_id, student_list) or validate_student_name(name, student_list)

    if not exists:
        print("student_id not found.")
        return
    amount = input("Enter deposit amount: $")
    if float(amount) < float(0):
        print("Invalid amount. Please enter a positive number.")
        return
    for student in student_list:
        student['fund'] = round(float(student['fund']) + float(amount), 2)
        break

    if update_student_record(student_list):
        print(f"Successfully deposited ${float(amount):.2f}")
        print(f"New balance: ${float(student['fund']):.2f}")

def withdrawal(student_id,name):
    student_list = read_student_file()
    exists, student = validate_student_id(student_id, student_list) or validate_student_name(name, student_list)

    if not exists:
        print("student_id not found.")
        return
    amount = input("Enter withdraw amount: $")
    if float(amount) < 0:
        print("Invalid amount. Please enter a positive number.")
        return
    if float(student['fund']) - float(amount) < 0:
        print("Insufficient funds. Withdrawal would result in a negative balance.")
        return
    for student in student_list:
        student['fund'] = round(float(student['fund']) - float(amount), 2)
        break

    if update_student_record(student_list):
        print(f"Successfully withdraw ${float(amount):.2f}")
        print(f"New balance: ${float(student['fund']):.2f}")

def transfer(student_id,name):
    student_list = read_student_file()
    exists, student = validate_student_id(student_id, student_list) or validate_student_name(name, student_list)
    if not exists:
        print("student_id not found.")
        return
    transfer_to_id = input("Transfer to (student_id):")
    transfer_to_name = input("Transfer to (username):")
    amount = input("Enter transfer amount: $")
    if float(amount) < 0:
        print("Invalid amount. Please enter a positive number.")
        return
    exists, student_to = validate_student_id(transfer_to_id, student_list) or validate_student_name(transfer_to_name, student_list)
    if not exists:
        print("student_id not found.")
        return

    if float(student['fund']) - float(amount) < 0:
        print("Insufficient funds. Would result in a negative balance.")
        return

    for student in student_list:
        if student['student_id'] == student_id or student['username'] == name:
            student['fund'] = round(float(student['fund']) - float(amount), 2)
        if student['student_id'] == transfer_to_id or student['username'] == transfer_to_name:
            student['fund'] = round(float(student['fund']) + float(amount), 2)

    if update_student_record(student_list):
        print(f"Successfully transferred ${float(amount):.2f}")
        print(f"Your new balance: ${float(student['fund']):.2f}")

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