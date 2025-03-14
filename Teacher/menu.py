def teacher_menu_page():

    while True:
        print("\nTeacher's Menu\n'1' - Course Creation & Management\n'2' - Student Enrolment & Management  \n'3' - Grading & Assessment\n'4' - Class & Attendance Management\n'5' - Report Generation\n'6' - Exit\n'7' - Logout")

        choice = input("\nEnter Choice: ").strip()

        if choice == '1':
            from Teacher.course_management_teach import manage_course_teach
            manage_course_teach()
        elif choice == '2':
            from Teacher.student_enrolment import manage_student_enroll
            manage_student_enroll()
        elif choice == '3':
            from Teacher.grading_assessment import manage_grading_assessment
            manage_grading_assessment()
        elif choice == '4':
            from Teacher.class_attendance_management import manage_attendance
            manage_attendance()
        elif choice == '5':
            from Teacher.report_generation import generate_student_report
            generate_student_report()
        elif choice == '6':
            return 'exit'
        elif choice == '7':
            return 'logout'
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")