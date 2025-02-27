from function.query import fetch_data
from function.query import insert_data

def change_password(student_info):
    """
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
    return:
        bool: if True means password change successfully, else notting changes.
    """
    while True:
        # Make sure it is the account owner who is changing the password
        current_password = input('Current Password(Press 0 to Student Account Management): ')

        if current_password == '0': # Go Back to Student Account Management Page
            return False
        elif current_password == student_info[1]["password"]:
            while True:
                new_password = input('New password(Press 0 to Student Account Management): ')
                if new_password == '0':
                    return False
                elif new_password == current_password:
                    print('New Password cannot be same as Current Password')
                else:
                    while True:
                        # To confirm the new password
                        confirm_password = input('Confirm Password(Press 0 to Back): ')
                        if confirm_password == '0': # Go back to new password
                            break
                        elif confirm_password == new_password:
                            student_info[1]["password"] = new_password # change the data of the student in their own dictionary
                            accounts = fetch_data("data/user_data.txt") # get all the account of the user in a list
                            accounts[student_info[0]] = student_info[1] # insert the updated student data dictionary to user list
                            insert_data("data/user_data.txt", accounts) # save it to the database
                            return True
                        else:
                            print('Wrong Password!')
        else:
            print('Wrong Password!')

def update_contact_detail(student_info):
    pass

def update_emergency_information(student_info):
    pass