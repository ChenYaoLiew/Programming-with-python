# Course Creation and Management
# Create and update courses, including lesson plans, assignments, and schedules

def manage_course_teach():
    while True:
        print("\nWelcome to Course Creation and Management\n'1' - Create Course\n'2' - Update Course\n'3' - Delete Course\n'4' - View Courses\n'5' - Add Course Material\n'6' - Back")

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
            from Teacher.course_material import add_course_material
            add_course_material()
        elif choice == '6':
            return
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
