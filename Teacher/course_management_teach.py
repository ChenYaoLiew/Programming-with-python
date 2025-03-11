# Course Creation and Management
# Create and update courses, including lesson plans, assignments, and schedules

def manage_course_teach():
    while True:
        print("\nWelcome to Course Creation and Management\n1 - Create Course\n2 - Update Course\n3 - Delete Course\n4 - View Courses\n5 - Add Course Material\n6 - Back")

        choice = input("\nEnter Choice: ").strip()

        if choice == '1':
            from Administrator.course_management import create_course
            create_course()
        elif choice == '2':
            from Administrator.course_management import update_course
            update_course()
        elif choice == '3':
            from Administrator.course_management import delete_course
            delete_course()
        elif choice == '4':
            from Administrator.course_management import view_courses
            view_courses()
        elif choice == '5':
            from course_material import add_course_material
            add_course_material()
        elif choice == '6':
            from Teacher.menu import teacher_menu_page
            teacher_menu_page()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
