from Administrator.menu import administrator_user_page
from Teacher.grading_assessment import manage_grading_assessment
from Teacher.student_enrolment import manage_stu_enrol
from function.query import *

# Course Management: Create, update, or delete course offerings and assign instructors to courses. 

# {
#     "course_id" = XXXX,
#     "course_title" = "XXXX",
#     "course_description" = "XXXXXXX",
#     "students_enrolled" = [
#         {"student_id": "STD0001", "assignment_grade": "A", "assignment_submission": "","exam_grade": "B", "feedback": "Good"},
#         {"student_id": "STD0002", "assignment_grade": "A", "assignment_submission": "", "exam_grade": "B", "feedback": "Good"},
#     ],
#     "course_assignment" = "Google doc link",
#     "course_timetable"= [
#         {"time_start": "9:00 AM", "time_end": "12:00PM", "course_teacher": "TP_ID"},
#         {"time_start": "9:00 AM", "time_end": "12:00PM", "course_teacher": "TP_ID"},
#         {"time_start": "9:00 AM", "time_end": "12:00PM", "course_teacher": "TP_ID"},
#         {"time_start": "9:00 AM", "time_end": "12:00PM", "course_teacher": "TP_ID"},
#     ],
# }

def getCourses():
    data = fetch_data("data/course_data.txt")

    return data

def generate_course_id(existing_ids):
    """
    Generate a new course ID in format CRSXXXX
    Args:
        existing_ids (list): List of existing course IDs
    Returns:
        str: New unique course ID
    """
    max_num = 0
    for id in existing_ids:
        if id.startswith("CRS"):
            try:
                num = int(id[3:])
                max_num = max(max_num, num)
            except ValueError:
                continue
    
    new_num = max_num + 1
    return f"CRS{new_num:04d}"

def createCourse():
    # Get course details
    courses = fetch_data("data/course_data.txt")
    if not courses:
        courses = []

    # Generate new course ID
    existing_ids = [course.get("course_id", "CRS0000") for course in courses]
    new_id = generate_course_id(existing_ids)

    # Get other course details
    course_title = input("Enter course title: ")
    course_description = input("Enter course description: ")
    assignment_name = input("Enter assignment name: ")

    # Create new course with empty timetable
    new_course = {
        "course_id": new_id,
        "course_title": course_title,
        "course_description": course_description,
        "course_assignment": assignment_name,
        "course_material": {"lecture_note":"","assignment_guideline":"","announcement":""},
        "students_enrolled": [],  # Empty dictionary where key=student_id, value=student_name
        "course_timetable": []  # Empty list for staff to fill later
    }

    # Add to courses list and save
    courses.append(new_course)
    
    if insert_data("data/course_data.txt", courses):
        print(f"Course {new_id} successfully created.")

def changeCourseName():
    courses_data = getCourses()
    found = False

    prompt1 = input("Enter course id: ")

    for data in courses_data:
        if data['course_id'] == prompt1:
            found = True
            prompt2 = input("Enter new name: ")
            data["course_title"] = prompt2  # Update the course in the list
            break

    if found:
        if insert_data("data/course_data.txt", courses_data):  # Consistent path format
            print(f"Course name updated successfully.")
        else:
            print("Error updating course name.")
    else:
        print("Invalid course")

def changeCourseDescription():
    courses_data = getCourses()
    found = False

    prompt1 = input("Enter course id: ")

    for data in courses_data:
        if data['course_id'] == prompt1:
            found = True
            prompt2 = input("Enter new description: ")
            data["course_description"] = prompt2  # Update the course description
            break

    if found:
        if insert_data("data/course_data.txt", courses_data):
            print(f"Course description updated successfully.")
        else:
            print("Error updating course description.")
    else:
        print("Invalid course")

def updateCourseTimetable():
    courses_data = getCourses()
    found = False

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
                if user["student_id"] == teacher_id and user["accountType"] == "teacher":
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
                "time_start": time_start,
                "time_end": time_end,
                "course_teacher": teacher_id
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

def updateCourse():
    print("'1' - Change course name\n'2' - Change course description\n'3' - Update course timetable")
    choice = input("Enter your choice: ")

    if choice == '1':
        changeCourseName()
    elif choice == '2':
        changeCourseDescription()
    elif choice == '3':
        updateCourseTimetable()
    else:
        print("Invalid choice")

def deleteCourse():
    prompt1 = input("Enter course id: ")
    found = False
    courses_data = getCourses()
    
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
    
def viewCourses():
    courses_data = getCourses()
    
    if not courses_data:
        print("No courses found.")
        return

    for course in courses_data:
        print("\n" + "="*50)
        print(f"Course ID: {course['course_id']}")
        print(f"Title: {course['course_title']}")
        print(f"Description: {course['course_description']}")
        
        # Display timetable if it exists
        if course['course_timetable']:
            print("\nTimetable:")
            for slot in course['course_timetable']:
                print(f"  • {slot['time_start']} - {slot['time_end']}")
                print(f"    Teacher: {slot['course_teacher']}")
        else:
            print("\nTimetable: No schedule yet")
        
        print("="*50)


def manageCourse():
    print("'1' - Create Course\n'2' - Update Course\n'3' - Delete Course\n'4' - View Courses\n'5' - Back")

    choice = input("Enter your choice: ")
    if choice == '1':
        createCourse()
    elif choice == '2':
        updateCourse()
    elif choice == '3':
        deleteCourse()
    elif choice == '4':
        viewCourses()
    elif choice == '5':
        administrator_user_page()

