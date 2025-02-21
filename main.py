from Administrator.menu import administrator_user_page
from function.query import *
from function.account_management import register_account

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


def generate_student_id(existing_ids):
    """
    Generate a new student ID in format STDXXXX
    Args:
        existing_ids (list): List of existing student IDs
    Returns:
        str: New unique student ID
    """
    # Find the highest number used
    max_num = 0
    for id in existing_ids:
        if id.startswith("STD"):
            try:
                num = int(id[3:])
                max_num = max(max_num, num)
            except ValueError:
                continue
    
    # Generate new ID with number incremented by 1
    new_num = max_num + 1
    return f"STD{new_num:04d}"  # Formats number to 4 digits with leading zeros

#Main Thread
def main_thread():
    while True:
        user_input = input("'1' - Login Account \n'2' - Register Account \n'3' - Exit\n => ")
        if user_input in ['1','2','3']:
            if user_input == "1":
                input_username = input("Enter your username: ")
                input_password = input("Enter your password: ")

                if check_account_credentials(input_username, input_password):
                    account_type = get_user_account_type(input_username)
                    
                    # Start session loop for logged-in user
                    while True:
                        print(f'\nWelcome Back {input_username} ({account_type})')
                        
                        if account_type == 'administrator':
                            choice = administrator_user_page()
                            if choice == 'logout':
                                break  # Break inner loop to return to login screen
                            elif choice == 'exit':
                                exit()
                                
                        elif account_type == 'student':
                            print('"1" - Student Account Management')
                            print('"2" - Course Enrolment')
                            print('"3" - Course Material Access')
                            print('"4" - Grades Tracking')
                            print('"5" - Feedback Submission')
                            print('"6" - Exit')
                            print('"0" - Logout')
                            
                            student_input = input('=> ')
                            if student_input == '0':
                                break  # Break inner loop to return to login screen
                            elif student_input == '6':
                                exit()
                            # Add other student menu options here
                            
                        elif account_type == 'teacher':
                            # Add teacher menu options here
                            pass
                            
                        elif account_type == 'staff':
                            # Add staff menu options here
                            pass
                            
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