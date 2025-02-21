from Administrator.menu import administrator_user_page
from function.query import *

def createCourse():
    prompt1 = input("")
    data = fetch_data('.\data\course_data.txt')


def manageCourse():
    print("'1' - Create Course\n'2' - Update Course\n'3' - Delete Course\n'4' - Back")

    choice = input("Enter your choice: ")
    if choice == '1':
        createCourse()
    elif choice == '2':
        updateCourse()
    elif choice == '3':
        deleteCourse()
    elif choice == '4':
        administrator_user_page()