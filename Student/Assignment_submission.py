from function.query import *
from Student.Student_function import get_student_course_id

all_courses = fetch_data('./data/course_data.txt') # get a list of all courses data inside the txt file

def subject_assignment(student_info, student_course, subject):
    """
    To display assignment status with specified subject
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
        student_course(dict): A dictionary which contain student's every subject and corresponding course_id
        subject(str): Subject name
    return:
        have_subject_course(Bool): If student have course in particular subject it will be True
    """
    student_data = student_info[1]
    have_subject_course = False # Initially student's have subject course will be defined as False.

    while True:
        print(f'\n[ {subject} ]')

        # To show their course assignment status if student has course
        for course in all_courses:
            for student in course['students_enrolled']:
                if course['course_id'] in student_course[subject] and student['student_id'] == student_data['student_id']:
                    have_subject_course = True
                    print('--------------------------------------------------------------')
                    print(f"Course ID             : {course['course_id']}")
                    print(f"Course Assignment     : {course['course_assignment']}")
                    print(f"Assignment Submission : {student['assignment_submission']}")

        # If student has course, assignment submission will run
        if have_subject_course:
            # Choose the course ID to submit assignment
            course_id = input('\nInput the Course ID to submit your assignment (Press 0 to Back): ')

            if course_id == '0':
                return have_subject_course

            elif course_id in student_course[subject]:
                # Assignment submission
                assignment = input('Input your assignment here: ')

                # iterate out specified course data to update assignment submissions for students in the corresponding course
                chosen_course = next(course for course in all_courses if course['course_id'] == course_id)
                student_course_data = next(student_course_data for student_course_data in chosen_course['students_enrolled'] if student_course_data['student_id'] == student_data['student_id'])
                student_course_data['assignment_submission'] = assignment
                print('Assignment uploaded!')
                continue

            else:
                print('Invalid Input!')

        else:
            return have_subject_course

def assignment_sub_menu(student_info):
    """
    To display assignment submission menu
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
    return:
        None
    """
    # A dictionary which contain student's every subject and corresponding course_id
    student_course = get_student_course_id(student_info, all_courses)

    while True:
        print('\n[ Course Assignment Submission ]')
        print('1 - Math')
        print('2 - Science')
        print('3 - English')
        print('0 - Save changes and Back')

        choice = input('Enter your choice: ')
        # If student got no course in that particular subject, it will display no courses enrolled.
        if choice == '1':
            if not subject_assignment(student_info, student_course, 'Math'):
                print('No Math courses enrolled!')

        elif choice == '2':
            if not subject_assignment(student_info, student_course, 'Science'):
                print('No Science courses enrolled!')

        elif choice == '3':
            if not subject_assignment(student_info, student_course, 'English'):
                print('No English courses enrolled!')

        elif choice == '0':
            insert_data('./data/course_data.txt', all_courses)
            break

        else:
            print('Invalid choice')