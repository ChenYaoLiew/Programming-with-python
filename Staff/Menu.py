import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def staff_user_page():
    while True:
        print("\nStaff Menu")
        print("'1' - Student Record")
        print("'2' - Resource Management")
        print("'3' - View Course Timetable")
        print("'4' - Event Management")
        print("'5' - Communication ")
        print("'6' - Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            from Staff.Student_Records import manage_student_records
            manage_student_records()
        elif choice == '2':
            from Staff.Resource_Allocation import manage_resource_allocation_main
            manage_resource_allocation_main()
        elif choice == '3':
            from Administrator.course_management import view_course_timetable
            view_course_timetable()
        elif choice == '4':
            from Staff.Event_Management import event_management_main
            event_management_main()
        elif choice == '5':
            from Staff.Communication import communication_main
            communication_main()
        elif choice == '6':
            quit()
        else:
            print("Invalid choice!")