from function.query import *

def assignment_sub(student_info):
    """
    Used when student need to check their assignment status
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
    Returns:
        bool: if True means assignment update successfully, else notting changes.
    """

    changes = False     # if student updated any assignment, it will be True
    student_course_data = fetch_data("data/student_data.txt")  # Get all the student's course data in a list format

    # loop through all students in the list and display student course data when student id matches
    for index, student in enumerate(student_course_data):
        if student_info[1]['student_id'] == student['student_id']: # if student id matches, display all the course data

            while True:
                print(f'\nMath assignment submission    (Press 1 to upload): {student["math_assignment"]}')
                print(f'Science assignment submission (Press 2 to upload): {student["science_assignment"]}')
                print(f'English assignment submission (Press 3 to upload): {student["english_assignment"]}')
                print('Press 0 save changes and go Back')

                choice = input('Enter your choice: ')

                if choice == '1':
                    assignment = input('Input your Math assignment here (Press 0 to Back): ')

                    if assignment == '0':
                        continue
                    else:
                        # change the student course data inside the list
                        student_course_data[index]["math_assignment"] = assignment
                        print('Assignment uploaded')
                        changes = True
                        continue

                elif choice == '2':
                    assignment = input('Input your Science assignment here (Press 0 to Back): ')

                    if assignment == '0':
                        continue
                    else:
                        # change the student course data inside the list
                        student_course_data[index]["science_assignment"] = assignment
                        print('Assignment uploaded')
                        changes = True
                        continue

                elif choice == '3':
                    assignment = input('Input your English assignment here (Press 0 to Back): ')

                    if assignment == '0':
                        continue
                    else:
                        # change the student course data inside the list
                        student_course_data[index]["english_assignment"] = assignment
                        print('Assignment uploaded')
                        changes = True
                        continue

                elif choice == '0':
                    # if student got change any data, it will overwrite the new data inside course_data.txt
                    if changes:
                        insert_data('data/student_data.txt', student_course_data)
                    return changes

                else:
                    print('Invalid choice!')