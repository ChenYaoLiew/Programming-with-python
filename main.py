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

#Main Thread
def main_thread():
    user_input = input("'1' - Login Account \n'2' - Register Account \n'3' - Exit")

    while user_input:
        if user_input == "1":
            user_input = ""
            input_username = input("Enter your username:")
            input_password = input("Enter your password:")

            if check_account_credentials(input_username, input_password):
                print("Welcome, " + input_username + "!, Account Type: " + get_user_account_type(input_username))
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

main_thread()