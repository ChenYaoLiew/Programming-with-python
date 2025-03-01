from function.query import fetch_data
import ast

def time_table_list(course):
    data_list = ast.literal_eval(course['course_timetable']) # to convert string data to list format
    return data_list                                         # return list data

def time_table(student_info):
    have_course = False
    course_data = fetch_data('data/course_data.txt') # get the course data inside the txt file
    for course in course_data:
        if student_info[1]['student_id'] in course["students_enrolled"]:   # check whether student id inside course data
            print('-----------------------------------------------------------')
            print(f'Course ID: {course["course_id"]}\n'
                  f'Course Title: {course["course_title"]}\n'
                  f'Course Description: {course["course_description"]}\n'
                  f'Time Table:')
            for index, time in enumerate(time_table_list(course), start= 1):  # To loop the course_timetable list
                print(f'\nClass [ {index} ]\n'  
                      f'Class teacher: {time['course_teacher']}\n'
                      f'Time Start: {time['time_start']}\n'
                      f'Time End: {time['time_end']}')
            print('-----------------------------------------------------------')
            have_course = True
    return have_course

