def change_session(file_path, user_name, user_type ):
    #used for Login or change account
    with open(file_path, 'w') as file:
        file.write(f'{user_name},{user_type}')

def check_session(file_path):
    #check the session file
    #if the file contains user data, it will return the data of the currently logged-in user.
    #if the file has the data "None", it will return False
    with open(file_path, 'r') as file:
        #to split the data into a list
        #if data contain (user,usertype), it will create a list like ['user', 'usertype']
        #if data contain (None), it will create a list like ['None']
        user = file.read().strip().split(',')
        #To check if the list has a user or None
        if len(user) == 2:
            return user
        else:
            return False

def load_accounts_from_file(file_path):
    accounts = []
    with open(file_path, "r") as file:
        for line in file:
            # Remove any extra spaces or newlines from the line
            line = line.strip()

            # Check if the line is a valid dictionary-like string and manually parse it
            if line.startswith("{") and line.endswith("}"):
                # Remove the curly braces
                line = line[1:-1]
                # Split by commas to get key-value pairs
                key_value_pairs = line.split(", ")

                account = {}
                for pair in key_value_pairs:
                    # Split each pair into key and value
                    key, value = pair.split(": ")
                    # Remove extra quotes from keys and values
                    key = key.strip('"')
                    value = value.strip('"')
                    account[key] = value

                # Add the parsed account dictionary to the accounts list
                accounts.append(account)

    return accounts

def get_user_account_type(username):
    accounts = load_accounts_from_file("data/user_data.txt")
    accountType = None

    for data in accounts:
        if data["username"] == username:
            accountType = data["accountType"]
            break

    return accountType

def check_account_credentials(username, password):
    accounts = load_accounts_from_file("data/user_data.txt")
    found = False

    for data in accounts:
        if username == data["username"] and password == data["password"]:
            found = True
            break

    return found

def register_account(username, password):
    # Check if the account already exists in the accounts list
    accounts = load_accounts_from_file("data/user_data.txt")

    for data in accounts:
        if username == data["username"]:
            print("Account already exists, Please try another username!")
            return  # Exit the function early if account exists

    # Add the new account to the accounts list
    new_account = {"username": username, "password": password, "accountType": "user"}
    accounts.append(new_account)

    # Save the updated accounts list back to the file
    with open("data/user_data.txt", "w") as accountsFile:
        # Write the list to the file manually
        for account in accounts:
            account_string = f'{{"username": "{account["username"]}", "password": "{account["password"]}", "accountType": "{account["accountType"]}"}}\n'
            accountsFile.write(account_string)

    print(f"Account for {username} successfully registered.")

def logout(file_path):
    with open(file_path, 'w') as file:
        #change the sessions file into None
        file.write('None')
        print('Logout successful')

#Main Thread
def main_thread():
    while True:
        if not check_session('data/session.txt'):
            while True:
                user_input = input("'1' - Login Account \n'2' - Register Account \n'3' - Exit\n => ")
                if user_input in ['1','2','3']:
                    if user_input == "1":
                        user_input = ""
                        input_username = input("Enter your username:")
                        input_password = input("Enter your password:")

                        if check_account_credentials(input_username, input_password):
                            change_session('data/session.txt', input_username, get_user_account_type(input_username))
                            break
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
        else:
            if check_session('data/session.txt')[1] == 'student':
                # This shit is just for test, I will create a student_user_page function later.
                while True:
                    print(f'Welcome Back {check_session('data/session.txt')[0]}({check_session('data/session.txt')[1]})')
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
                        logout('data/session.txt')
                        break
                    else:
                        print('invalid input')
                        continue
            elif check_session('data/session.txt')[1] == 'teacher':
                pass
            elif check_session('data/session.txt')[1] == 'staff':
                pass
            else:
                pass


main_thread()