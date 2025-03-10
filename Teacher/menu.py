# Teacher Menu Page
# Course Creation & Management : Create and update courses, including lesson plans, assignments, and schedules.
# Student Enrolment: Enrol and remove students from the courses they are teaching.
# Grading and Assessment: Grade assignments, exams, and provide detailed feedback to students.
# Attendance Tracking: Record and monitor student attendance during classes.
# Report Generation: Generate reports on student performance and participation for administrative review.

def teacher_menu_page():
    while True:
<<<<<<< Updated upstream
        print("\nTeacher's Menu\n1 - Course Creation & Management\n2 - Student Enrolment & Management  \n3 - Grading & Assessment\n4 - Class Enrolment and Attendance Management\n5 - Report Generation\n6 - Logout")
        try:
            choice = input("\nEnter Choice: ").strip()
            if not choice:  # Prevent empty input
                print("Input cannot be empty. Please enter a number.")
                continue
=======
        print("\nTeacher's Menu\n1 - Course Creation & Management\n2 - Student Enrolment & Management  \n3 - Grading & Assessment\n4 - Class Enrolment and Attendance Management\n5 - Report Generation\n6 - Exit\n7 - Logout")
>>>>>>> Stashed changes

        choice = input("\nEnter Choice: ").strip()


        if choice == '1':
            from course_management_teach import manage_course_teach
            manage_course_teach()
        elif choice == '2':
            from student_enrolment import manage_stu_enrol
            manage_stu_enrol()
        elif choice == '3':
            from grading_assessment import manage_grading_assessment
            manage_grading_assessment()
        elif choice == '4':
            from class_attendance_management import manage_attendance
            manage_attendance()
        elif choice == '5':
            from report_generation import generate_student_report
            generate_student_report()
        elif choice == '6':
            return 'exit'
        elif choice == '7':
            return 'logout'
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

<<<<<<< Updated upstream
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
                from class_attendance_management import manage_attendance
                manage_attendance()
            elif choice == 5:
                from report_generation import generate_student_report
                generate_student_report()
            elif choice == 6:
                continue
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
=======
>>>>>>> Stashed changes

