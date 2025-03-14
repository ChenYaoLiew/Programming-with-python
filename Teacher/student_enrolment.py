def view_enrolled_stu():
    """
    Display all students enrolled in a selected course.
    
    This function retrieves and displays the list of students 
    enrolled in a course that the teacher selects.
    
    Parameters:
        None
        
    Returns:
        None
    """
    from Teacher.teacher_function import get_course_students_enrolled,display_students_in_course

    selected_course, students = get_course_students_enrolled("View Enrolled Students")

    if selected_course is None:
        return

    if not selected_course[1] or not students:
        return

    # Display student IDs
    display_students_in_course(selected_course[1])

def enroll_student():
    """
    Enroll a student into a selected course.
    
    This function allows teachers to add a student to a course's enrollment list.
    It validates the student ID, checks if the student exists in the system,
    and ensures they aren't already enrolled before adding them.
    
    Parameters:
        None
        
    Returns:
        None
    """
    from Teacher.teacher_function import fetch_courses,display_course,select_course,process_stud_id,get_student_id
    from function.query import insert_data

    courses = fetch_courses()
    if not courses:
        return

    display_course()

    try:
        selected_course = select_course(courses, action="Enroll Students")

        if not selected_course:
            print("No course selected.")
            return

        # Get student detail
        student_id = input("Enter student ID (format UIDxxxx): ").strip()

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
            print(f"{student_id} is already enrolled in this course")
            return

        # Create a new student entry with all required fields
        new_student = {
            "student_id": student_id,
            "assignment_grade": "Not graded",
            "assignment_submission": "Empty",
            "exam_grade": "Not graded",
            "feedback": "No feedback yet"
            }

        # Enroll student
        selected_course[1]["students_enrolled"].append(new_student)
        courses[selected_course[0]] = selected_course[1]
        print(f"Student {student_id} is now enrolled ")
        file_path = "data/course_data.txt"
        insert_data(file_path, courses)

    except ValueError:
        print("Invalid selection, please try again")
        enroll_student()

def remove_enrolled_student():
    """
    Remove a student from a selected course.
    
    This function allows teachers to remove a student from a course's enrollment list.
    It displays the list of enrolled students, validates the student ID to remove,
    and updates the course data file after removal.
    
    Parameters:
        None
        
    Returns:
        None
    """
    from Teacher.teacher_function import fetch_courses,display_course,select_course,display_students_in_course,process_stud_id
    from function.query import insert_data

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
        if not selected_course[1].get("students_enrolled"):  # Check if students exist
            print("\nNo students enrolled in this course.")
            return  # Exit early if no students

        display_students_in_course(selected_course[1])

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
        file_path = "data/course_data.txt"
        insert_data(file_path, courses)

    except(ValueError,IndexError):
        print("Invalid selection, please try again")
        remove_enrolled_student()

def manage_student_enroll():
    """
    Provide a menu interface for student enrollment management.
    
    This function displays options for viewing enrolled students,
    enrolling new students, removing students, or returning to
    the previous menu.
    
    Parameters:
        None
        
    Returns:
        None
    """
    while True:
        print("\nWelcome to Student Enrollment Management\n'1' - View Enrolled Student\n'2' - Enroll Student\n'3' - Remove Student\n'4' - Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            view_enrolled_stu()
        elif choice == '2':
            enroll_student()
        elif choice == '3':
            remove_enrolled_student()
        elif choice == '4':
            return
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")