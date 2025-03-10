# Student Account Management: Student can choose to manage or update, for the manage part student can
#                             change their password there. When update is chosen, they can update their
#                             contact details and emergency information. Data in data.txt
# Course Enrolment          : When selected, fetch data from txt file and display their timetable
# Course Material Access    : Fetch data from course_data.txt display course material with corresponding course
# Assignment Submission     : Insert student's assignment submission inside the course_data.txt with corresponding course
# Grades Tracking           : Fetch data from txt file, and display grade with corresponding course
# Feedback Submission       : Have a prompt that they can input to provide feedback on courses and overall
#                             academic experience. Data will insert to user.data.txt

from Student.Student_Account_Management import student_account_management
from Student.Course_Enrolment import time_table
from Student.Feedback_Submission import feedback_sub
from Student.Assignment_submission import assignment_sub_menu
from Student.grades_tracking import show_grade
from Student.course_material_access import course_material

def student_user_page(student_info):
    #Display student main menu
    while True:
        print("\n[ Student Menu ]")
        print('"1" - Student Account Management')
        print('"2" - Course Enrolment ')
        print('"3" - Course Material Access')
        print('"4" - Assignment Submission')
        print('"5" - Grades Tracking')
        print('"6" - Feedback Submission')
        print("'7' - Communication ")
        print('"8" - Exit')
        print('"0" - Logout')

        # Choose function to use
        choice = input("Enter your choice: ")

        if choice == '1': # Student Account Management
            student_account_management(student_info)

        elif choice == '2': # view time_table
            time_table(student_info)

        elif choice == '3': # View course material
            course_material(student_info)

        elif choice == '4': # student can submit assignment here
            assignment_sub_menu(student_info)

        elif choice == '5': # display their grades
            show_grade(student_info)

        elif choice == '6': # student can type their feedback here
            if feedback_sub(student_info): # if they have type in any feedback, it will show 'Feedback saved!'
                print('Feedback saved!')

        elif choice == '7':
            from Staff.Communication import communication_main
            communication_main()

        elif choice == '8':
            return 'exit'

        elif choice == '0':
            return 'logout'

        else:
            print("Invalid choice!")