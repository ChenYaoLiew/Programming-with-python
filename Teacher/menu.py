# Teacher Menu Page

def teacher_menu_page():
    while True:
        print("\nTeacher's Menu\n1 - Course Creation & Management\n2 - Student Enrolment Management  \n3 - Grading & Assessment\n4 - Attendance Tracking\n5 - Report Generation\n6 - Back")
        try:
            choice = input("\nEnter Choice: ").strip()
            if not choice:  # Prevent empty input
                print("Input cannot be empty. Please enter a number.")
                continue

            choice = int(choice)

            if choice == 1:
                from course_management_teach import manage_course_teach
                manage_course_teach()
            elif choice == 2:
                from student_enrolment import manage_stu_enrol
                manage_stu_enrol()
            elif choice == 3:
                from grading_assessment import manage_grading_assessment
                manage_grading_assessment()
            elif choice == 4:
                from attendance_tracking import manage_attendance
                manage_attendance()
            elif choice == 5:
                continue
            elif choice == 6:
                continue
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

teacher_menu_page()
