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
    """
    Used when student want to update contact detail such as update phone number or country
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
    return:
        bool: if True means data edited successfully, else notting changes.
    """

    while True:
        print('"1" - Edit Phone Number')
        print('"2" - Edit Country')
        print('"3" - Back')
        choice = input('Enter your choice: ')
        if choice == '1':
            new_phone_num = input('Phone Number(Press 0 to Back): ')
            if new_phone_num == '0': # Go back to update contact detail page
                break
            else:
                # if data dictionary contain phone_num(Key) it will overwrite with new data
                try:
                    student_info[1]['phone_num'] = new_phone_num
                    accounts = fetch_data("data/user_data.txt")  # get all the account of the user in a list
                    accounts[student_info[0]] = student_info[1]  # insert the updated student data dictionary to user list
                    insert_data("data/user_data.txt", accounts)  # save it to the database
                    return True
                # if data dictionary not contain phone_num(Key) it will add a it inside dictionary
                except KeyError:
                    student_info[1]['phone_num'] = new_phone_num
                    accounts = fetch_data("data/user_data.txt")  # get all the account of the user in a list
                    accounts[student_info[0]] = student_info[1]  # insert the updated student data dictionary to user list
                    insert_data("data/user_data.txt", accounts)  # save it to the database
                    return True

        elif choice == '2':
            new_country = input('Country(Press 0 to Back): ')
            if new_country == '0':
                break
            else:
                try:
                    student_info[1]['country'] = new_country
                    accounts = fetch_data("data/user_data.txt")  # get all the account of the user in a list
                    accounts[student_info[0]] = student_info[1]  # insert the updated student data dictionary to user list
                    insert_data("data/user_data.txt", accounts)  # save it to the database
                    return True
                except KeyError:
                    student_info[1]['country'] = new_country
                    accounts = fetch_data("data/user_data.txt")  # get all the account of the user in a list
                    accounts[student_info[0]] = student_info[1]  # insert the updated student data dictionary to user list
                    insert_data("data/user_data.txt", accounts)  # save it to the database
                    return True

        elif choice == '3':
            return False
        else:
            print('Invalid choice!')

def update_emergency_information(student_info):
    """
    Used when student want to update emergency information
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
    return:
        bool: if True means data edited successfully, else notting changes.
    """
    emergency_info = input('Emergency Information(Press 0 to Back): ')
    if emergency_info == '0':
        return False
    else:
        try:
            student_info[1]['emergency_info'] = emergency_info
            accounts = fetch_data("data/user_data.txt")  # get all the account of the user in a list
            accounts[student_info[0]] = student_info[1]  # insert the updated student data dictionary to user list
            insert_data("data/user_data.txt", accounts)  # save it to the database
            return True
        except KeyError:
            student_info[1]['emergency_info'] = emergency_info
            accounts = fetch_data("data/user_data.txt")  # get all the account of the user in a list
            accounts[student_info[0]] = student_info[1]  # insert the updated student data dictionary to user list
            insert_data("data/user_data.txt", accounts)  # save it to the database
            return True