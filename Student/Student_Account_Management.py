from Student.Student_function import update_student_data

def change_password(student_info):
    """
    Used when student want to change their password

    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
    return:
        bool: if True means password change successfully, else notting changes.
    """
    student_data = student_info[1]
    index_in_list = student_info[0]

    while True:
        # Make sure it is the account owner who is changing the password
        current_password = input('Current Password(Press 0 to Student Account Management): ')

        if current_password == '0': # Go Back to Student Account Management Page
            return False

        elif current_password == student_data["password"]:
            while True:
                # Get new password from user
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
                            student_data["password"] = new_password # change the data of the student in their own dictionary
                            update_student_data(index_in_list, student_data) #Update new data
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
    student_data = student_info[1]
    index_in_list = student_info[0]

    while True:
        print('\n[ Contact detail settings ]')
        print('"1" - Edit Phone Number')
        print('"2" - Edit Country')
        print('"3" - Back')

        choice = input('Enter your choice: ')

        if choice == '1':
            new_phone = input('Phone Number(Press 0 to Back): ')
            if new_phone == '0': # Go back to update contact detail page
                break
            else:
                student_data['phone_num'] = new_phone
                update_student_data(index_in_list, student_data)
                return True

        elif choice == '2':
            new_country = input('Country(Press 0 to Back): ')

            if new_country == '0':
                break

            else:
                student_data['country'] = new_country
                update_student_data(index_in_list, student_data)
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
    student_data = student_info[1]
    index_in_list = student_info[0]

    emergency_info = input('Emergency Information(Press 0 to Back): ')

    if emergency_info == '0':
        return False

    else:
        student_data['emergency_info'] = emergency_info
        update_student_data(index_in_list, student_data)
        return True

def student_account_management(student_info):
    """
    To display Student Account Management menu
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
    return:
        None
    """
    # Display student info
    while True:
        print('\n [ Student Account Management ] ')
        print(f'Student Name         : {student_info[1]['username']}')
        print(f'Student ID           : {student_info[1]['student_id']}')
        print(f'Student Fund         : {student_info[1]['fund']}')
        print(f'Student Phone Number : {student_info[1]['phone_num']}')
        print(f'Student country      : {student_info[1]['country']}')
        print(f'Emergency information: {student_info[1]['emergency_info']}')
        print('\n"1" - Change password')
        print('"2" - Update contact detail')
        print('"3" - Update emergency information')
        print('"4" - Back')

        choice = input("Enter your choice: ")

        if choice == '1':  # change password
            if change_password(student_info):
                print('Password changed!')

        elif choice == '2':  # update contact detail
            if update_contact_detail(student_info):
                print('Successfully changed!')

        elif choice == '3':  # update emergency info
            if update_emergency_information(student_info):
                print('Information saved!')

        elif choice == '4':  # back to main page
            break

        else:
            print("Invalid choice!")