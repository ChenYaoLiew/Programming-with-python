def administrator_user_page():
    while True:
        print("\nAdministrator Menu")
        print("'1' - System Administration")
        print("'2' - Student Management")
        print("'3' - Course Management")
        print("'4' - Class Schedule")
        print("'5' - Report Generation")
        print("'6' - Communication ")
        print("'7' - Exit")
        print("'0' - Logout")

        choice = input("Enter your choice: ")
        if choice == '1':
            from Administrator.system_administration import manage_account
            manage_account()
        elif choice == '2':
            from Administrator.student_management import student_management_menu
            student_management_menu()
        elif choice == '3':
            from Administrator.course_management import manage_course
            manage_course()
        elif choice == '4':
            from Administrator.class_schedule import class_schedule_menu
            class_schedule_menu()
        elif choice == '5':
            from Administrator.report_generation import generate_reports
            generate_reports()
        elif choice == '6':
            from Staff.Communication import communication_main
            communication_main()
        elif choice == '7':
            return 'exit'
        elif choice == '0':
            return 'logout'
        else:
            print("Invalid choice!")