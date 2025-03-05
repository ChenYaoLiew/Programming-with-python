# Grade student
import os

def grade_assignment():
    from teacher_function import fetch_courses,display_course,select_course,display_student_ids,process_stud_id,get_valid_grade
    from function.query import insert_data

    courses = fetch_courses()
    if not courses:
        return

    # Display Course
    display_course()

    try:
        selected_course = select_course(courses, action="Grade Student's Assignment")

        if not selected_course:
            print("No course selected.")
            return

        display_student_ids(selected_course[1])

        student_id = input("\nEnter student ID to grade assignment: ").strip()

        process_stud_id(student_id)

        student_found = next((student for student in selected_course[1]["students_enrolled"] if student.get("student_id") == student_id), None)

        if not student_found:
            print("Student ID not found in this course.")
            return

        assignment_grade = get_valid_grade(student_id)

        student_found["assignment_grade"] = assignment_grade
        print(f"Assignment grade updated for {student_id}.")

        courses[selected_course[0]] = selected_course[1]

        file_path = os.path.join(os.path.dirname(__file__), "..", "data", "course_data.txt")
        insert_data(file_path, courses)
        print("Updated assignment grades saved successfully.")

    except ValueError:
        print("Invalid selection, please try again")
        grade_assignment()

def grade_exam():
    from teacher_function import fetch_courses, display_course, select_course, display_student_ids, process_stud_id, \
        get_valid_grade
    from function.query import insert_data

    courses = fetch_courses()
    if not courses:
        return

    display_course()

    try:
        selected_course = select_course(courses, action="Grade Student's Exam")

        if not selected_course:
            print("No course selected.")
            return

        display_student_ids(selected_course[1])

        student_id = input("\nEnter student ID to grade exam: ").strip()

        process_stud_id(student_id)

        student_found = next((student for student in selected_course[1]["students_enrolled"] if student.get("student_id") == student_id), None)

        if not student_found:
            print("Student ID not found in this course.")
            return

        exam_grade = get_valid_grade(student_id)

        student_found["exam_grade"] = exam_grade
        print(f"Exam grade updated for {student_id}.")

        courses[selected_course[0]] = selected_course[1]

        file_path = os.path.join(os.path.dirname(__file__), "..", "data", "course_data.txt")
        insert_data(file_path, courses)
        print("Updated exam grades saved successfully.")

    except ValueError:
        print("Invalid selection, please try again")
        grade_exam()

def give_feedback():
    from teacher_function import fetch_courses, display_course, select_course, display_student_ids, process_stud_id
    from function.query import insert_data

    courses = fetch_courses()
    if not courses:
        return

    display_course()

    try:
        selected_course = select_course(courses, action="Provide Student's Feedback")

        if not selected_course:
            print("No course selected.")
            return

        display_student_ids(selected_course[1])

        student_id = input("\nEnter student ID to provide student feedback: ").strip()

        process_stud_id(student_id)

        student_found = None
        for student in selected_course[1]["students_enrolled"]:
            if student.get("student_id") == student_id:
                student_found = student
                break

        if not student_found:
            print("Student ID not found in this course.")
            return

        feedback = input("\nEnter feedback: ").strip()
        student_found["feedback"] = feedback
        print(f"Feedback updated for {student_id}.")

        # Update the courses list with the modified course
        courses[selected_course[0]] = selected_course[1]

        file_path = os.path.join(os.path.dirname(__file__), "..", "data", "course_data.txt")
        insert_data(file_path, courses)
        print("Feedback saved successfully.")

    except ValueError:
        print("Invalid selection, please try again")
        give_feedback()

def manage_grading_assessment():
    while True:
        print("\nWelcome to Grading & Assessment Management\n1 - Grade Assignment\n2 - Grade Exam\n3 - Provide Feedback for student\n4 - Back")
        try:
            choice = input("\nEnter Choice: ").strip()
            if not choice:  # Prevent empty input
                print("Input cannot be empty. Please enter a number.")
                continue

            choice = int(choice)
            if choice == 1:
                grade_assignment()
            elif choice == 2:
                grade_exam()
            elif choice == 3:
                give_feedback()
            elif choice == 4:
                from menu import teacher_menu_page
                teacher_menu_page()
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")




