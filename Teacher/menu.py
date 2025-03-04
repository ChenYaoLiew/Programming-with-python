from Administrator.course_management import manageCourse
from Teacher.grading_assessment import manage_grading_assessment
from Teacher.student_enrolment import manage_stu_enrol

def teacher_menu_page():
    while True:
        print("1 - Course Creation & Management\n2 - Student Enrolment Management  \n3 - Grading & Assessment\n4 - Attendance Tracking\n5 - Report Generation\n 6 - Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            manageCourse()
        elif choice == 2:
            manage_stu_enrol()
        elif choice == 3:
            manage_grading_assessment()
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
