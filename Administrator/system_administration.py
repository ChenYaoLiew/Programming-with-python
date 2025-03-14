import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from function.query import *
from function.account_management import register_account

def manage_account():
    """
    Display a menu for account management operations.
    
    This function presents options for viewing, adding, updating,
    and deleting user accounts, or returning to the previous menu.
    
    Parameters:
        None
        
    Returns:
        None
    """
    print("'1' - View Accounts\n'2' - Add Account\n'3' - Update Account\n'4' - Delete Account\n'5' - Back")

    choice = input("Enter your choice: ")
    if choice == '1':
        view_accounts()
    elif choice == '2':
        add_account()
    elif choice == '3':
        update_account()
    elif choice == '4':
        delete_account()
    elif choice == '5':
        return

def fetch_accounts():
    """
    Retrieve all user accounts from the data file.
    
    This function uses the fetch_data utility to get all user account
    records from the user_data.txt file.
    
    Parameters:
        None
        
    Returns:
        list: A list of dictionaries containing user account information
    """
    accounts = fetch_data("data/user_data.txt")

    return accounts

def view_accounts():
    """
    Display all user accounts with their details.
    
    This function retrieves all account records and prints each account's
    username, password, account type, student ID, and fund balance.
    
    Parameters:
        None
        
    Returns:
        None
    """
    account_list = fetch_accounts()
    for account in account_list:
        print(f"Username: {account['username']}, Password: {account['password']}, Account Type: {account['account_type']}, Student ID: {account['student_id']}, Fund: {account['fund']}")
        print("-" * 100)  # Add a separator line between accounts

def add_account_into_db(username, password, account_type):
    """
    Add a new account to the database after verifying username uniqueness.
    
    This function checks if the username already exists and, if not,
    registers a new account with the provided details.
    
    Parameters:
        username (str): Username for the new account
        password (str): Password for the new account
        account_type (str): Type of account to create
        
    Returns:
        None
    """
    accounts = fetch_accounts()

    for data in accounts:
        if username == data["username"]:
            print("Account already exists, Please try another username!")
            return  # Exit the function early if account exists

    register_account(username, password, account_type)

def update_account():
    """
    Update an existing user account's details.
    
    This function allows updating username, password, or account type
    for an existing account. It ensures the new username is unique
    and validates the account type selection.
    
    Parameters:
        None
        
    Returns:
        None
    """
    username = input("Enter username to update: ")
    accounts = fetch_accounts()
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
                    data["account_type"] = "administrator"
                elif type_choice == "2":
                    data["account_type"] = "teacher"
                elif type_choice == "3":
                    data["account_type"] = "student"
                elif type_choice == "4":
                    data["account_type"] = "staff"
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

def add_account():
    """
    Collect user input and register a new account.
    
    This function prompts for username, password, and account type,
    then calls the register_account function to create the account.
    
    Parameters:
        None
        
    Returns:
        None
    """
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

def delete_account():
    """
    Delete a user account from the system.
    
    This function removes an account based on the provided username
    and updates the user data file.
    
    Parameters:
        None
        
    Returns:
        None
    """
    username = input("Enter username: ")
    accounts = fetch_accounts()
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