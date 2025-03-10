# 1. System Administration: Manage user accounts and credentials for all system users (teachers, students, staff). (Done)
# 2. Student Management: Oversee student records, including viewing and updating personal details, enrollment status, and academic performance. 
# 3. Course Management: Create, update, or delete course offerings and assign instructors to courses. (Done)
# 4. Class Schedule: Maintain and update class schedules, ensuring no overlap and proper resource allocation. 
# 5. Report Generation: Generate academic performance, attendance, and financial reports for students and the institution.

def administrator_user_page():
    while True:
        print("\nAdministrator Menu")
        print("'1' - System Administration")
        print("'2' - Student Management")
        print("'3' - Course Management")
        print("'4' - Class Schedule")
        print("'5' - Report Generation")
        print("'6' - Exit")
        print("'0' - Logout")

        choice = input("Enter your choice: ")
        if choice == '1':
            from Administrator.system_administration import manage_account
            manage_account()
        elif choice == '2':
            # from Administrator.system_administration import manageStudent
            # manageStudent()
            pass
        elif choice == '3':
            from Administrator.course_management import manage_course
            manage_course()
        elif choice == '4':
            # manageClassSchedule()
            pass
        elif choice == '5':
            # manageReportGeneration()
            pass
        elif choice == '6':
<<<<<<< Updated upstream
=======
            from Staff.Communication import communication_main
            communication_main()
        elif choice == '7':
>>>>>>> Stashed changes
            return 'exit'
        elif choice == '0':
            return 'logout'
        else:
            print("Invalid choice!")