# Student Account Management: Student can choose to manage or update, for the manage part student can
#                             change their password there. When update is chosen, they can update their
#                             contact details and emergency information
# Course Enrolment: When selected, fetch data from txt file and display their timetable
# Course Material Access: To be found a way to do
# Grades Tracking: Fetch data from txt file, and display in a row
# Feedback Submission: Have a prompt that they can input to provide feedback on courses, instructor and overall
#                      academic experience.

from Student.Student_Account_Management import *

def student_user_page(student_info):
    while True:
        print("Student Menu")
        print('"1" - Student Account Management')
        print('"2" - Course Enrolment')
        print('"3" - Course Material Access')
        print('"4" - Grades Tracking')
        print('"5" - Feedback Submission')
        print('"6" - Exit')
        print('"0" - Logout')

        choice = input("Enter your choice: ")
        if choice == '1':
            while True:
                print('\nStudent Account Management')
                print(f'Student Name: {student_info[1]['username']}')
                print(f'Student ID: {student_info[1]['student_id']}')
                print(f'Student Fund: {student_info[1]['fund']}')
                print('"1" - Change password')
                print('"2" - Update contact detail')
                print('"3" - Update emergency information')
                print('"4" - Back' )

                choice = input("Enter your choice: ")
                if choice == '1':
                    if change_password(student_info):
                        print('Password changed!')
                elif choice == '2':
                    pass
                elif choice == '3':
                    pass
                elif choice == '4':
                    break
                else:
                    print("Invalid choice!")
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            return 'exit'
        elif choice == '0':
            return 'logout'
        else:
            print("Invalid choice!")