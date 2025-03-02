from function.query import fetch_data

def show_grade(student_info):
    """
    Used when student need to check their grades
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
    """
    student_course_data = fetch_data("data/student_data.txt") # A list of all student's course data

    # Find the student's course data and display it
    for student in student_course_data:
        if student['student_id'] == student_info[1]['student_id']:
            print('\nGrades Tracking')
            print(f'Math grade   : {student["math_grade"]}')
            print(f'Science grade: {student["science_grade"]}')
            print(f'English grade: {student["english_grade"]}')