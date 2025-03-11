from Student.Student_function import update_student_data

def feedback_sub(student_info):
    """
    To display grades tracking menu
    Args:
        student_info(list): ["Index of the student in data_list"(int), "data of the student(one student only)"(dict)]
    return:
        Bool: If student update feedback, it will return True
    """
    student_data = student_info[1]
    index_in_list = student_info[0]

    while True:
        feedback = input('Type your feedback here(Press 0 to Back): ')
        if feedback == '0':
            return False
        else:
            student_data['feedback'] = feedback
            update_student_data(index_in_list, student_data)
            return True
