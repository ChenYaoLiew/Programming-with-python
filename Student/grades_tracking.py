from function.query import fetch_data
from Student.Student_function import get_student_course_id

all_courses = fetch_data('./data/course_data.txt') # A list of all student's course data

def show_subject_grade(student_info, student_course, subject):
    """
    To display student's course grade with particular subject
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
        student_course(dict): A dictionary which contain student's every subject and corresponding course_id
        subject(str): Subject name
    return:
        have_subject_course(Bool): If student have course in particular subject it will be True
    """
    student_data = student_info[1]
    have_subject_course = False # Initially student's have subject course will be defined as False.

    print(f'\n[ {subject} Grade ]')
    # To show their course assignment grade and exam grade, if student has course
    for course in all_courses:
        for student in course['students_enrolled']:
            if course['course_id'] in student_course[subject] and student['student_id'] == student_data['student_id']:
                have_subject_course = True
                print('--------------------------------------------------------------')
                print(f"Course ID             : {course['course_id']}")
                print(f"Course Assignment     : {course['course_assignment']}")
                print(f"Assignment Submission : {student['assignment_submission']}")
                print(f'Assignment Grade      : {student['assignment_grade']}')
                print(f'Exam Grade            : {student['exam_grade']}')
                print(f'Feedback              : {student['feedback']}')

    if not have_subject_course:
        print(f'No {subject} course enrolled!')

def show_grade(student_info):
    """
    To display grades tracking menu
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
    return:
        None
    """
    # A dictionary which contain student's every subject and corresponding course_id
    student_course = get_student_course_id(student_info, all_courses)

    while True:
        print('\nCourses Grade')
        print('"1" - Math')
        print('"2" - Science')
        print('"3" - English')
        print('"0" - Back')

        choice = input('Enter your choice: ')
        if choice == '1':
            show_subject_grade(student_info, student_course, 'Math')

        elif choice == '2':
            show_subject_grade(student_info, student_course, 'Science')

        elif choice == '3':
            show_subject_grade(student_info, student_course, 'English')

        elif choice == '0':
            break

        else:
            print('Invalid input!')