from Administrator.menu import administrator_user_page
from function.query import *
from function.account_management import register_account
from function.cache import *

def get_user_account_type(username):
    """
    Retrieves the account type associated with a given username.
    
    Args:
        username (str): The username to look up
        
    Returns:
        str or None: The account type if the username exists, None otherwise
    """
    accounts = fetch_data("data/user_data.txt")
    account_type = None

    for data in accounts:
        if data["username"] == username:
            account_type = data["account_type"]
            break

    return account_type

def check_account_credentials(username, password):
    """
    Verifies if the provided username and password match any account in the system.
    If credentials are valid, also caches the user's student ID.
    
    Args:
        username (str): The username to check
        password (str): The password to check
        
    Returns:
        bool: True if credentials are valid, False otherwise
    """
    accounts = fetch_data("data/user_data.txt")
    found = False

    for data in accounts:
        if username == data["username"] and password == data["password"]:
            set_student_id(data["student_id"])
            found = True
            break

    return found

def get_account_info(username):
    """
    To get the specified data and index for a given username. Only can use after user logged in
    Args:
        username (str): account username of the user
    Returns:
        data(list): ["Index of the data in data_list"(int), "data of the user(one user only)"(dict)]
    """
    accounts = fetch_data('data/user_data.txt')

    for index, user in enumerate(accounts):
        if user.get("username") == username:
            return [index, user]

def get_user_data(username):
    """
    Get user data by username
    Args:
        username (str): Username to look up
    Returns:
        dict: User data if found, None if not found
    """
    accounts = fetch_data("data/user_data.txt")
    for data in accounts:
        if data["username"] == username:
            return data
    return None

#Main Thread
def main_thread():
    while True:
        user_input = input("'1' - Login Account \n'2' - Register Account \n'3' - Exit\n => ")
        if user_input == "1":
            input_username = input("Enter your username: ")
            # Get user data and cache student ID immediately
            user_data = get_user_data(input_username)
            if user_data:
                set_student_id(user_data["student_id"])

            input_password = input("Enter your password: ")

            if check_account_credentials(input_username, input_password):
                account_type = get_user_account_type(input_username)

                # Start session loop for logged-in user
                while True:
                    print(f'\nWelcome Back {input_username} ({account_type})')

                    if account_type == 'administrator':
                        choice = administrator_user_page()
                        if choice == 'logout':
                            break  # Break inner loop to return to log in screen
                        elif choice == 'exit':
                            exit()
                    elif account_type == 'student':
                        from Student.menu import student_user_page
                        choice = student_user_page(get_account_info(input_username))
                        if choice == 'logout':
                            break  # Break inner loop to return to log in screen
                        elif choice == 'exit':
                            exit()
                    elif account_type == 'teacher':
                        from Teacher.menu import teacher_menu_page
                        choice = teacher_menu_page()
                        if choice == 'logout':
                            break
                        elif choice == 'exit':
                            exit()
                    elif account_type == 'staff':
                        from Staff.Menu import staff_user_page
                        choice = staff_user_page()
                        if choice == 'logout':
                            break
                        elif choice == 'exit':
                            exit()
            else:
                print("Login failed, please try again.")

        elif user_input == "2":
            input_username = input("Enter your username: ")
            input_password = input("Enter your password: ")
            register_account(input_username, input_password)

        elif user_input == "3":
            exit()
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main_thread()