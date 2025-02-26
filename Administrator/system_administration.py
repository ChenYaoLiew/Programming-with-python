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