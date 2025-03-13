from Student.Student_function import get_student_course_id
from Student.Student_function import display_subject_menu
from function.query import fetch_data


all_courses = fetch_data('./data/course_data.txt')  # get a list of all courses data inside the txt file

def course_material(student_info):
    """
    Display all the course and its course material
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
    Returns:
        None
    """
    # A dictionary that contain all the student's subject and corresponding course
    student_course = get_student_course_id(student_info, all_courses)
    # A list of the student's subject
    subject_list = list(student_course)

    while True:
        # Display menu
        if not display_subject_menu(student_course, 'Course Material'):
            print('No courses enrolled!')
            break

        sub_choice = input('Enter your choice: ')
        try:
            sub_choice = int(sub_choice) # Convert the choice to an integer to ensure subject that selected by the student

            if sub_choice == 0: # if choice is 0 student will back to main page
                break

            # Make sure student input the correct choice and display the course material in the course
            elif 1 <= sub_choice <= len(subject_list):
                subject = subject_list[sub_choice - 1] # Get the subject name with corresponding index
                # Display assignment info
                print(f'\n[ {subject} ]')
                for sub_info in student_course[subject]:
                        print('----------------------------------------------------------------------------')
                        print(f'Course ID            : {sub_info['course_id']}')
                        print(f'lecture Note         : {sub_info['course_material']['lecture_note']}')
                        print(f'Assignment Guideline : {sub_info['course_material']['assignment_guideline']}')
                        print(f'Announcement         : {sub_info['course_material']['announcement']}')

            else:
                print('Invalid choice!')

        except ValueError:
            print('Invalid choice!')