def staff_user_page():
    while True:
        print("\nStaff Menu")
        print("'1' - Student Record")
        print("'2' - Resource Management")
        print("'3' - Timetable Management")
        print("'4' - Exit")
        print("'5' - Logout")

        choice = input("Enter your choice: ")
        if choice == '1':
            from Staff.Student_Records import manage_student_records
            manage_student_records()
        elif choice == '2':
            from Staff.Resource_Allocation import manage_resource_allocation
            manage_resource_allocation()
        elif choice == '3':
            pass
        elif choice == '4':
            return 'exit'
        elif choice == '5':
            return 'logout'
        else:
            print("Invalid choice!")

staff_user_page()