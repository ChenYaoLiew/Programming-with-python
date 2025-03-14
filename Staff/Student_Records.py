import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from function.query import *
from function.utils import *
from Staff.Menu import staff_user_page

def read_student_file():
    """
    Read and return all student records from the user data file.
    
    This function retrieves all student records stored in the user_data.txt file
    using the fetch_data utility function.
    
    Parameters:
        None
        
    Returns:
        list: A list of dictionaries containing student records
    """
    # Read and return all student records from file, Returns list of student dictionaries
    student_list = fetch_data("data/user_data.txt")
    return student_list

def update_student_record(student_list):
    """
    Update student records in the file using the query functions
    
    Parameters:
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
        print(f"Error updating student records: {e}")
        return False

def view_records():
    """
    Display all student account records with their details.
    
    This function retrieves all student records and prints each student's 
    username, password, account type, student ID, and fund balance.
    
    Parameters:
        None
        
    Returns:
        None
    """
    account_list = read_student_file()
    for account in account_list:
        print(f"Username: {account['username']}, Password: {account['password']}, Account Type: {account['account_type']}, student_id: {account['student_id']}, Fund: {account['fund']}")
        print("-" * 100)  # Add a separator line between accounts

def deposit(student_id, name):
    """
    Add funds to a student's account.
    
    This function allows a specified amount to be added to a student's
    fund balance after validating the student ID and ensuring the 
    deposit amount is positive.
    
    Parameters:
        student_id (str): ID of the student receiving the deposit
        name (str): Name of the student (for reference)
        
    Returns:
        None
    """
    student_list = read_student_file()
    
    # Check if student exists by ID
    student_exists = validate_student_id(student_id)
    
    if not student_exists:
        print("Student ID not found.")
        return
    
    # Find the student in the list
    student = None
    for s in student_list:
        if s['student_id'] == student_id:
            student = s
            break
            
    amount = input("Enter deposit amount: $")
    if float(amount) < float(0):
        print("Invalid amount. Please enter a positive number.")
        return
    
    # Update the student's fund
    student['fund'] = round(float(student['fund']) + float(amount), 2)

    if update_student_record(student_list):
        print(f"Successfully deposited ${float(amount):.2f}")
        print(f"New balance: ${float(student['fund']):.2f}")

def withdrawal(student_id, name):
    """
    Withdraw funds from a student's account.
    
    This function allows a specified amount to be withdrawn from a student's
    fund balance after validating the student ID, ensuring the withdrawal
    amount is positive, and checking for sufficient funds.
    
    Parameters:
        student_id (str): ID of the student making the withdrawal
        name (str): Name of the student (for reference)
        
    Returns:
        None
    """
    student_list = read_student_file()
    
    # Check if student exists by ID
    student_exists = validate_student_id(student_id)
    
    if not student_exists:
        print("Student ID not found.")
        return
    
    # Find the student in the list
    student = None
    for s in student_list:
        if s['student_id'] == student_id:
            student = s
            break
            
    amount = input("Enter withdraw amount: $")
    if float(amount) < 0:
        print("Invalid amount. Please enter a positive number.")
        return
    if float(student['fund']) - float(amount) < 0:
        print("Insufficient funds. Withdrawal would result in a negative balance.")
        return
    
    # Update the student's fund
    student['fund'] = round(float(student['fund']) - float(amount), 2)

    if update_student_record(student_list):
        print(f"Successfully withdraw ${float(amount):.2f}")
        print(f"New balance: ${float(student['fund']):.2f}")

def transfer(student_id, name):
    """
    Transfer funds from one student's account to another.
    
    This function allows funds to be transferred between student accounts
    after validating both student IDs, ensuring the transfer amount is
    positive, and checking that the sender has sufficient funds.
    
    Parameters:
        student_id (str): ID of the student sending the funds
        name (str): Name of the student (for reference)
        
    Returns:
        None
    """
    student_list = read_student_file()
    
    # Check if student exists by ID
    student_exists = validate_student_id(student_id)
    
    if not student_exists:
        print("Student ID not found.")
        return
    
    # Find the student in the list
    student = None
    for s in student_list:
        if s['student_id'] == student_id:
            student = s
            break
            
    transfer_to_id = input("Transfer to (student_id):")
    
    # Check if recipient exists by ID
    recipient_exists = validate_student_id(transfer_to_id)
    
    if not recipient_exists:
        print("Recipient student ID not found.")
        return
    
    # Find the recipient in the list
    recipient = None
    for s in student_list:
        if s['student_id'] == transfer_to_id:
            recipient = s
            break
            
    amount = input("Enter transfer amount: $")
    
    if float(amount) < 0:
        print("Invalid amount. Please enter a positive number.")
        return

    if float(student['fund']) - float(amount) < 0:
        print("Insufficient funds. Would result in a negative balance.")
        return

    # Update sender's fund
    student['fund'] = round(float(student['fund']) - float(amount), 2)
    # Update recipient's fund
    recipient['fund'] = round(float(recipient['fund']) + float(amount), 2)

    if update_student_record(student_list):
        print(f"Successfully transferred ${float(amount):.2f}")
        print(f"Your new balance: ${float(student['fund']):.2f}")

def manage_student_records():
    # starting point(start the loop)
    while True:
        print("\nStudent Records Management")
        print("'1' - View Student Records")
        print("'2' - Process Deposit")
        print("'3' - Process Withdrawal")
        print("'4' - Process Transfer")
        print("'5' - Back")

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
            deposit(student_id, name)
            continue
        elif choice == '3':
            student_id = input("Enter student_id: ")
            name = input("Enter your name: ")
            withdrawal(student_id, name)
        elif choice == '4':
            student_id = input("Enter student_id: ")
            name = input("Enter your name: ")
            transfer(student_id, name)
        elif choice == '5':
            return