from function.query import fetch_data
from Student.Student_function import get_student_course_id
from Student.Student_function import display_subject_menu

def show_grade(student_info):
    """
        Student can choose the subject with corresponding course that they want to submit the assignment
        Args:
            student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
        Returns:
            None
        """
    student_data = student_info[1] # Data of the student
    all_courses = fetch_data('data/course_data.txt') # A list of all student's course data
    student_course = get_student_course_id(student_info, all_courses) # A dictionary which contain student's every subject and corresponding course
    subject_list = list(student_course) # A list of the student's subject

    # Display the subject option, if any course enrolled
    while True:
        if not display_subject_menu(student_course, 'Courses Grade'):
            print('No courses enrolled!')
            break

        sub_choice = input('Enter your choice: ')
        try:
            sub_choice = int(sub_choice) # Convert the choice to an integer to ensure subject that selected by the student

            if sub_choice == 0:
                break # GO back

            elif 1 <= sub_choice <= len(subject_list): # Make sure student input the correct choice
                subject = subject_list[sub_choice - 1] # Get the subject name with corresponding index

                # Print out the grade of the student with corresponding course
                print(f'\n[ {subject} ]')
                for sub_info in student_course[subject]:
                    for student in sub_info['students_enrolled']:
                        if student_data['student_id'] == student['student_id']:
                            print('--------------------------------------------------------------')
                            print(f"Course ID             : {sub_info['course_id']}")
                            print(f"Course Assignment     : {sub_info['course_assignment']}")
                            print(f"Assignment Submission : {student['assignment_submission']}")
                            print(f'Assignment Grade      : {student['assignment_grade']}')
                            print(f'Exam Grade            : {student['exam_grade']}')
                            print(f'Feedback              : {student['feedback']}')

            else:
                print('Invalid choice!')

        except ValueError:
            print('Invalid choice!')