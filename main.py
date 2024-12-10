with open("data/user_data.txt", "r") as file:
    accounts = eval(file.read())

input_username = input("Enter your username:")
input_password = input("Enter your password:")

def check_account_credentials(username, password):
    found = False

    for key in accounts:
        if username == key["username"] and password == key["password"]:
            found = True

    return found

if check_account_credentials(input_username, input_password):
    print("Welcome, " + input_username + "!")
else:
    print("Login failed, please try again.")