# Grading student
from Teacher.student_enrolment import display_student_ids, process_stud_id, \
    insert_data_json, display_course, select_course, fetch_courses
import os

from function.query import fetch_data

def get_valid_grade(student_id):
    """Prompts the user to enter a valid assignment grade (A-F) and returns it."""
    while True:
        grade = input(f"\nEnter assignment grade for {student_id} (Grade can only be A, B, C, D, E, or F): ").strip().upper()
        if grade in ["A", "B", "C", "D", "E", "F"]:
            return grade  #Return the valid grade
        print("Invalid grade! Please enter only A, B, C, D, E, or F.")


def grade_assignment():
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
        insert_data_json(file_path, courses)
        print("Updated assignment grades saved successfully.")

    except ValueError:
        print("Invalid selection, please try again")
        grade_assignment()

def grade_exam():
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
        insert_data_json(file_path, courses)
        print("Updated exam grades saved successfully.")

    except ValueError:
        print("Invalid selection, please try again")
        grade_exam()

def give_feedback():
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
        insert_data_json(file_path, courses)
        print("Feedback saved successfully.")

    except ValueError:
        print("Invalid selection, please try again")
        give_feedback()

def manage_grading_assessment():
    while True:
        print("1 - Grade Assignment\n2 - Grade Exam\n3 - Provide Feedback for student\n4 - Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            grade_assignment()
        elif choice == 2:
            grade_exam()
        elif choice == 3:
            give_feedback()



