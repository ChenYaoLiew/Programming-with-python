# Report Generation
# Generate reports on student performance and participation for administrative review
# Report will be in this format:
# === Student Report ===
# course_id: M0001
# course_title: Math
# assignment_submission: Empty
# assignment_grade: Not graded
# exam_grade: Not graded
# class_id: CLS0001
# attendance: Absent
# report: exam did great but assignment didn't submit in time

def generate_student_report():
    """
    Generates a report containing a student's course and performance details.
    Displays course selection, enrolled students, and generates a structured report.
    """
    from teacher_function import fetch_courses, display_course, display_students_in_course, select_course

    courses = fetch_courses()
    if not courses:
        print("No courses available.")
        return

    display_course()

    selected_course = select_course(courses, action="Generate Student Report")

    if not selected_course:
        print("No course selected.")
        return

    course_data = selected_course[1] # Get the course dictionary

    # Check for no enrolled students
    if not selected_course[1]["students_enrolled"]:
        print("\nNo students enrolled in this course.")
        return  # Exit the function early

    display_students_in_course(course_data)

    student_id = input("\nEnter Student ID to generate report: ").strip()

    student_found = next(
        (student for student in course_data["students_enrolled"] if student["student_id"] == student_id), None)

    if not student_found:
        print("Student ID not found in this course.")
        return

    # Retrieve attendance data
    class_id = "Not Available"
    attendance_status = "Not Recorded"

    for class_data in course_data.get("course_timetable", []):
        for attendance_record in class_data.get("attendance_list", []):
            if attendance_record["student_id"] == student_id:
                class_id = class_data["class_id"]
                attendance_status = attendance_record["attendance"]
                break

    # Generate report
    report = {
        "course_id": course_data["course_id"],
        "course_title": course_data["course_title"],
        "assignment_submission": student_found.get("assignment_submission", "Not submitted"),
        "assignment_grade": student_found.get("assignment_grade", "Not graded"),
        "exam_grade": student_found.get("exam_grade", "Not graded"),
        "class_id": class_id,
        "attendance": attendance_status,
        "feedback" : student_found.get("feedback"),
    }

    print("\n=== Student Report ===")
    for key, value in report.items():
        print(f"{key}: {value}")

    return report

