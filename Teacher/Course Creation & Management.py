import os

def create_course():
    course_data = {} # Initialize an empty dictionary

    # Get course details of course name , code and schedule
    course_data["name"] = input("Create a course name: ")
    course_data["code"] = input("Enter course code: ")

    # Get Schedule Details
    print("Creating Course Schedule: ")
    course_data["schedule"] = []
    while True:
        entry = input("Enter a schedule entry or 'done' to finish (Example: Mon/Fri 9:00am-10:00am): ")
        if entry.lower() == "done":
            break
        course_data["schedule"].append(entry)

    # Get lesson plan details
    course_data["lesson_plan"] = {} # Nested dictionary for lesson plan inside course_data dictionary
    course_data["lesson_plan"]["title"] = input("Enter lesson title: ")
    course_data["lesson_plan"]["description"] = input("Enter lesson description: ")

    # Get Assignment details
    course_data["Assignment"] = {} # Nested dictionary for assignment inside course_data dictionary
    course_data["Assignment"]["title"] = input("Enter Assignment title: ")
    course_data["Assignment"]["description"] = input("Enter Assignment description: ")

    try:
        # Construct the file path
        teach_file_path = os.path.join("../data", "teacher_data.txt")
        with open(teach_file_path, "a") as f:
            #Enters the data into the teacher_data.txt file line by line
            f.write(f"Course Name: {course_data["name"]}\n")
            f.write(f"Course Code: {course_data["code"]}\n")
            f.write(f"Course Schedule: {course_data["schedule"]}\n")

            f.write(f"Lesson Plan: {course_data["lesson_plan"]["title"]}\n")
            f.write(f"Lesson description: {course_data["lesson_plan"]["description"]}\n")

            f.write(f"Assignment: {course_data["Assignment"]["title"]}\n")
            f.write(f"Assignment Description: {course_data["Assignment"]["description"]}\n")

            f.write("----------\n")
            print("Course added successfully!")


    except FileNotFoundError:
        print("Error creating course file ")
    except OSError as e:
        print(f"An error occurred: {e} ")

create_course()