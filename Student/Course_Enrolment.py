from function.query import fetch_data
from Student.Student_function import get_student_course_id

all_courses = fetch_data('./data/course_data.txt')  # get a list of all courses data inside the txt file

def display_time_table(student_course, subject):
    """
    To display student's timetable with corresponding subject
    Args:
        student_course(dict): A dictionary which contain student's every subject and corresponding course_id
        subject(str): Subject name
    return:
        subject_course(Bool): if no enrolled yet return False
    """
    subject_course = False # Initially student's have subject course will be defined as False.

    # To iterate out every course the student have with corresponding subject.
    for course in all_courses:
        if course['course_id'] in student_course[subject]:
            print('-----------------------------------------------------------')
            print(f'Course ID         : {course['course_id']}\n'
                  f'Course Title      : {course['course_title']}\n'
                  f'Lesson Plan       : {course['lesson_plan']}\n'
                  f'Course Assignment : {course['course_assignment']}\n'
                  f'Time Table:')

            # To iterate out every class in that course
            for index, time in enumerate(course["course_timetable"], start=1):
                print(f'\nClass [ {index} ]\n'
                      f'Class ID     : {time['class_id']}\n'
                      f'Class teacher: {time['course_teacher']}\n'
                      f'Time Start   : {time['time_start']}\n'
                      f'Time End     : {time['time_end']}')
            print('-----------------------------------------------------------')

            subject_course = True

    return subject_course

def time_table(student_info):
    """
    To display all timetable with its subject
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
    return:
        None
    """
    # A dictionary which contain student's every subject and corresponding course_id
    student_course = get_student_course_id(student_info, all_courses)

    print('\n[ Math ]')
    if not display_time_table(student_course, 'Math'): # if no subject's course enrolled, print No Math courses enrolled!
        print('No Math courses enrolled!')

    print('\n[ Science ]')
    if not display_time_table(student_course, 'Science'):
        print('No Science courses enrolled!')

    print('\n[ English ]')
    if not display_time_table(student_course, 'English'):
        print('No English courses enrolled!')
