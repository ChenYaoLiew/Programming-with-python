# Student Account Management: Student can choose to manage or update, for the manage part student can
#                             change their password there. When update is chosen, they can update their
#                             contact details and emergency information
# Course Enrolment : When selected, fetch data from txt file and display their timetable
# Course Material Access: To be found a way to do
# Assignment Submission: insert student's assignment submission inside the course_data.txt
# Grades Tracking: Fetch data from txt file, and display in a row
# Feedback Submission: Have a prompt that they can input to provide feedback on courses, instructor and overall
#                      academic experience.

from Student.Student_Account_Management import *
from Student.Course_Enrolment import time_table
from Student.Feedback_Submission import feedback_sub
from Student.Assignment_submission import *
from Student.grades_tracking import show_grade

def student_user_page(student_info):
    #Display student main menu
    while True:
        print("\nStudent Menu")
        print('"1" - Student Account Management')
        print('"2" - Course Enrolment ')
        print('"3" - Course Material Access')
        print('"4" - Assignment Submission')
        print('"5" - Grades Tracking')
        print('"6" - Feedback Submission')
        print('"7" - Exit')
        print('"0" - Logout')

        choice = input("Enter your choice: ")

        if choice == '1': # Student Account Management
            # Display student account management page
            while True:
                print('\nStudent Account Management')
                print(f'Student Name         : {student_info[1]['username']}')
                print(f'Student ID           : {student_info[1]['student_id']}')
                print(f'Student Fund         : {student_info[1]['fund']}')
                print(f'Student Phone Number : {student_info[1]['phone_num']}')
                print(f'Student country      : {student_info[1]['country']}')
                print(f'Emergency information: {student_info[1]['emergency_info']}')
                print('"1" - Change password')
                print('"2" - Update contact detail')
                print('"3" - Update emergency information')
                print('"4" - Back' )

                choice = input("Enter your choice: ")

                if choice == '1': # change password
                    if change_password(student_info):
                        print('Password changed!')

                elif choice == '2': # update contact detail
                    if update_contact_detail(student_info):
                        print('Successfully changed!')

                elif choice == '3': # update emergency info
                    if update_emergency_information(student_info):
                        print('Information saved!')

                elif choice == '4': # back to main page
                    break

                else:
                    print("Invalid choice!")

        elif choice == '2': # view time_table
            if not time_table(student_info): # If got class it will display, else show no class enrolled
                print('\nNo classes enrolled! ')

        elif choice == '3': # wait for manfred
            pass

        elif choice == '4': # student can submit assignment here
                if assignment_sub(student_info): # if they do any changes, it will show 'Assignment Submitted!'
                    print('Assignment Submitted!')

        elif choice == '5': # display their grades
            show_grade(student_info)

        elif choice == '6': # student can type their feedback here
            if feedback_sub(student_info): # if they have type in any feedback, it will show 'Feedback saved!'
                print('Feedback saved!')

        elif choice == '7':
            return 'exit'

        elif choice == '0':
            return 'logout'

        else:
            print("Invalid choice!")