from function.query import *
from Student.Student_function import get_student_course_id
from Student.Student_function import display_subject_menu

all_courses = fetch_data('data/course_data.txt') # get a list of all courses data inside the txt file

def get_sub_info_list(student_course, subject):
    """
    To get all the courses ID of specified subject
    Args:
        student_course(dict): A dictionary that contain all the student's subject and corresponding course
        subject(str): The subject name
    Returns:
        sub_info_list(list): A list of courses ID
    """
    sub_info_list = []

    for sub_info in student_course[subject]:
        sub_info_list.append(sub_info['course_id'])

    return sub_info_list

def assignment_sub_menu(student_info):
    """
    Student can choose the subject with corresponding course that they want to submit the assignment
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
    Returns:
        None
    """
    student_data = student_info[1] # Data of the student
    student_course = get_student_course_id(student_info, all_courses) # A dictionary which contain student's every subject and corresponding course_id
    subject_list = list(student_course) # A list of the student's subject

    # Display the subject option, if any course enrolled
    while True:
        if not display_subject_menu(student_course, 'Course Assignment Submission'):
            print('No courses enrolled!')
            break

        # Choose the subject
        sub_choice = input('Enter your choice: ')
        try:
            sub_choice = int(sub_choice) # Convert the choice to an integer to ensure subject that selected by the student

            if sub_choice == 0:
                break # GO back

            elif 1 <= sub_choice <= len(subject_list):  # Make sure student input the correct choice
                subject = subject_list[sub_choice - 1] # Get the subject name with corresponding index

                # print out all the course assignment info of corresponding subject
                while True:
                    print(f'\n[ {subject} ]')
                    for sub_info in student_course[subject]:
                        for student in sub_info['students_enrolled']:
                            if student_data['student_id'] == student['student_id']:
                                print('--------------------------------------------------------------')
                                print(f"Course ID             : {sub_info['course_id']}")
                                print(f"Course Assignment     : {sub_info['course_assignment']}")
                                print(f"Assignment Submission : {student['assignment_submission']}")

                    # Choose the course ID to submit assignment
                    course_id = input('\nInput the Course ID to submit your assignment (Press 0 to Back): ')

                    if course_id == '0':
                        break # Back to choose subject

                    # Make sure student input the correct course ID
                    elif course_id in get_sub_info_list(student_course, subject):
                        assignment = input('Input your assignment here(Press 0 to back): ')

                        if assignment == '0':
                            break # Back to choose subject

                        else:
                            # iterate out specified course data to update assignment submissions for students in the corresponding course
                            chosen_course = next(course for course in all_courses if course['course_id'] == course_id)
                            student_course_data = next(student_course_data for student_course_data in chosen_course['students_enrolled'] if student_course_data['student_id'] == student_data['student_id'])
                            student_course_data['assignment_submission'] = assignment
                            print('Assignment uploaded!')

                            # Update new data to the course_data file
                            insert_data('data/course_data.txt', all_courses)
                            continue
                    else:
                        print('Invalid course ID!')

            else:
                print('Invalid choice!')

        except ValueError:
            print('Invalid choice!')