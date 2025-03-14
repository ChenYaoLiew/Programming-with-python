#  Student Management: Oversee student records, including viewing and updating personal details, enrollment status, and academic performance. 
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from function.query import *

def view_all_student():
    """
    Display information for all students in the system.
    
    This function retrieves all user records from the data file and
    prints details for accounts with the "student" account type, including
    username, student ID, phone number, and country.
    
    Parameters:
        None
        
    Returns:
        None
    """
    student_data = fetch_data("data/user_data.txt")

    for student in student_data:
        if student["accountType"] == "student":
            print(f"Username: {student['username']}, Student ID: {student['student_id']}, Phone Number: {student['phone_num']}, Country: {student['country']}")

def view_student(student_id):
    """
    Display information for a specific student by ID.
    
    This function retrieves and displays the details of a student
    matching the provided student ID, including username, ID,
    phone number, and country.
    
    Parameters:
        student_id (str): The ID of the student to view
        
    Returns:
        None
    """
    student_data = fetch_data("data/user_data.txt")

    for student in student_data:
        if student["student_id"] == student_id:
            print(f"Username: {student['username']}, Student ID: {student['student_id']}, Phone Number: {student['phone_num']}, Country: {student['country']}")

def view_student_menu():
    """
    Display a menu for student viewing options.
    
    This function presents options for viewing all students,
    viewing a specific student by ID, or returning to the
    previous menu.
    
    Parameters:
        None
        
    Returns:
        None
    """
    while True:
        print("'1' - View All Student\n'2' - View Student\n'3' - Back")
        choice = input("Enter your choice: ")
        if choice == '1':
           view_all_student()
        elif choice == '2': 
            student_id = input("Enter student ID: ")
            view_student(student_id)
        elif choice == '3':
            from menu import administrator_user_page
            administrator_user_page()
        else:
            print("Invalid choice")

def remove_student(student_id):
    """
    Remove a student from the system by their student ID.
    
    This function removes a student account from the user data file
    based on the provided student ID.
    
    Parameters:
        student_id (str): The ID of the student to remove
        
    Returns:
        bool: True if student was found and removed, False otherwise
    """
    student_data = fetch_data("data/user_data.txt")
    found = False
    
    # Create a new list without the student to be deleted
    updated_students = []
    for student in student_data:
        if student["student_id"] == student_id:
            found = True
        else:
            updated_students.append(student)
    
    if found:
        # Save the updated list back to the file
        if insert_data("data/user_data.txt", updated_students):
            print(f"Student with ID {student_id} has been removed successfully.")
            return True
        else:
            print("Error removing student. Please try again.")
            return False
    else:
        print(f"Student with ID {student_id} not found!")
        return False

def update_student_details(student_id):
    """
    Update student details in the system.
    
    This function allows updating a student's phone number, country,
    or emergency information. It displays the current values before
    prompting for changes.
    
    Parameters:
        student_id (str): The ID of the student to update
        
    Returns:
        bool: True if student was found and updated, False otherwise
    """
    student_data = fetch_data("data/user_data.txt")
    found = False
    
    for student in student_data:
        if student["student_id"] == student_id:
            found = True
            print("\nCurrent Student Details:")
            print(f"Username: {student['username']}")
            print(f"Phone Number: {student.get('phone_num', 'Empty')}")
            print(f"Country: {student.get('country', 'Empty')}")
            print(f"Emergency Info: {student.get('emergency_info', 'Empty')}")
            
            print("\nWhat would you like to update?")
            print("1 - Update Phone Number")
            print("2 - Update Country")
            print("3 - Update Emergency Information")
            print("4 - Cancel")
            
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                new_phone = input("Enter new phone number: ").strip()
                student["phone_num"] = new_phone
                print("Phone number updated successfully!")
                
            elif choice == "2":
                new_country = input("Enter new country: ").strip()
                student["country"] = new_country
                print("Country updated successfully!")
                
            elif choice == "3":
                new_emergency = input("Enter new emergency information: ").strip()
                student["emergency_info"] = new_emergency
                print("Emergency information updated successfully!")
                
            elif choice == "4":
                print("Update cancelled.")
                return False
                
            else:
                print("Invalid choice!")
                return False
            
            # Save the updated data
            if insert_data("data/user_data.txt", student_data):
                print(f"Student {student_id} details updated successfully.")
                return True
            else:
                print("Error saving updates. Please try again.")
                return False
    
    if not found:
        print(f"Student with ID {student_id} not found!")
        return False

def view_enrollment_status(student_id):
    """
    View all courses a student is enrolled in.
    
    This function retrieves and displays a list of all courses the
    specified student is enrolled in, including course ID, title,
    and current grades.
    
    Parameters:
        student_id (str): The ID of the student to check
        
    Returns:
        None
    """
    # First verify the student exists
    student_data = fetch_data("data/user_data.txt")
    student_exists = False
    for student in student_data:
        if student["student_id"] == student_id:
            student_exists = True
            break
    
    if not student_exists:
        print(f"Student with ID {student_id} not found!")
        return

    # Get all courses and check enrollment
    courses_data = fetch_data("data/course_data.txt")
    enrolled_courses = []
    
    for course in courses_data:
        for student in course.get("students_enrolled", []):
            if student.get("student_id") == student_id:
                enrolled_courses.append({
                    "course_id": course["course_id"],
                    "course_title": course["course_title"],
                    "assignment_grade": student.get("assignment_grade", "Not graded"),
                    "exam_grade": student.get("exam_grade", "Not graded")
                })
    
    if enrolled_courses:
        print(f"\nStudent {student_id} is enrolled in the following courses:")
        for course in enrolled_courses:
            print(f"\nCourse ID: {course['course_id']}")
            print(f"Course Title: {course['course_title']}")
            print(f"Assignment Grade: {course['assignment_grade']}")
            print(f"Exam Grade: {course['exam_grade']}")
    else:
        print(f"\nStudent {student_id} is not enrolled in any courses.")

def view_academic_performance(student_id):
    """
    View academic performance for all courses a student is enrolled in.
    
    This function displays detailed academic information for a student
    across all enrolled courses, including assignment status, assignment
    grade, exam grade, and teacher feedback.
    
    Parameters:
        student_id (str): The ID of the student to check
        
    Returns:
        None
    """
    # First verify the student exists
    student_data = fetch_data("data/user_data.txt")
    student_exists = False
    student_name = ""
    
    for student in student_data:
        if student["student_id"] == student_id:
            student_exists = True
            student_name = student["username"]
            break
    
    if not student_exists:
        print(f"Student with ID {student_id} not found!")
        return

    # Get all courses and check enrollment
    courses_data = fetch_data("data/course_data.txt")
    enrolled_courses = []
    
    print(f"\nAcademic Performance for {student_name} ({student_id})")
    print("=" * 60)
    
    found_courses = False
    for course in courses_data:
        for student in course.get("students_enrolled", []):
            if student.get("student_id") == student_id:
                found_courses = True
                print(f"\nCourse: {course['course_title']} ({course['course_id']})")
                print("-" * 40)
                print(f"Assignment Status: {student.get('assignment_submission', 'Not submitted')}")
                print(f"Assignment Grade : {student.get('assignment_grade', 'Not graded')}")
                print(f"Exam Grade      : {student.get('exam_grade', 'Not graded')}")
                print(f"Feedback        : {student.get('feedback', 'No feedback provided')}")
    
    if not found_courses:
        print("\nStudent is not enrolled in any courses.")

def student_management_menu():
    """
    Display the main student management menu.
    
    This function presents options for viewing student information,
    enrolling students, removing students, updating details, viewing
    enrollment status, checking academic performance, or returning
    to the previous menu.
    
    Parameters:
        None
        
    Returns:
        None
    """
    while True:
        print("\n'1' - View Student\n'2' - Enroll Student\n'3' - Remove Student\n'4' - Update Personal Details\n'5' - View Enrollment Status\n'6' - View Academic Performance\n'7' - Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_student_menu()
        elif choice == '2':
            from Teacher.student_enrolment import enroll_student
            enroll_student()
        elif choice == '3':
            student_id = input("Enter student ID: ")
            remove_student(student_id)
        elif choice == '4':
            student_id = input("Enter student ID: ")
            update_student_details(student_id)
        elif choice == '5':
            student_id = input("Enter student ID: ")
            view_enrollment_status(student_id)
        elif choice == '6':
            student_id = input("Enter student ID: ")
            view_academic_performance(student_id)
        elif choice == '7':
            from Administrator.menu import administrator_user_page
            administrator_user_page()
        else:
            print("Invalid choice")