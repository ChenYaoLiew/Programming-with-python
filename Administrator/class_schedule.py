from function.query import *

def check_time_collision(time1_start, time1_end, time2_start, time2_end):
    """
    Check if two time slots overlap.
    
    This function compares two time periods and determines if they have any
    overlap. It converts time strings to datetime objects for comparison.
    
    Parameters:
        time1_start (str): Start time of first slot (format: "HH:MM AM/PM")
        time1_end (str): End time of first slot (format: "HH:MM AM/PM")
        time2_start (str): Start time of second slot (format: "HH:MM AM/PM")
        time2_end (str): End time of second slot (format: "HH:MM AM/PM")
        
    Returns:
        bool: True if times overlap, False otherwise
    """
    from datetime import datetime
    
    # Convert time strings to datetime objects for comparison
    time_format = "%I:%M %p"  # Format: "HH:MM AM/PM"
    t1_start = datetime.strptime(time1_start, time_format)
    t1_end = datetime.strptime(time1_end, time_format)
    t2_start = datetime.strptime(time2_start, time_format)
    t2_end = datetime.strptime(time2_end, time_format)
    
    return (t1_start < t2_end) and (t2_start < t1_end)

def view_class_schedule():
    """
    View and check for time collisions within class schedules.
    
    This function displays the current class schedule for all courses
    and identifies any scheduling conflicts where the same teacher is
    assigned to multiple classes at overlapping times. When conflicts
    are detected, it offers options to resolve them.
    
    Parameters:
        None
        
    Returns:
        None
    """
    courses_data = fetch_data("data/course_data.txt")
    
    if not courses_data:
        print("\nNo courses found in the system.")
        return
        
    print("\nChecking class schedules for time conflicts...")
    print("=" * 60)
    
    found_any_collision = False
    
    # Check each course for internal time collisions
    for course in courses_data:
        timetable = course.get('course_timetable', [])
        collisions = []
        
        # Compare each time slot with others in the same course
        for i, slot1 in enumerate(timetable):
            for slot2 in timetable[i+1:]:
                # Check if same teacher and times overlap
                if (slot1['course_teacher'] == slot2['course_teacher'] and 
                    check_time_collision(slot1['time_start'], slot1['time_end'],
                                      slot2['time_start'], slot2['time_end'])):
                    collisions.append((slot1, slot2))
        
        # If collisions found in this course, display and offer to fix
        if collisions:
            found_any_collision = True
            print(f"\nWARNING: Time Collisions Detected in {course['course_title']} ({course['course_id']})")
            print("=" * 60)
            print(f"Teacher {collisions[0][0]['course_teacher']} is scheduled for multiple classes at overlapping times:")
            
            for slot1, slot2 in collisions:
                print(f"\nCollision between:")
                print(f"1. Class Time: {slot1['time_start']} - {slot1['time_end']}")
                print(f"2. Class Time: {slot2['time_start']} - {slot2['time_end']}")
                
                # Ask to resolve collision
                print("\nWould you like to change one of these time slots?")
                choice = input("Enter 1 or 2 to change respective slot (or 0 to skip): ")
                
                if choice in ['1', '2']:
                    # Call update_course_timetable to modify the slot
                    from Administrator.course_management import update_course_timetable
                    print(f"\nUpdating schedule for {course['course_title']}")
                    update_course_timetable()
        
        # Display current schedule for the course
        print(f"\nCurrent Schedule for {course['course_title']} ({course['course_id']}):")
        print("-" * 40)
        if timetable:
            for slot in timetable:
                print(f"Teacher: {slot['course_teacher']}")
                print(f"Time: {slot['time_start']} - {slot['time_end']}")
                print("-" * 20)
        else:
            print("No classes scheduled for this course.")
    
    if not found_any_collision:
        print("\nNo time conflicts found in any course schedules.")
        print("All class schedules are properly arranged.")

def class_schedule_menu():
    """
    Display the class schedule management menu.
    
    This function presents options for viewing class schedules
    or returning to the previous menu.
    
    Parameters:
        None
        
    Returns:
        None
    """
    while True:
        print("\n'1' - View Class Schedule\n'2' - Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_class_schedule()
        elif choice == '2':
            break