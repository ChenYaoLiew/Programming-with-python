from Administrator.menu import administrator_user_page
from function.query import *

# Add enroll student
# Course timetable assign student
# Course Management: Create, update, or delete course offerings and assign instructors to courses.
# {
#     "course_id" = XXXX,
#     "course_title" = "XXXX",
#     "lesson_plan" = "XXXXXXX",
#     "students_enrolled" = [
#         {"student_id": "STD0001", "assignment_grade": "A", "assignment_submission": "","exam_grade": "B", "feedback": "Good"},
#         {"student_id": "STD0002", "assignment_grade": "A", "assignment_submission": "", "exam_grade": "B", "feedback": "Good"},
#     ],
#     "course_assignment" = "Google doc link",
#     "course_timetable"= [
#         {"class_id": "CLS0001", "time_start": "9:00 AM", "time_end": "12:00PM", "course_teacher": "TP_ID", "attendance_list": [] },
#         {"class_id": "CLS0002", "time_start": "9:00 AM", "time_end": "12:00PM", "course_teacher": "TP_ID", "attendance_list": [] },
#         {"class_id": "CLS0003", "time_start": "9:00 AM", "time_end": "12:00PM", "course_teacher": "TP_ID", "attendance_list": [] },
#         {"class_id": "CLS0004", "time_start": "9:00 AM", "time_end": "12:00PM", "course_teacher": "TP_ID", "attendance_list": [] },
#     ],
# }

def get_courses():
    """
    Retrieve all course records from the course data file.
    
    This function fetches all course data stored in the course_data.txt file
    using the fetch_data utility function.
    
    Parameters:
        None
        
    Returns:
        list: A list of dictionaries containing course records
    """
    data = fetch_data("data/course_data.txt")

    return data

def display_course(all_course):
    """
    Display a list of all available courses.
    
    This function prints course IDs and titles for all courses in the provided list.
    If no courses are available, it displays "None".
    
    Parameters:
        all_course (list): List of course dictionaries to display
        
    Returns:
        None
    """
    # Display all the course ID and course title if got any course
    print('\n[ Available Courses ]')
    if all_course:
        for course in all_course:
            print(f'- {course['course_id']} {course['course_title']}')
    else:
        print('None')

def generate_course_id(existing_ids):
    """
    Generate a new course ID in format CRSXXXX
    
    Parameters:
        existing_ids (list): List of existing course IDs
        
    Returns:
        str: New unique course ID
    """
    max_num = 0
    for course_id in existing_ids:
        if course_id.startswith("CRS"):
            try:
                num = int(course_id[3:])
                max_num = max(max_num, num)
            except ValueError:
                continue

    new_num = max_num + 1
    return f"CRS{new_num:04d}"

def generate_class_id():
    """
    Generate a new class ID in format CLSXXXX.
    
    Retrieves class IDs from course data to ensure no gaps when reusing deleted IDs.
    
    Parameters:
        None
        
    Returns:
        str: New unique class ID
    """
    from Teacher.teacher_function import fetch_courses

    courses = fetch_courses()
    if not courses:
        return "CLS0001"  # Start fresh if no courses exist

    # Extract existing class IDs from all courses
    existing_ids = set()
    for course in courses:
        for class_data in course.get("course_timetable", []):
            if isinstance(class_data, dict) and "class_id" in class_data:
                existing_ids.add(class_data["class_id"])

    # Identify the lowest available class ID
    for i in range(1, len(existing_ids) + 2):  # Ensures it checks one beyond the max
        new_id = f"CLS{i:04d}"
        if new_id not in existing_ids:
            return new_id  # Return the first available ID

    return None  # Should never reach this point

def create_course():
    """
    Create a new course in the system.
    
    This function prompts for course details, generates a new course ID,
    and adds the course to the course data file. The new course is initialized
    with empty lists for enrolled students and timetable entries.
    
    Parameters:
        None
        
    Returns:
        None
    """
    # Get course details
    courses = fetch_data("data/course_data.txt")
    if not courses:
        courses = []

    # Generate new course ID
    existing_ids = [course.get("course_id", "CRS0000") for course in courses]
    new_id = generate_course_id(existing_ids)

    # Get other course details
    course_title = input("Enter course title: ")
    lesson_plan = input("Enter course lesson plan: ")
    assignment_name = input("Enter assignment name: ")

    # Create new course with empty timetable
    new_course = {
        "course_id": new_id,
        "course_title": course_title,
        "lesson_plan": lesson_plan,
        "course_assignment": assignment_name,
        "course_material": {"lecture_note": "", "assignment_guideline": "", "announcement": ""},
        "students_enrolled": [],  # Empty dictionary where key=student_id, value=student_name
        "course_timetable": []  # Empty list for staff to fill later
    }

    # Add to courses list and save
    courses.append(new_course)

    if insert_data("data/course_data.txt", courses):
        print(f"Course {new_id} successfully created.")

def change_course_name():
    """
    Update the name of an existing course.
    
    This function displays all available courses, prompts for a course ID
    and new name, then updates the course record if found.
    
    Parameters:
        None
        
    Returns:
        None
    """
    courses_data = get_courses()
    found = False

    display_course(courses_data)
    prompt1 = input("Enter course id: ")

    for data in courses_data:
        if data['course_id'] == prompt1:
            found = True
            prompt2 = input("Enter new name for the course: ")
            data["course_title"] = prompt2  # Update the course in the list
            break

    if found:
        if insert_data("data/course_data.txt", courses_data):  # Consistent path format
            print(f"Course name updated successfully.")
        else:
            print("Error updating course name.")
    else:
        print("Invalid course")


def change_course_lesson_plan():
    """
    Update the lesson plan of an existing course.
    
    This function displays all available courses, prompts for a course ID
    and new lesson plan, then updates the course record if found.
    
    Parameters:
        None
        
    Returns:
        None
    """
    courses_data = get_courses()
    found = False

    display_course(courses_data)
    prompt1 = input("Enter course id: ")

    for data in courses_data:
        if data['course_id'] == prompt1:
            found = True
            prompt2 = input("Enter new lesson plan: ")
            data["lesson_plan"] = prompt2  # Update the course description
            break

    if found:
        if insert_data("data/course_data.txt", courses_data):
            print(f"Course description updated successfully.")
        else:
            print("Error updating course description.")
    else:
        print("Invalid course")

def update_course_timetable():
    """
    Add a new timetable entry to an existing course.
    
    This function prompts for course ID, teacher ID, and time slot details,
    then adds a new class to the course's timetable. It validates the teacher ID
    and generates a unique class ID for the new entry.
    
    Parameters:
        None
        
    Returns:
        None
    """
    courses_data = get_courses()
    found = False

    display_course(courses_data)
    course_id = input("Enter course id: ")

    # Find the course
    for course in courses_data:
        if course['course_id'] == course_id:
            found = True

            # Get and validate teacher
            teacher_id = input("Enter teacher id: ")
            teachers = fetch_data("data/user_data.txt")
            teacher_valid = False

            for user in teachers:
                if user["student_id"] == teacher_id and user["account_type"] == "teacher":
                    teacher_valid = True
                    break

            if not teacher_valid:
                print("Invalid teacher ID! Please enter a valid teacher username.")
                return

            # Get time slots
            print("\nEnter time slot details:")
            time_start = input("Enter start time (e.g., 9:00 AM): ")
            time_end = input("Enter end time (e.g., 12:00 PM): ")

            # Create new timetable entry
            new_slot = {
                "class_id": generate_class_id(),
                "time_start": time_start,
                "time_end": time_end,
                "course_teacher": teacher_id,
                "attendance_list": []
            }

            # Initialize timetable as list
            if not course.get('course_timetable'):
                course['course_timetable'] = []
            elif isinstance(course['course_timetable'], str):
                try:
                    # Convert string representation back to list
                    import ast
                    course['course_timetable'] = ast.literal_eval(course['course_timetable'])
                except:
                    course['course_timetable'] = []

            if not isinstance(course['course_timetable'], list):
                course['course_timetable'] = []

            # Add to course timetable
            course['course_timetable'].append(new_slot)

            # Save updated courses data
            if insert_data("data/course_data.txt", courses_data):
                print("Course timetable updated successfully.")
                print(f"Added: {time_start} - {time_end} with teacher {teacher_id}")
            else:
                print("Error updating course timetable.")
            break

    if not found:
        print("Invalid course ID")

def view_course_timetable():
    """
    Display the timetable for a specific course.
    
    This function prompts for a course ID and displays all timetable entries
    for the selected course, including start time, end time, and assigned teacher.
    
    Parameters:
        None
        
    Returns:
        None
    """
    courses_data = get_courses()
    found = False

    display_course(courses_data)
    course_id = input("Enter course id: ")

    for data in courses_data:
        if data['course_id'] == course_id:
            found = True
            timetable_data = data.get('course_timetable', [])

            if not timetable_data:
                print("No timetable entries found for this course.")
                return

            for slot in timetable_data:
                print("\nTimetable Entry:")
                print("Start time:", slot.get('time_start'))
                print("End time:", slot.get('time_end'))
                print("Teacher:", slot.get('course_teacher'))
                print("-" * 50)
            return

    if not found:
        print("Invalid course id")

def update_course():
    """
    Present a menu for various course update operations.
    
    This function displays options for changing course name or lesson plan,
    updating timetable, deleting a class, or viewing the timetable.
    
    Parameters:
        None
        
    Returns:
        None
    """
    print(
        "\n'1' - Change course name\n'2' - Change course lesson\n'3' - Update / Create course timetable\n'4' - Delete class\n'5' - View course timetable")
    choice = input("Enter your choice: ")

    if choice == '1':
        change_course_name()
    elif choice == '2':
        change_course_lesson_plan()
    elif choice == '3':
        update_course_timetable()
    elif choice == '4':
        from Teacher.class_attendance_management import delete_class
        delete_class()
    elif choice == '5':
        view_course_timetable()
    else:
        print("Invalid choice")

def delete_course():
    """
    Delete a course from the system.
    
    This function displays all available courses, prompts for a course ID,
    and removes the selected course from the course data file.
    
    Parameters:
        None
        
    Returns:
        None
    """
    courses_data = get_courses()
    found = False

    display_course(courses_data)
    prompt1 = input("Enter course id: ")

    # Create new list without the course to be deleted
    updated_courses = []
    for data in courses_data:
        if data["course_id"] == prompt1:
            found = True
        else:
            updated_courses.append(data)

    if found:
        if insert_data("data/course_data.txt", updated_courses):
            print(f"Course {prompt1} has been removed!")
        else:
            print("Error deleting course. Please try again.")
    else:
        print("Invalid course id")

def view_courses():
    """
    Display detailed information for all courses.
    
    This function retrieves and displays comprehensive details for each course,
    including course ID, title, lesson plan, and timetable entries.
    
    Parameters:
        None
        
    Returns:
        None
    """
    courses_data = get_courses()

    if not courses_data:
        print("No courses found.")
        return

    for course in courses_data:
        print("\n" + "=" * 50)
        print(f"Course ID: {course['course_id']}")
        print(f"Title: {course['course_title']}")
        print(f"Lesson Plan: {course['lesson_plan']}")

        # Display timetable if it exists
        if course['course_timetable']:
            print("\nTimetable:")
            for slot in course['course_timetable']:
                print(f"  • {slot['time_start']} - {slot['time_end']}")
                print(f"    Teacher: {slot['course_teacher']}")
        else:
            print("\nTimetable: No schedule yet")

        print("=" * 50)

def manage_course():
    """
    Present the main course management menu.
    
    This function displays options for creating, updating, deleting,
    and viewing courses, or returning to the previous menu.
    
    Parameters:
        None
        
    Returns:
        None
    """
    while True:
        print("'1' - Create Course\n'2' - Update Course\n'3' - Delete Course\n'4' - View Courses\n'5' - Back")

        choice = input("Enter your choice: ")
        if choice == '1':
            create_course()
        elif choice == '2':
            update_course()
        elif choice == '3':
            delete_course()
        elif choice == '4':
            view_courses()
        elif choice == '5':
            return
        else:
            print("Invalid choice")