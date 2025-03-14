def grade_assignment():
    """
    Allow teachers to grade student assignments for a selected course.
    
    This function guides teachers through the process of selecting a course,
    choosing a student, and assigning a grade for their submitted assignment.
    The function verifies that the student exists in the course and has 
    submitted an assignment before allowing grading. Updated grades are saved
    to the course data file.
    
    Parameters:
        None
        
    Returns:
        None
    """
    from Teacher.teacher_function import fetch_courses,display_course,select_course,display_students_in_course,process_stud_id,get_valid_grade
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

        if not selected_course[1]["students_enrolled"]:
            print("\nNo students enrolled in this course.")
            return  # Exit the function early

        display_students_in_course(selected_course[1])

        student_id = input("\nEnter student ID to grade assignment: ").strip()

        process_stud_id(student_id)

        student_found = next((student for student in selected_course[1]["students_enrolled"] if student.get("student_id") == student_id), None)

        if student_found is None:
            print("Student ID not found in this course.")
            return

        # Check if assignment has been submitted
        if student_found.get("assignment_submission", "Empty") == "Empty":
            print("Cannot grade assignment. The student has not submitted the assignment yet.")
            return

        # Get assignment grade
        assignment_grade = get_valid_grade(student_id)

        # Update assignment grade
        student_found["assignment_grade"] = assignment_grade
        print(f"Assignment grade updated for {student_id}.")

        # Save the updated data
        courses[selected_course[0]] = selected_course[1]
        file_path = "data/course_data.txt"
        insert_data(file_path, courses)
        print("Updated assignment grades saved successfully.")

    except ValueError:
        print("Invalid selection, please try again.")
        grade_assignment()

def grade_exam():
    """
    Allow teachers to grade student exams for a selected course.
    
    This function guides teachers through the process of selecting a course,
    choosing a student, and assigning an exam grade. The function verifies 
    that the student exists in the course before allowing grading. Updated 
    exam grades are saved to the course data file.
    
    Parameters:
        None
        
    Returns:
        None
    """
    from Teacher.teacher_function import fetch_courses, display_course, select_course, display_students_in_course, process_stud_id, \
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

        display_students_in_course(selected_course[1])

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

        file_path = "data/course_data.txt"
        insert_data(file_path, courses)
        print("Updated exam grades saved successfully.")

    except ValueError:
        print("Invalid selection, please try again")
        grade_exam()

def give_feedback():
    """
    Allow teachers to provide written feedback to students in a selected course.
    
    This function guides teachers through the process of selecting a course,
    choosing a student, and entering written feedback. The function verifies 
    that the student exists in the course before allowing feedback entry.
    Updated feedback is saved to the course data file.
    
    Parameters:
        None
        
    Returns:
        None
    """
    from Teacher.teacher_function import fetch_courses, display_course, select_course, display_students_in_course, process_stud_id
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

        display_students_in_course(selected_course[1])

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

        file_path = "data/course_data.txt"
        insert_data(file_path, courses)
        print("Feedback saved successfully.")

    except ValueError:
        print("Invalid selection, please try again")
        give_feedback()

def manage_grading_assessment():
    """
    Present a menu interface for teachers to access grading and assessment functions.
    
    This function displays a menu with options for grading assignments, grading exams,
    providing student feedback, or returning to the previous menu. It loops until the
    user chooses to go back.
    
    Parameters:
        None
        
    Returns:
        None
    """
    while True:
        print("\nWelcome to Grading & Assessment Management\n'1' - Grade Assignment\n'2' - Grade Exam\n'3' - Provide Feedback for student\n'4' - Back")

        choice = input("\nEnter Choice: ").strip()

        if choice == '1':
            grade_assignment()
        elif choice == '2':
            grade_exam()
        elif choice == '3':
            give_feedback()
        elif choice == '4':
            return
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")