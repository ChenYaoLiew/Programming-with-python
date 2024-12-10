accounts = open("~/data/user_data.txt", "r").readline()

print(accounts)

# input_username = input("Enter your username:")
# input_password = input("Enter your password:")
#
# def check_account_credentials(username, password):
#     found = False
#
#     for key in accounts:
#         data_username, data_password = accounts.strip().split('||')
#
#         if username == data_username and password == data_password:
#             found = True
#
#     return found
#
# if check_account_credentials(input_username, input_password):
#     print("Welcome, " + input_username + "!")