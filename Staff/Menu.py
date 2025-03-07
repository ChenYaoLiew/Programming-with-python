def staff_user_page():
    while True:
        print("\nStaff Menu")
        print("'1' - Student Record")
        print("'2' - Resource Management")
        print("'3' - Timetable Management")
        print("'4' - Event Management")
        print("'5' - Communication ")
        print("'6' - Exit")
        print("'7' - Logout")

        choice = input("Enter your choice: ")
        if choice == '1':
            from Staff.Student_Records import manage_student_records
            manage_student_records()
        elif choice == '2':
            from Staff.Resource_Allocation import manage_resource_allocation_main
            manage_resource_allocation_main()
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            from Staff.Communication import communication_main
            communication_main
        elif choice == '6':
            return 'exit'
        elif choice == '7':
            return 'logout'
        else:
            print("Invalid choice!")

staff_user_page()