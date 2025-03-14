# Helper functions for student enrollment, course selection, grading, and attendance tracking.

# For Student Enrolment
def process_stud_id(student_id):
    """
    Process the provided student ID by validating its format.
    
    This function checks whether the given student ID adheres to the expected format
    using the 'validate_stud_id' function. If the student ID is invalid, the function
    returns immediately.
    
    Parameters:
        student_id (str): The student ID to be processed.
        
    Returns:
        None
    """
    if not validate_stud_id(student_id):
        return

def get_student_id(student_id):
    """
    Retrieve the student ID from the student data file if it exists.
    
    This function reads student data from the 'user_data.txt' file and
    iterates through the records to find a matching student ID.
    
    Parameters:
        student_id (str): The student ID to search for.
        
    Returns:
        str or None: The matching student ID if found; otherwise, None.
    """
    from function.query import fetch_data
    file_path = "data/user_data.txt"
    accounts = fetch_data(file_path)

    for data in accounts:
        if data["student_id"] == student_id:
            return data["student_id"]

    return None

def validate_stud_id(student_id):
    """
    Validate student ID format.
    
    This function checks if the student ID follows the required format (UID followed
    by 4 digits, e.g., UID0001).
    
    Parameters:
        student_id (str): The student ID to validate.
        
    Returns:
        bool: True if the ID format is valid, False otherwise.
    """
    if not student_id.startswith("UID") or not student_id[3:].isdigit() or len(student_id) != 7:
        print("Invalid student ID format. Should be STD followed by 4 digits (e.g., UID0001)")
        return False
    return True

def fetch_courses():
    """
    Read course data from a text file and return as a list of dictionaries.
    
    This function retrieves course information from the course_data.txt file.
    If the file doesn't exist, an empty list is returned.
    
    Parameters:
        None
        
    Returns:
        list: A list of course dictionaries or an empty list if no data is found.
    """
    import os
    file_path = "data/course_data.txt"

    if not os.path.exists(file_path):
        return []  # Return an empty list if the file does not exist

    from function.query import fetch_data
    course = fetch_data(file_path)
    return course

def get_course_students_enrolled(action="perform this action"):
    """
    Fetch a course and its enrolled students.
    
    This function retrieves a course selected by the user and ensures the
    'students_enrolled' field is a valid list.
    
    Parameters:
        action (str): Description of the action being performed.
        
    Returns:
        tuple: (selected_course, students_list) or (None, []) if no course or students.
    """

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

def select_course(courses, action="view students", return_to_menu=None):
    """
    Prompt the user to select a course from a list.
    
    This function displays a numbered list of courses and allows the user
    to select one by number.
    
    Parameters:
        courses (list): List of course dictionaries to select from.
        action (str): Description of the action being performed.
        return_to_menu (function): Optional callback function to return to menu.
        
    Returns:
        list or None: [course_index, course_data] or None if selection is canceled.
    """
    while True:
        try:
            course1 = []
            course_choice = int(input(f"\nSelect a course to {action} (0 to go back to menu page): "))
            if course_choice == 0:
                if return_to_menu:
                    return_to_menu()
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

def display_students_in_course(course):
    """
    Display all students enrolled in a specified course.
    
    This function prints a list of student IDs for the students enrolled
    in the given course.
    
    Parameters:
        course (dict): Course dictionary containing student enrollment data.
        
    Returns:
        None
    """

    students = course.get("students_enrolled", [])  # Always expect a list

    if not students:
        print(f"\nNo students enrolled in {course.get('course_title', 'this course')}.")
        return

    print(f"\nStudents enrolled in {course.get('course_title', 'this course')}:")
    for student in students:
        print(f"- {student.get('student_id', 'Unknown')}")  # Use `.get()` for safety

def display_course():
    """
    Display available courses fetched from the data source.
    
    This function retrieves and prints a numbered list of courses showing 
    each course's ID and title.
    
    Parameters:
        None
        
    Returns:
        None
    """
    courses = fetch_courses()
    if not courses:  # If courses list is empty, return early
        return

    print("\nAvailable Courses:")
    for i, course in enumerate(courses, 1):
        print(f"{i} - {course['course_id']}: {course['course_title']}")


# For Grading_assessment
def get_valid_grade(student_id):
    """
    Prompt for and validate a student grade input.
    
    This function repeatedly asks for a grade until a valid grade (A-F)
    is entered.
    
    Parameters:
        student_id (str): ID of the student being graded.
        
    Returns:
        str: The valid grade (A, B, C, D, E, or F).
    """
    while True:
        grade = input(f"\nEnter assignment grade for {student_id} (Grade can only be A, B, C, D, E, or F): ").strip().upper()
        if grade in ["A", "B", "C", "D", "E", "F"]:
            return grade  #Return the valid grade
        print("Invalid grade! Please enter only A, B, C, D, E, or F.")


# For attendance_tracking and managing class
def select_class(selected_course, action="Select"):
    """
    Display available classes in a course and allow user to select one.
    
    This function shows a list of classes for the selected course and
    prompts the user to enter a class ID.
    
    Parameters:
        selected_course (tuple): A tuple containing the course index and course data.
        action (str): Description of the action being performed.
        
    Returns:
        dict or None: The selected class dictionary or None if not found.
    """
    # Get the course timetable
    timetable = selected_course[1].get("course_timetable", [])

    if not timetable:
        print("No classes available for this course.")
        return None

    # Filter valid classes (must be a dict and contain "class_id")
    valid_classes = [cls for cls in timetable if isinstance(cls, dict) and "class_id" in cls]

    if not valid_classes:  # If there are no valid classes, return immediately
        print("No valid classes available for this course. Returning...")
        return None  # Exit function

    # Display available classes
    print(f"\nAvailable Classes for {action}:")
    for class_info in timetable:
        print(f"- {class_info.get('class_id', 'class_id not found')}")

    while True:
        # Get class ID from the user
        class_id = input("\nEnter Class ID: ").strip()

        if not class_id:
            print("Class ID cannot be empty. Please enter a valid ID.")
            continue  # Ask for input again

        # Find the selected class (ignoring case differences)
        class_match = next((cls for cls in timetable if cls["class_id"].lower() == class_id.lower()), None)

        if class_match:
            return class_match  # Return the matched class

        print(f"Class ID '{class_id}' not found. Please try again.")

def validate_class_id(class_id):
    """
    Validate class ID format.
    
    This function checks if the class ID follows the required format (CLS followed
    by 4 digits, e.g., CLS0001).
    
    Parameters:
        class_id (str): The class ID to validate.
        
    Returns:
        bool: True if the ID format is valid, False otherwise.
    """
    if not class_id.startswith("CLS") or not class_id[3:].isdigit() or len(class_id) != 7:
        print("Invalid class ID format. Should be CLS followed by 4 digits (e.g., UID0001)")
        return False
    return True

def display_students_in_class(class_match):
    """
    Display all students enrolled in a specific class.
    
    This function prints a list of student IDs for students enrolled
    in the given class.
    
    Parameters:
        class_match (dict): Class dictionary containing attendance data.
        
    Returns:
        None
    """

    students = class_match.get("attendance_list", [])  # List of students in the class

    if not students:
        print(f"\nNo students enrolled in class {class_match.get('class_id', 'Unknown')}.")
        return

    print(f"\nStudents enrolled in class {class_match.get('class_id', 'Unknown')}:")
    for student in students:
        print(f"- {student.get('student_id', 'Unknown')}")