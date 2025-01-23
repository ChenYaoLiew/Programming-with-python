def create_course():
 # Initialize an empty dictionary
    course_name = input("Create a course name: ")
    course_code = int(input("Enter course code: "))
    schedule = input("Enter course schedule: ")

    try:
        # Construct the file path
        teach_file_path = "data/teacher_data.txt"

        with open(teach_file_path, "a") as f:
            f.write(f"Course Name: {course_name}\n")
            f.write(f"Course Code: {course_code}\n")
            f.write(f"Schedule: {schedule}\n")

    except FileNotFoundError:
        print("Error creating course file ")
    except OSError as e:
        print(f"An error occurred: {e} ")

create_course()



