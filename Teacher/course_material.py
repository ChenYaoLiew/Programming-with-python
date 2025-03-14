def add_course_material():
    """
    Allow teachers to add or update course materials for an existing course.
    
    This function guides teachers through the process of selecting a course
    and adding/updating lecture notes, assignment guidelines, and announcements.
    All course material updates are saved to the course data file.
    
    Parameters:
        None
        
    Returns:
        None
        
    Note:
        - If no courses exist, the function returns early
        - In case of an invalid course selection, the function recursively calls itself
        - Course materials are stored as links (for lecture notes and assignment guidelines)
    """
    from Teacher.teacher_function import fetch_courses,display_course,select_course
    from function.query import insert_data

    courses = fetch_courses()
    if not courses:
        return

    # Display courses
    display_course()

    try:
        selected_course = select_course(courses, action="Add course material")

        if not selected_course:
            print("No course selected.")
            return

        # Get material inputs
        lecture_note = input("Enter lecture note link (e.g: Google doc link): ").strip()
        assignment_guideline = input("Enter assignment guideline's link (e.g: Google doc link): ").strip()
        announcement = input("Enter announcements: ").strip()

        # Update course material
        selected_course[1]["course_material"]["lecture_note"] = lecture_note
        selected_course[1]["course_material"]["assignment_guideline"] = assignment_guideline
        selected_course[1]["course_material"]["announcement"] = announcement

        courses[selected_course[0]] = selected_course[1]

        file_path = "data/course_data.txt"
        insert_data(file_path,courses)
        print("Successfully added course material.")

    except ValueError:
        print("Invalid selection, please try again.")
        add_course_material()