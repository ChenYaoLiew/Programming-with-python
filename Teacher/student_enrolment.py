# Enrolling student
from function.query import *
import os
import ast

def getStudentName(student_id):
    accounts = fetch_data("..\data\student_data.txt")

    for data in accounts:
        if data["student_id"] == student_id:
            return data["username"]

def fetch_courses():
    # Create absolute file path
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "course_data.txt")
    courses = fetch_data(file_path) # Fetch data from file and returns the list
    if not courses:
        print("No courses found")
        return []
    return courses

def display_course():
    #Displays available courses
    courses = fetch_courses()
    if not courses:  # If courses list is empty, return early
        return

    print("\nAvailable Courses:")
    for i, course in enumerate(courses, 1):
        print(f"{i} - {course['course_id']}: {course['course_title']}")

def view_enrolled_stu():
    # Get course data
    courses = fetch_courses()
    if not courses:
        return

    # Display course
    display_course()
    try:
        # Get course choice
        course_choice = int(input("\nSelect a course to view student(0 to go back to main menu): "))
        if course_choice == 0:
            manage_stu_enrol() # Go back to manageCourse() menu
        if 0 < course_choice <= len(courses):
            selected_course = courses[course_choice - 1] # Get the selected course based on user input (adjust for 0-based index)
            students = selected_course.get("students_enrolled",{})

            if not students:
                print("No students enrolled in this course")
                return
            else:
                print(f"Students enrolled in this course: {students}")

    except IndexError:
        print("Invalid selection, please try again")
        view_enrolled_stu()
    except ValueError:
        print("Invalid selection, please try again")
        view_enrolled_stu()

def enrol_stud():
    courses = fetch_courses()
    if not courses:
        return

    display_course()

    course_choice = int(input("\nSelect a course to enroll(0 to go back to main menu): "))
    if course_choice == 0:
        manage_stu_enrol()
    if 0 < course_choice <= len(courses):
        selected_course = courses[course_choice - 1]

        # Get student detail ( Once nengzhe finishes his student part make sure to change this)
        # ( need to set some rules such as if there is no STD in front then return false and try again or if it's more than 5 numbers then try again)
        student_id = input("Enter student ID: ").strip()
        student_name = input("Enter the student name to enroll: ").strip()

        # File path for user_data.txt
        userdata_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "user_data.txt")
        # Check student_id and student_name exits first only proceed
        if student_id in  userdata_file_path:

            # Ensure students_enrolled is a dictionary
            if not isinstance(selected_course["students_enrolled"], dict):
                    # Convert into dictionary
                    selected_course["students_enrolled"] = ast.literal_eval(selected_course["students_enrolled"])

            # Check if student is already enrolled
            if student_id in selected_course["students_enrolled"]:
                print(f"{student_id}:{student_name} is already enrolled in this course")
                return

            # Enroll student
            elif student_id not in selected_course["students_enrolled"]:
                selected_course["students_enrolled"][student_id] = student_name
                print(f"{student_id}:{student_name} is now enrolled")

            file_path = os.path.join(os.path.dirname(__file__), "..", "data", "course_data.txt")
            insert_data(file_path, courses)

        else:
            print(f"{student_id} not found")

def remove_enrolled_stu():
    courses = fetch_courses()
    display_course()

    try:
        course_choice = int(input("\nSelect a course to remove: "))
        if course_choice == 0:
            manage_stu_enrol()
        elif 0 < course_choice <= len(courses):
            selected_course = courses[course_choice - 1]

            # Ensure 'students_enrolled' is a dictionary
            if isinstance(selected_course["students_enrolled"], str):
                selected_course["students_enrolled"] = ast.literal_eval(selected_course["students_enrolled"])

            # View Student to delete


            student_id = input("Enter student ID: ").strip()
            if student_id not in selected_course["students_enrolled"]:
                print("Student not found")
            if student_id in selected_course["students_enrolled"]:
                del selected_course["students_enrolled"][student_id]
                print("Student removed")

    except IndexError:
        print("Invalid selection, please try again")
        remove_enrolled_stu()
    except ValueError:
        print("Invalid selection, please try again")
        remove_enrolled_stu()

        # Define file path for saving
        file_path = os.path.join(os.path.dirname(__file__), "..", "data", "course_data.txt")

        # Save updated course data back to file
        try:
            with open(file_path, 'w') as file:
                for course in courses:
                    file.write(str(course) + "\n")  # Convert dictionary to string and write to file
            print("Course data updated successfully.")
        except Exception as e:
            print(f"Error saving file: {str(e)}")

def manage_stu_enrol():
        while True:
            print("1 - View Student Enrolled\n2 - Enroll Student\n3 - Remove Student\n4 - Back")
            choice = input("Enter your choice: ")
            if choice == "1":
                view_enrolled_stu()
            elif choice == "2":
                enrol_stud()
            elif choice == "3":
                remove_enrolled_stu()
            elif choice == "4":
                from Administrator.course_management import manageCourse
                manageCourse()

manage_stu_enrol()