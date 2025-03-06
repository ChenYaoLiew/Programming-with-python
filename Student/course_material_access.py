from Student.Student_function import get_student_course_id
from function.query import fetch_data

all_courses = fetch_data('./data/course_data.txt')  # get a list of all courses data inside the txt file

def show_course_material(student_course, subject):
    """
    To display course material with corresponding subject
    Args:
        student_course(dict): A dictionary which contain student's every subject and corresponding course_id
        subject(str): Subject name
    return:
        None
    """
    print(f'[ {subject} material ]')
    # To make sure student have course in that subject, if no print no course enrolled
    if student_course[subject]:
        # print out all the course material with its course_id
        for course in all_courses:
            if course['course_id'] in student_course[subject]:
                print('----------------------------------------------------------------------------')
                print(f'Course ID            : {course['course_id']}')
                print(f'lecture Note         : {course['course_material']['lecture_note']}')
                print(f'Assignment Guideline : {course['course_material']['assignment_guideline']}')
                print(f'Announcement         : {course['course_material']['announcement']}')
    else:
        print(f'No {subject} course enrolled!')

def course_material(student_info):
    """
    To display course material menu
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
    return:
        None
    """
    student_course = get_student_course_id(student_info, all_courses)

    while True:
        # Display menu
        print('\n[ Course Material ]')
        print('"1" - Math')
        print('"2" - Science')
        print('"3" - English')
        print('"0" - Back')

        choice = input('Enter your choice: ')

        if choice == '1':
            show_course_material(student_course, 'Math')
        elif choice == '2':
            show_course_material(student_course, 'Science')
        elif choice == '3':
            show_course_material(student_course, 'English')
        elif choice == '0':
            break
        else:
            print('Invalid choice!')