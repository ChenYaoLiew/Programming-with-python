# 1. System Administration: Manage user accounts and credentials for all system users (teachers, students, staff). 
# 2. Student Management: Oversee student records, including viewing and updating personal details, enrollment status, and academic performance. 
# 3. Course Management: Create, update, or delete course offerings and assign instructors to courses. 
# 4. Class Schedule: Maintain and update class schedules, ensuring no overlap and proper resource allocation. 
# 5. Report Generation: Generate academic performance, attendance, and financial reports for students and the institution.

def fetchAccounts():
    account_list = []
    file = open('data/user_data.txt', 'r')
    for line in file:
        if line.strip():
            account = line.strip('\n').split(',')
            account_list.append({
                'Account ID': account[0],
                'Account Name': account[1],
                'Account Type': account[2]
                # float makes it a scientific number
            })
    file.close()
    return account_list

def viewAccounts():
    account_list = fetchAccounts()
    for account in account_list:
        print(f"Account ID: {account['Account ID']}, Account Name: {account['Account Name']}, Account Type: {account['Account Type']}")

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

def addAccountIntoDB(username, password, account_type):
    accounts = load_accounts_from_file("data/user_data.txt")

    for data in accounts:
        if username == data["username"]:
            print("Account already exists, Please try another username!")
            return  # Exit the function early if account exists

    # Add the new account to the accounts list
    new_account = {"username": username, "password": password, "accountType": account_type}
    accounts.append(new_account)

    # Save the updated accounts list back to the file
    with open("data/user_data.txt", "w") as accountsFile:
        # Write the list to the file manually
        for account in accounts:
            account_string = f'{{"username": "{account["username"]}", "password": "{account["password"]}", "accountType": "{account["accountType"]}"}}\n'
            accountsFile.write(account_string)

    print(f"Account for {username} successfully registered.")

def addAccount():
    username = input("Enter username: ")
    password = input("Enter password: ")
    account_type = input("Enter account type: ")
    pass

def manageAccount():
    print("'1' - View Accounts\n'2' - Add Account\n'3' - Update Account\n'4' - Delete Account")

    choice = input("Enter your choice: ")
    if choice == '1':
        viewAccounts()
    elif choice == '2':
        addAccount()
    elif choice == '3':
        # updateAccount()
        pass
    elif choice == '4':
        # deleteAccount()
        pass

def manageStudent():
    pass

def manageCourse():
    pass

def administrator_user_page():
    print("'1' - System Administration\n'2' - Student Management\n'3' - Course Management\n'4' - Class Schedule\n'5' - Report Generation")
    print("'6' - Back")
    print("'7' - Logout")
    print("'8' - Exit")
    print("'9' - Help")
    print("'10' - About")

    choice = input("Enter your choice: ")
    if choice == '1':
        manageAccount()
    elif choice == '2':
        manageStudent()
    elif choice == '3':
        manageCourse()
    elif choice == '4':
        # manageClassSchedule()
        pass
    elif choice == '5':
        # manageReportGeneration()
        pass
    elif choice == '6':
        # main_thread()
        pass
    elif choice == '7':
        # logout('data/session.txt')
        pass
    elif choice == '8':
        exit()
    elif choice == '9':
        # help()
        pass
    elif choice == '10':
        # about()
        pass
        