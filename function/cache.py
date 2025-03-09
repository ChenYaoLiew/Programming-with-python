cache_student_id = None

def get_student_id():
    global cache_student_id
    return cache_student_id

def set_student_id(student_id):
    global cache_student_id
    cache_student_id = student_id