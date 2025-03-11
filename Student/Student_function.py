def get_student_course_id(student_info, all_courses):
    """
    To get iterate out all the courses that student has and store the course_id in a subject list. Every Subject will initialise in a dictionary
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
        all_courses(list): A list of all courses data inside the txt file
    return:
        student_courses(Dict): A dictionary which contain student's every subject and corresponding course_id
    """
    student_data = student_info[1]
    student_courses = {'Math': [], 'Science': [], 'English': []}

    for course in all_courses:
        for student in course['students_enrolled']:
            # If student_id matching it will store the course_id in list
            if student['student_id'] == student_data['student_id']:
                student_courses[course['course_title']].append(course['course_id'])

    return student_courses

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