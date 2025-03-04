# Enrolling student
from function.query import *
import os
import json

def process_stud_id(student_id):
    if not validate_stud_id(student_id):
        return

def get_student_id(student_id):
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "student_data.txt")
    accounts = fetch_data(file_path)

    for data in accounts:
        if data["student_id"] == student_id:
            return data["student_id"]

    return None

def validate_stud_id(student_id):
    """Validates student ID format (should be 'STDxxxx')."""
    if not student_id.startswith("STD") or not student_id[3:].isdigit() or len(student_id) != 7:
        print("Invalid student ID format. Should be STD followed by 4 digits (e.g., STD0001)")
        return False
    return True

def insert_data_json(file_path, data_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        for data in data_list:
            file.write(json.dumps(data) + "\n")

def fetch_courses():
    """Reads course data from a JSON file and returns it as a list of dictionaries."""
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "course_data.txt")

    if not os.path.exists(file_path):
        return []  # Return an empty list if the file does not exist

    course = fetch_data(file_path)
    return course

def get_valid_selected_course(action="perform this action"):
    """Fetches a course, ensures 'students_enrolled' is a valid list, and returns both."""

    courses = fetch_courses()
    if not courses:
        print("No courses available.")
        return None, []

    display_course()
    selected_course = select_course(courses, action)

    if not selected_course:
        print(f"No course selected for {action}.")
        return None, []

    # Ensure 'students_enrolled' is always a list
    selected_course[1]["students_enrolled"] = selected_course[1].get("students_enrolled", [])

    students = selected_course[1]["students_enrolled"]

    if not students:
        print("No students enrolled in this course.")
        return selected_course, []  # Return an empty list instead of `None`

    return selected_course, students

def select_course(courses, action="view students"):
    """Prompts the user to select a course and returns the selected course or None if canceled."""
    while True:
        try:
            course1 = []
            course_choice = int(input(f"\nSelect a course to {action} (0 to go back to main menu): "))
            if course_choice == 0:
                manage_stu_enrol()  # Return to menu
                return None  # Indicate that no course was selected

            if 0 < course_choice <= len(courses):
                course1.append(course_choice - 1)
                course1.append(courses[course_choice - 1])
                return course1  # Return the selected course

            print("Invalid selection, please try again.")
            return select_course(courses, action)  # Recursive call for invalid input

        except ValueError:
            print("Invalid input. Please enter a number.")
            return select_course(courses, action)  # Recursive call for invalid input

def display_student_ids(course):
    """Displays student IDs for a given course."""

    students = course.get("students_enrolled", [])  # Always expect a list

    if not students:
        print(f"\nNo students enrolled in {course.get('course_title', 'this course')}.")
        return

    print(f"\nStudents enrolled in {course.get('course_title', 'this course')}:")
    for student in students:
        print(f"- {student.get('student_id', 'Unknown')}")  # Use `.get()` for safety

def display_course():
    #Displays available courses
    courses = fetch_courses()
    if not courses:  # If courses list is empty, return early
        return

    print("\nAvailable Courses:")
    for i, course in enumerate(courses, 1):
        print(f"{i} - {course['course_id']}: {course['course_title']}")


def view_enrolled_stu():
    selected_course, students = get_valid_selected_course("View Enrolled Students")

    if not selected_course[1] or not students:
        print("\nNo students enrolled in this course.")
        return

    # Display student IDs
    display_student_ids(selected_course[1])

def enrol_stud():
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "course_data.txt")
    courses = fetch_data(file_path)
    if not courses:
        return

    display_course()

    try:
        selected_course = select_course(courses, action="Enroll Students")

        if not selected_course:
            print("No course selected.")
            return

        # Get student detail
        student_id = input("Enter student ID (format STDxxxx): ").strip()

        # Validate student ID format
        process_stud_id(student_id)

        # Check student_id exits in system first only proceed
        student_name = get_student_id(student_id)
        if not student_name:
            print(f"Student with ID {student_id} not found in the system")
            return

        # Check if student is already enrolled
        students_exist = False
        for student in selected_course[1]["students_enrolled"]:
            if student.get("student_id") == student_id:
                students_exist = True
                break  # Stop looping once a match is found

        if students_exist:
            print(f"{student_id}) is already enrolled in this course")
            return

        # Create a new student entry with all required fields
        new_student = {
            "student_id": student_id,
            "assignment_grade": "Not graded",
            "assignment_submission": "",
            "exam_grade": "Not graded",
            "feedback": "No feedback yet"
            }

        # Enroll student
        # selected_course = [0 , {}]
        selected_course[1]["students_enrolled"].append(new_student)
        courses[selected_course[0]] = selected_course[1]
        print(f"Student {student_id} is now enrolled ")
        insert_data_json(file_path, courses)

    except ValueError:
        print("Invalid selection, please try again")
        enrol_stud()

def remove_enrolled_stu():
    courses = fetch_courses()
    if not courses:
        return

    display_course()

    try:
        selected_course = select_course(courses, action="Remove Enrolled Students")

        if not selected_course:
            print("No course selected.")
            return

        # Display enrolled students
        display_student_ids(selected_course[1])

        # Input student_id to delete
        student_id = input("Enter student ID: ").strip()

        # Validate student id format
        process_stud_id(student_id)

        # Check if student exists and remove
        student_found = False
        for student in selected_course[1]["students_enrolled"]:
            if student.get("student_id") == student_id:
                selected_course[1]["students_enrolled"].remove(student)
                student_found = True
                print(f"Student {student_id} has been removed.")
                break  # Stop searching after removal

        if not student_found:
            print("Student not found.")

        # Save the deletion back into course_data file
        file_path = os.path.join(os.path.dirname(__file__), "..", "data", "course_data.txt")
        insert_data_json(file_path, courses)

    except(ValueError,IndexError):
        print("Invalid selection, please try again")
        remove_enrolled_stu()

def manage_stu_enrol():
        while True:
            print("1 - View Enrolled Student\n2 - Enroll Student\n3 - Remove Student\n4 - Back")
            choice = input("Enter your choice: ")
            if choice == '1':
                view_enrolled_stu()
            elif choice == "2":
                enrol_stud()
            elif choice == "3":
                remove_enrolled_stu()
            elif choice == "4":
                from Administrator.course_management import manageCourse
                manageCourse()

