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

def update_collision_slot(course, slot_to_update):
    """
    Update a specific time slot causing a collision.
    
    This function modifies the start and end times of a specific time slot
    to resolve a scheduling collision.
    
    Parameters:
        course (dict): The course containing the time slot to update
        slot_to_update (dict): The specific time slot to modify
        
    Returns:
        bool: True if the update was successful, False otherwise
    """
    print(f"\nUpdating time slot for class {slot_to_update['class_id']}")
    print(f"Current time: {slot_to_update['time_start']} - {slot_to_update['time_end']}")
    
    # Get new time slot values
    new_time_start = input("Enter new start time (e.g., 9:00 AM): ")
    new_time_end = input("Enter new end time (e.g., 12:00 PM): ")
    
    # Update the slot in the course's timetable
    for slot in course['course_timetable']:
        if slot['class_id'] == slot_to_update['class_id']:
            slot['time_start'] = new_time_start
            slot['time_end'] = new_time_end
            
    # Save the updated course data
    courses_data = fetch_data("data/course_data.txt")
    for i, c in enumerate(courses_data):
        if c['course_id'] == course['course_id']:
            courses_data[i] = course
            
    if insert_data("data/course_data.txt", courses_data):
        print("Time slot updated successfully.")
        return True
    else:
        print("Error updating time slot.")
        return False

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
                
                if choice == '1':
                    if update_collision_slot(course, slot1):
                        print("Schedule conflict resolved.")
                elif choice == '2':
                    if update_collision_slot(course, slot2):
                        print("Schedule conflict resolved.")
        
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
            return