from Administrator.system_administration import administrator_user_page
from function.query import *

def get_user_account_type(username):
    accounts = fetch_data("data/user_data.txt")
    accountType = None

    for data in accounts:
        if data["username"] == username:
            accountType = data["accountType"]
            break

    return accountType

def check_account_credentials(username, password):
    accounts = fetch_data("data/user_data.txt")
    found = False

    for data in accounts:
        if username == data["username"] and password == data["password"]:
            found = True
            break

    return found

def register_account(username, password):
    # Check if the account already exists in the accounts list
    accounts = fetch_data("data/user_data.txt")

    for data in accounts:
        if username == data["username"]:
            print("Account already exists, Please try another username!")
            return  # Exit the function early if account exists

    # Add the new account to the accounts list
    new_account = {"username": username, "password": password, "accountType": "user"}
    accounts.append(new_account)

    # Save the updated accounts list using the insert_data function
    if insert_data("data/user_data.txt", accounts):
        print(f"Account for {username} successfully registered.")
    else:
        print("Error registering account. Please try again.")

#Main Thread
def main_thread():
    while True:
        user_input = input("'1' - Login Account \n'2' - Register Account \n'3' - Exit\n => ")
        if user_input in ['1','2','3']:
            if user_input == "1":
                user_input = ""
                input_username = input("Enter your username:")
                input_password = input("Enter your password:")

                if check_account_credentials(input_username, input_password):
                    account_type = get_user_account_type(input_username)
                    if account_type == 'student':
                        while True:
                            print(f'Welcome Back {input_username}({account_type})')
                            student_input = input(
                                '"1" - Student Account Management\n'
                                '"2" - Course Enrolment\n'
                                '"3" - Course Material Access \n'
                                '"4" - Grades Tracking\n'
                                '"5" - Feedback Submission\n'
                                '"6" - Exit \n'
                                '"0" - Logout\n'
                                '=> '
                            )
                            if student_input == '1':
                                pass
                            elif student_input == '2':
                                pass
                            elif student_input == '3':
                                pass
                            elif student_input == '4':
                                pass
                            elif student_input == '5':
                                pass
                            elif student_input == '6':
                                exit()
                            elif student_input == '0':
                                break
                            else:
                                print('invalid input')
                                continue
                    elif account_type == 'teacher':
                        pass
                    elif account_type == 'staff':
                        pass
                    elif account_type == 'administrator':
                        administrator_user_page()
                else:
                    print("Login failed, please try again.")
            elif user_input == "2":
                user_input = ""
                input_username = input("Enter your username:")
                input_password = input("Enter your password:")
                register_account(input_username, input_password)
            elif user_input == "3":
                exit()
        else:
            print("Invalid input, please try again.")
            continue

if __name__ == "__main__":
    main_thread()