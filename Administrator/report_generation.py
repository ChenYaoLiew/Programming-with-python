from function.query import *  # Import database query functions

def format_table(data, headers=None):
    """Format data as a table using only built-in Python"""
    if not data:
        return "No data available"
    
    # If data is a list of dictionaries, convert to a list of lists with headers
    if isinstance(data[0], dict):
        if not headers:
            headers = list(data[0].keys())
        rows = [[row.get(header, '') for header in headers] for row in data]
    else:
        rows = data
    
    # Convert all values to strings
    str_rows = [[str(cell) for cell in row] for row in rows]
    
    # Determine column widths
    if headers:
        all_rows = [headers] + str_rows
    else:
        all_rows = str_rows
    
    col_widths = [max(len(row[i]) for row in all_rows) for i in range(len(all_rows[0]))]
    
    # Create the table
    result = []
    
    # Add header
    if headers:
        header_row = ' | '.join(headers[i].ljust(col_widths[i]) for i in range(len(headers)))
        result.append(header_row)
        result.append('-' * len(header_row))
    
    # Add data rows
    for row in str_rows:
        result.append(' | '.join(row[i].ljust(col_widths[i]) for i in range(len(row))))
    
    return '\n'.join(result)

def generate_academic_report(student_id):
    """Generate academic performance report for a student"""
    # Pull academic data from database
    grades = get_student_grades(student_id)  # Assuming this function exists in your query module
    
    if not grades:
        print("No academic records found for this student.")
        return
    
    print("\n=== ACADEMIC PERFORMANCE REPORT ===")
    # Format and display the academic data
    print(format_table(grades))
    
    # Calculate and show averages, GPA, etc.
    try:
        scores = [grade['score'] for grade in grades if 'score' in grade]
        if scores:
            average_score = sum(scores) / len(scores)
            print(f"\nAverage Score: {average_score:.2f}")
    except (KeyError, TypeError):
        print("Could not calculate average score.")

def generate_attendance_report(student_id):
    """Generate attendance report for a student"""
    # Pull attendance data
    attendance = get_student_attendance(student_id)  # Assuming this function exists
    
    if not attendance:
        print("No attendance records found for this student.")
        return
    
    print("\n=== ATTENDANCE REPORT ===")
    # Format and display attendance data
    print(format_table(attendance["courses"]))
    
    # Calculate attendance percentage
    try:
        overall_percentage = attendance["overall_attendance"]["percentage"]
        print(f"\nOverall Attendance Rate: {overall_percentage:.2f}%")
    except (KeyError, TypeError, ZeroDivisionError):
        print("Could not calculate overall attendance rate.")

def generate_financial_report(student_id):
    """Generate financial report for a student"""
    # Pull financial data
    finances = get_student_finances(student_id)  # Assuming this function exists
    
    if not finances:
        print("No financial records found for this student.")
        return
    
    print("\n=== FINANCIAL REPORT ===")
    print(f"Remaining Balance: ${finances['balance']:.2f}")
    
    # Display transaction history if available
    if 'transactions' in finances and finances['transactions']:
        print("\nTransaction History:")
        transactions = finances['transactions']
        print(format_table(transactions))

def get_total_students():
    """Get the total number of students in the system"""
    users = fetch_data("../data/user_data.txt")
    student_count = sum(1 for user in users if user.get("accountType") == "student")
    return student_count

def get_total_teachers():
    """Get the total number of teachers in the system"""
    users = fetch_data("../data/user_data.txt")
    teacher_count = sum(1 for user in users if user.get("accountType") == "teacher")
    return teacher_count

def get_total_courses():
    """Get the total number of courses in the system"""
    courses = fetch_data("../data/course_data.txt")
    return len(courses) if courses else 0

def generate_institution_report():
    """Generate overall institution report with counts"""
    # Get counts from database
    student_count = get_total_students()  # Assuming these functions exist
    teacher_count = get_total_teachers()
    course_count = get_total_courses()
    
    print("\n=== INSTITUTION REPORT ===")
    print(f"Total Students: {student_count}")
    print(f"Total Teachers: {teacher_count}")
    print(f"Total Courses: {course_count}")
    
    # Could add more metrics like average GPA, financial stats, etc.

def generate_reports():
    """Main function to handle report generation"""
    while True:
        print("\n=== REPORT GENERATION ===")
        print("1. Student Academic Report")
        print("2. Student Attendance Report")
        print("3. Student Financial Report")
        print("4. Institution Report")
        print("5. Return to Main Menu")
        
        choice = input("Select report type: ")
        
        if choice in ["1", "2", "3"]:
            student_id = input("Enter student ID: ")
            
            if choice == "1":
                generate_academic_report(student_id)
            elif choice == "2":
                generate_attendance_report(student_id)
            elif choice == "3":
                generate_financial_report(student_id)
                
        elif choice == "4":
            generate_institution_report()
            
        elif choice == "5":
            return
            
        else:
            print("Invalid option. Please try again.")
        
        input("\nPress Enter to continue...")

def get_student_grades(student_id):
    """
    Retrieve all grades for a student across all enrolled courses
    
    Args:
        student_id (str): The student ID to get grades for
    
    Returns:
        list: List of dictionaries containing grade information
    """
    # Get all course data where student is enrolled
    courses_data = fetch_data("../data/course_data.txt")
    grades = []
    
    # Extract grade information from all courses
    for course in courses_data:
        for student in course.get("students_enrolled", []):
            if student.get("student_id") == student_id:
                grades.append({
                    "course_id": course["course_id"],
                    "course_title": course["course_title"],
                    "assignment_grade": student.get("assignment_grade", "Not graded"),
                    "exam_grade": student.get("exam_grade", "Not graded"),
                    "feedback": student.get("feedback", "No feedback provided")
                })
    
    return grades

def get_student_attendance(student_id):
    """
    Retrieve attendance records for a student across all classes with percentage calculations
    
    Args:
        student_id (str): The student ID to get attendance for
    
    Returns:
        dict: Dictionary containing attendance records and percentage calculations
    """
    # Get all course data
    courses_data = fetch_data("../data/course_data.txt")
    
    # Structure to hold attendance data by course
    attendance_by_course = {}
    total_present = 0
    total_classes = 0
    
    for course in courses_data:
        course_id = course["course_id"]
        course_title = course["course_title"]
        
        # Check if student is enrolled in this course
        is_enrolled = any(student.get("student_id") == student_id 
                         for student in course.get("students_enrolled", []))
        
        if is_enrolled:
            # Initialize course attendance data if not exists
            if course_id not in attendance_by_course:
                attendance_by_course[course_id] = {
                    "course_id": course_id,
                    "course_title": course_title,
                    "present_count": 0,
                    "total_classes": 0,
                    "records": []
                }
            
            # Process each class session
            for class_session in course.get("course_timetable", []):
                # Check if this class has attendance records
                attendance_list = class_session.get("attendance_list", [])
                
                # Find if student has attendance record for this class
                student_attendance = next(
                    (a for a in attendance_list if a.get("student_id") == student_id), 
                    None
                )
                
                # If class exists, count it for this course
                attendance_by_course[course_id]["total_classes"] += 1
                total_classes += 1
                
                # If student was present, increment counters
                if student_attendance and student_attendance.get("attendance") == "Present":
                    attendance_by_course[course_id]["present_count"] += 1
                    total_present += 1
                
                # Add detailed record
                if student_attendance:
                    attendance_by_course[course_id]["records"].append({
                        "class_id": class_session.get("class_id", "Unknown"),
                        "status": student_attendance.get("attendance", "Not recorded")
                    })
    
    # Calculate percentages for each course
    for course_id in attendance_by_course:
        course = attendance_by_course[course_id]
        total = course["total_classes"]
        if total > 0:
            course["attendance_percentage"] = (course["present_count"] / total) * 100
        else:
            course["attendance_percentage"] = 0
    
    # Calculate overall percentage
    overall_percentage = 0
    if total_classes > 0:
        overall_percentage = (total_present / total_classes) * 100
    
    # Return complete structure
    return {
        "overall_attendance": {
            "present_count": total_present,
            "total_classes": total_classes,
            "percentage": overall_percentage
        },
        "courses": list(attendance_by_course.values())
    }

def get_student_finances(student_id):
    """
    Retrieve financial information for a student
    
    Args:
        student_id (str): The student ID to get finances for
    
    Returns:
        dict: Dictionary containing balance information
    """
    # Get student data to find balance
    student_data = fetch_data("../data/user_data.txt")
    student = next((s for s in student_data if s.get("student_id") == student_id), None)
    
    if not student:
        return None
    
    # Create basic financial info structure
    finances = {
        "balance": float(student.get("fund", 0))
    }
    
    return finances