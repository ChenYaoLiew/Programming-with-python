# Course Creation and Management
# Create and update courses, including lesson plans, assignments, and schedules

#  Student Management: Oversee student records, including viewing and updating personal details, enrollment status, and academic performance. 
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def manage_course_teach():
    while True:
        print("\nWelcome to Course Creation and Management\n1 - Create Course\n2 - Update Course\n3 - Delete Course\n4 - View Courses\n5 - Add Course Material\n6 - Back")
        try:
            choice = input("\nEnter Choice: ").strip()
            if not choice:  # Prevent empty input
                print("Input cannot be empty. Please enter a number.")
                continue

            choice = int(choice)

            if choice == 1:
                from Administrator.course_management import create_course
                create_course()
            elif choice == 2:
                from Administrator.course_management import update_course
                update_course()
            elif choice == 3:
                from Administrator.course_management import delete_course
                delete_course()
            elif choice == 4:
                from Administrator.course_management import view_courses
                view_courses()
            elif choice == 5:
                from Administrator.course_management import add_course_material
                add_course_material()
            elif choice == 6:
                from Teacher.menu import teacher_menu_page
                teacher_menu_page()
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

manage_course_teach()