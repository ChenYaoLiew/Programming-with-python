# Grade attendance of student of selected course

def enrol_stud_class():
    from Teacher.teacher_function import fetch_courses, display_course, select_course,select_class,validate_stud_id
    from function.query import insert_data

    courses = fetch_courses()
    if not courses:
        return

    display_course()

    selected_course = select_course(courses,action="Enrol Student Into a Class")
    if not selected_course:
        return

    # Get all class id in the selected course and print it all out
    class_match = select_class(selected_course, action="Enrolling Student Into a Class")

    if not class_match:
        print("No classes available for this course.")
        return

    # Get student id to enroll
    student_id = input("Enter Student ID (Make sure Student ID is registered in system): ").strip()

    if not validate_stud_id(student_id):
        print("Student ID not valid.")
        return

    # Check if the student is already enrolled into the class
    if any(record["student_id"].strip() == student_id for record in class_match["attendance_list"]):
        print(f"Student ID: {student_id} already enrolled into class {class_match['class_id']}.")
        return

    # Creat new field to be used later
    enrolled_class_student = {
        "student_id": student_id,
        "attendance": "Absent"
    }

    class_match["attendance_list"].append(enrolled_class_student)

    print(f"Student ID: {student_id} is enrolled into class {class_match['class_id']}.")

    # save_data
    courses[selected_course[0]] = selected_course[1]
    file_path = "data/course_data.txt"
    insert_data(file_path, courses)

def delete_class():
    from function.query import fetch_data,insert_data
    """
    Delete a class by class_id from the course_data file.
    """
    import os
    file_path = "data/course_data.txt"
    if not os.path.exists(file_path):
        print("File path not found.")
        return

    courses = fetch_data(file_path)
    found = False

    class_id = input("Enter class ID: ").strip()
    from Teacher.teacher_function import validate_class_id
    if not validate_class_id(class_id):
        return

    for course in courses:
        original_length = len(course["course_timetable"])
        course["course_timetable"] = [cls for cls in course["course_timetable"] if cls["class_id"] != class_id]
        if len(course["course_timetable"]) < original_length:
            found = True

    if found:
        insert_data(file_path, courses)
        print(f"Class {class_id} deleted successfully.")
    else:
        print(f"Class {class_id} not found.")

def delete_stud_class():
    from Teacher.teacher_function import fetch_courses, display_course, select_course, select_class, validate_stud_id,display_students_in_class
    from function.query import insert_data
    import os

    courses = fetch_courses()
    if not courses:
        return

    display_course()

    selected_course = select_course(courses, action="Remove Student From a Class")
    if not selected_course:
        return

    # Select the class
    class_match = select_class(selected_course, action="Removing Student From a Class")

    if not class_match:
        print("No classes available for this course.")
        return

    # Display students in the selected class
    display_students_in_class(class_match)

    # Check if there are any students enrolled in the class
    if not class_match.get("attendance_list"):
        return

    # Get student ID to remove
    student_id = input("Enter Student ID to remove: ").strip()

    if not validate_stud_id(student_id):
        print("Student ID not valid.")
        return

    # Check if student exists in the class
    student_record = next((record for record in class_match["attendance_list"] if record["student_id"] == student_id), None)

    if not student_record:
        print(f"Student ID: {student_id} not found in class {class_match['class_id']}.")
        return

    # Remove the student from the attendance list
    class_match["attendance_list"].remove(student_record)
    print(f"Student ID: {student_id} has been removed from class {class_match['class_id']}.")

    # Save data
    courses[selected_course[0]] = selected_course[1]
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "course_data.txt")
    insert_data(file_path, courses)

def grade_attendance():
    from Teacher.teacher_function import fetch_courses, display_course, select_course, select_class, validate_stud_id
    from function.query import insert_data

    courses = fetch_courses()
    if not courses:
        return

    display_course()

    # Select the course
    selected_course = select_course(courses, action="Grade Attendance")
    if not selected_course:
        return

    class_match = select_class(selected_course, action="Grade Attendance")
    if not class_match:
        return

    # Print out all student_id in that class
    print("\nStudents in this class:")
    if class_match["attendance_list"]:
        for student in class_match["attendance_list"]:
            print(f"- {student['student_id']}")
    else:
        print("No students found in this class.")
        return

    # Get student id to grade attendance
    student_id = input("\nEnter Student ID to give attendance: ")

    if not validate_stud_id(student_id):
        return

    if validate_stud_id(student_id):
        # Initialize attendance_status
        attendance_status = None

        # Enter attendance
        print("1 - Mark Present\n2 - Mark Absent ")
        choice = input("Enter Choice: ")
        if choice == '1':
            attendance_status = "Present"
        elif choice == '2':
            attendance_status = "Absent"
        else:
            print("Invalid choice. Attendance not updated.")
            return attendance_status

        # Find the student in the attendance list
        student_attendance = next((record for record in class_match["attendance_list"] if record["student_id"] == student_id), None)
        # If found, Grade assignment of that student
        if student_attendance:
            student_attendance["attendance"] = attendance_status
            print(f"Attendance for {student_id} updated to {attendance_status}.")
        else:
            print(f"Student ID {student_id} not found in the class. Attendance not updated.")

        # save_data
        courses[selected_course[0]] = selected_course[1]
        file_path = "data/course_data.txt"
        insert_data(file_path,courses)

def view_stud_attendance():
    from Teacher.teacher_function import fetch_courses, display_course, select_course, select_class

    courses = fetch_courses()
    if not courses:
        return

    display_course()

    selected_course = select_course(courses, action="View Student Attendance")
    if not selected_course:
        return

    # Use the select_class function to select a class
    class_match = select_class(selected_course, action="View Student Attendance")
    if not class_match:
        return

    # Print student attendance records
    print("\nStudent Attendance Records:")
    if class_match["attendance_list"]:
        for student in class_match["attendance_list"]:
            print(f"- {student['student_id']}: {student.get('attendance', 'Not marked')}")
    else:
        print("No students found in this class.")


def manage_attendance():
    while True:
        print("\nWelcome to Class & Attendance Management\n1 - Enrol Student into a Class\n2 - Remove Student from Enrolled Class\n3 - Delete class\n4 - Grade Attendance\n5 - View Attendance\n6 - Back")

        choice = input("\nEnter Choice: ").strip()

        if choice == '1':
            enrol_stud_class()
        elif choice == '2':
            delete_stud_class()
        elif choice == '3':
            delete_class()
        elif choice == '4':
            grade_attendance()
        elif choice == '5':
            view_stud_attendance()
        elif choice == '6':
            from Teacher.menu import teacher_menu_page
            teacher_menu_page()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")











