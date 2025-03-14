from function.query import fetch_data
from Student.Student_function import get_student_course_id

all_courses = fetch_data('./data/course_data.txt')  # get a list of all courses data inside the txt file

def get_all_teacher(file_path):
    """
    To get all the teacher id and their name in a dictionary
    Args:
        file_path (str): The directory of the file
    Returns:
        teacher_dict(dict): A dictionary that store all the teacher ID and their name
    """
    from function.query import fetch_data
    all_user = fetch_data(file_path)
    teacher_dict = {}

    # To get all the user in the file and insert into teacher_dict
    for user in all_user:
        if user['account_type'] == 'teacher':
            teacher_dict[user['student_id']] = user['username']

    return teacher_dict

def time_table(student_info):
    """
    Display all the course and its timetable with specified student_id
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
    Returns:
        None
    """
    # A dictionary that contain all the student's subject and corresponding course
    student_course = get_student_course_id(student_info, all_courses)
    # A dictionary that store all the teacher ID and their name
    teacher_dict = get_all_teacher('./data/user_data.txt')

    if student_course: # Check if student got any subject that was already enrolled
        for subject in student_course: # Check the subject of the student one by one
            print(f'\n[ {subject} ]')
            for sub_info in student_course[subject]: # Check all the courses of the subject one by one
                print('-----------------------------------------------------------')
                print(f'Course ID         : {sub_info['course_id']}\n'
                      f'Course Title      : {sub_info['course_title']}\n'
                      f'Lesson Plan       : {sub_info['lesson_plan']}\n'
                      f'Course Assignment : {sub_info['course_assignment']}\n'
                      f'Time Table:')

                # To iterate out every class in that course
                for index, classes in enumerate(sub_info["course_timetable"], start=1):
                    print(f'\nClass [ {index} ]\n'
                          f'Class ID     : {classes['class_id']}\n'
                          f'Class teacher: {teacher_dict[classes['course_teacher']]}\n'
                          f'Time Start   : {classes['time_start']}\n'
                          f'Time End     : {classes['time_end']}')
                print('-----------------------------------------------------------')
    else:
        print('\nNo courses enrolled!')