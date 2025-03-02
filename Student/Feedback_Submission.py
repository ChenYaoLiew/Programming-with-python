from function.query import *

def feedback_sub(student_info):
    while True:
        feedback = input('Type your feedback here(Press 0 to Back): ')
        if feedback == '0':
            return False
        else:
            try:
                student_info[1]['feedback'] = feedback
                accounts = fetch_data("data/user_data.txt")  # get all the account of the user in a list
                accounts[student_info[0]] = student_info[1]  # insert the updated student data dictionary to user list
                insert_data("data/user_data.txt", accounts)  # save it to the database
                return True
            except KeyError:
                student_info[1]['feedback'] = feedback
                accounts = fetch_data("data/user_data.txt")  # get all the account of the user in a list
                accounts[student_info[0]] = student_info[1]  # insert the updated student data dictionary to user list
                insert_data("data/user_data.txt", accounts)  # save it to the database
                return True