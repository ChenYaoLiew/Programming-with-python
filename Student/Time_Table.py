from function.query import fetch_data
import ast

def time_table_list(course):
    data_list = ast.literal_eval(course["course_timetable"])
    return data_list

def time_table(student_info):
    course_data = fetch_data('data/course_data.txt')
    for course in course_data:
        if student_info[1]['student_id'] in course["students_enrolled"]:
            print('-----------------------------------------------------------')
            print(f'Course ID: {course["course_id"]}\n'
                  f'Course Title: {course["course_title"]}\n'
                  f'Course Description: {course["course_description"]}\n'
                  f'Time Table:')
            for index, time in enumerate(time_table_list(course), start= 1):
                print(f'Class [ {index} ]\n'
                      f'Class teacher: {time['course_teacher']}\n'
                      f'Time Start: {time['time_start']}\n'
                      f'Time End: {time['time_end']}')
            print('-----------------------------------------------------------')



