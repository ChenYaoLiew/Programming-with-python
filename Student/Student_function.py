def get_student_course_id(student_info, all_courses):
    """
        Get all the subjects and corresponding course information of the students
        Args:
            student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
            all_courses(list):  A list of all courses data
        Returns:
            student_courses(dict): A dictionary that contain all the student's subject and corresponding course
        """
    student_data = student_info[1]
    student_courses = {}

    # Use for loop to check all the course one by one
    for course in all_courses:
        # Check if student's ID in the course data
        if any(student_data['student_id'] == student['student_id'] for student in course['students_enrolled']):
            if course['course_title'] not in student_courses: # Add subject into student_courses
                student_courses[course['course_title']] = []
            student_courses[course['course_title']].append(course) # Insert the course into corresponding subject

    return student_courses

def display_subject_menu(student_course, menu_title):
    """
        Display all the subject of the student, student can choose what subject they want to interact like a menu
        Args:
            student_course(list): A dictionary that contain all the student's subject and corresponding course
            menu_title(str):  the title of the Page
        Returns:
            have_course(bool): if student has any subject that is already enrolled it will return True
    """
    have_course = False

    print(f'\n[ {menu_title} ]')
    if student_course:
        have_course = True

        # Print out all the subject that student can choose
        for index, subject in enumerate(student_course, start=1):
            print(f'{index} - {subject}')
        print('0 - Back') # Print a Back option for student back to main page

    return have_course

def update_student_data(index_in_list, student_data):
    """
    To update new student data into user_data.txt file
    Args:
        index_in_list(int): The index of the student in the data
        student_data(dict): A dictionary that contain all the info of the student
    return:
        None
    """
    from function.query import fetch_data
    from function.query import insert_data
    accounts = fetch_data("data/user_data.txt") # get all the account of the user in a list
    accounts[index_in_list] = student_data # insert the updated student data dictionary to user list
    insert_data("data/user_data.txt", accounts) # save it to the database