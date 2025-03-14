import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from function.query import *
# event Management: Create, update, or delete event offerings and assign instructors to events. 

def read_event_file():
    """
    Read and return all event records from the event data file.
    
    This function retrieves all event records stored in the event_data.txt file
    using the fetch_data utility function.
    
    Parameters:
        None
        
    Returns:
        list: A list of dictionaries containing event records
    """
    # Read and return all event records from file, Returns list of event dictionaries
    event_list = fetch_data("data/event_data.txt")
    return event_list

def read_student_file():
    """
    Read and return all student records from the student data file.
    
    This function retrieves all student records stored in the student_data.txt file
    using the fetch_data utility function.
    
    Parameters:
        None
        
    Returns:
        list: A list of dictionaries containing student records
    """
    # Read and return all student records from file, Returns list of student dictionaries
    student_list = fetch_data("data/student_data.txt")
    return student_list

def generate_event_id(existing_ids):
    """
    Generate a new event ID in format EVEXXXX
    
    Parameters:
        existing_ids (list): List of existing event IDs
        
    Returns:
        str: New unique event ID
    """
    max_num = 0
    for id in existing_ids:
        if id.startswith("EVEX"):
            try:
                num = int(id[4:])
                max_num = max(max_num, num)
            except ValueError:
                continue
    
    new_num = max_num + 1
    return f"EVEX{new_num:04d}"

def register_event(event_id, event_title, event_description, students_enrolled, event_time):
    """
    Register a new event
    
    Parameters:
        event_id (str): Unique event ID
        event_title (str): Event title
        event_description (str): Event description
        students_enrolled (list): List of enrolled student IDs
        event_time (str): Event time
        
    Returns:
        bool: True if successful, False otherwise
    """
    success = False
    
    # Check if the event already exists
    event = fetch_data("data/event_data.txt")
    
    # Validate inputs
    if not all([event_id, event_title, event_description, students_enrolled, event_time]):
        print("All fields are required!")
        return False

    # Check for duplicate event_id
    for data in event:
        if event_id == data["event_id"]:
            print("Event already exists, Please try another event_id!")
            return False    

    # Add the new event
    new_event = {
        "event_id": event_id,
        "event_title": event_title,
        "event_description": event_description,
        "students_enrolled": students_enrolled,  # This is now a list
        "event_time": event_time
    }
    event.append(new_event)

    # Save the file
    if insert_data("data/event_data.txt", event):
        print(f"Event '{event_title}' successfully registered.")
        print(f"Event ID: {event_id}")
        print(f"Enrolled students: {', '.join(students_enrolled)}")
        success = True
    else:
        print("Error registering event. Please try again.")
        
    return success

def validate_event_id(event_id, event_list):
    """
    Check if an event ID exists in the event records.
    
    Parameters:
        event_id (str): The event ID to validate
        event_list (list): List of event dictionaries to check against
        
    Returns:
        tuple: (bool, dict) - Boolean indicating if ID exists and the event data if found
    """
    # Check if event_id exists in records
    for event in event_list:
        if event['event_id'] == event_id:
            return True, event
    return False, None

def validate_event_title(event_title, event_list):
    """
    Check if an event title exists in the event records.
    
    Parameters:
        event_title (str): The event title to validate
        event_list (list): List of event dictionaries to check against
        
    Returns:
        tuple: (bool, dict) - Boolean indicating if title exists and the event data if found
    """
    # Check if event_title exists in records
    for event in event_list:
        if event['event_title'] == event_title:
            return True, event
    return False, None

def update_event_record(event_list):
    """
    Update event records in the file using the query functions
    
    Parameters:
        event_list (list): List of event dictionaries to update
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Convert all amount value  
        for event in event_list:
            event['event_time'] = int(event['event_time'])
            
        # Use insert_data function to write the updated list
        success = insert_data("data/event_data.txt", event_list)
        
        if success:
            print("event records updated successfully.")
            return True
        else:
            print("Error updating event records.")
            return False
    except Exception as e:
        print(f"Error updating event records: {e}")
        return False

def view_event():
    """
    Display all events with enrolled students.
    
    This function retrieves all event records and prints each event's
    ID, title, description, time, and list of enrolled students.
    
    Parameters:
        None
        
    Returns:
        None
    """
    event_list = read_event_file()
    print("-" * 100)
    for event in event_list:
        print(f"\nEvent ID: {event['event_id']}")
        print(f"Title: {event['event_title']}")
        print(f"Description: {event['event_description']}")
        print(f"Event Time: {event['event_time']}")
        print(f"Enrolled Students: {', '.join(event['students_enrolled'])}")
        print("-" * 100)

def add_event():
    """
    Add a new event with multiple student enrollments.
    
    This function prompts for event information, generates a new
    event ID, and allows adding multiple students to the event.
    It validates student IDs against existing records before enrollment.
    
    Parameters:
        None
        
    Returns:
        None
    """
    event_title = input("Enter event title: ")
    event_description = input("Enter event description: ")
    event_time = input("Enter event time: ")
    
    # Get existing event list to generate new ID
    event_list = read_event_file()
    existing_ids = [data.get("event_id", "EVEX0000") for data in event_list]
    event_id = generate_event_id(existing_ids)
    
    # Handle multiple student enrollments
    students_enrolled = []
    while True:
        print("\nCurrent enrolled students:", students_enrolled)
        print("Options:")
        print("1. Add student")
        print("2. Finish adding students")
        print("3. Quit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            student_id = input("Enter student ID (e.g., STD0003): ").strip()
            
            # Validate student ID against user_data.txt
            users = fetch_data("data/user_data.txt")
            valid_student = False
            
            for user in users:
                if (user.get("student_id") == student_id and 
                    user.get("account_type") == "student"):
                    valid_student = True
                    if student_id not in students_enrolled:
                        students_enrolled.append(student_id)
                        print(f"Student {student_id} added successfully.")
                    else:
                        print("This student is already enrolled.")
                    break
            
            if not valid_student:
                print("Invalid student ID or not a student account.")
                
        elif choice == '2':
            if not students_enrolled:
                print("Error: At least one student must be enrolled.")
                continue
            break
        elif choice == '3':
            return
        else:
            print("Invalid choice. Please try again.")
    
    # Register the event with the list of enrolled students
    register_event(
        event_id=event_id,
        event_title=event_title,
        event_description=event_description,
        students_enrolled=students_enrolled,  # Now this is a list of student IDs
        event_time=event_time
    )

def change_event_title():
    """
    Update the title of an existing event.
    
    This function prompts for an event ID and a new title,
    then updates the event record if the ID is found.
    
    Parameters:
        None
        
    Returns:
        None
    """
    event_list = read_event_file()
    found = False

    prompt1 = input("Enter event id: ")

    for data in event_list:
        if data['event_id'] == prompt1:
            found = True
            prompt2 = input("Enter new name: ")
            data["event_title"] = prompt2  # Update the course in the list
            break

    if found:
        if insert_data("data/event_data.txt", event_list):  # Consistent path format
            print(f"Event title updated successfully.")
        else:
            print("Error updating event title.")
    else:
        print("Invalid event")

def change_event_description():
    """
    Update the description of an existing event.
    
    This function prompts for an event ID and a new description,
    then updates the event record if the ID is found.
    
    Parameters:
        None
        
    Returns:
        None
    """
    event_list = read_event_file()
    found = False

    prompt1 = input("Enter course id: ")

    for data in event_list:
        if data['event_id'] == prompt1:
            found = True
            prompt2 = input("Enter new description: ")
            data["event_description"] = prompt2  # Update the course description
            break

    if found:
        if insert_data("data/event_data.txt", event_list):
            print(f"Event description updated successfully.")
        else:
            print("Error updating event description.")
    else:
        print("Invalid event")

def update_event():
    """
    Present a menu for updating event information.
    
    This function displays options for changing an event's title,
    description, or viewing the event timetable.
    
    Parameters:
        None
        
    Returns:
        None
    """
    print("\n'1' - Change event title\n'2' - Change event description\n'3' - View event timetable")
    choice = input("Enter your choice: ")

    if choice == '1':
        change_event_title()
    elif choice == '2':
        change_event_description()
    elif choice == '3':
        view_event()
    else:
        print("Invalid choice")

def delete_event():
    """
    Delete an event from the system.
    
    This function prompts for an event ID and removes the event
    from the event data file if the ID is found.
    
    Parameters:
        None
        
    Returns:
        None
    """
    event_list = read_event_file()
    event_id = input("Enter want to delete event id: ")
    for data in event_list:
        if data['event_id'] == event_id:
            event_list.remove(data)
            if insert_data("data/event_data.txt", event_list):
                print("Event deleted successfully.")
            else:
                print("Error deleting event.")
            break
    else:
        print("Event not found.")

def event_management_main():
    while True:
        print("\nEvent Management")
        print("1. Add Event")
        print("2. Manage Event")
        print("3. Delete Event")
        print("4. View Events")
        print("5. Back")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_event()
        elif choice == '2':
            update_event()
        elif choice == '3':
            delete_event()
        elif choice == '4':
            view_event()
        elif choice == '5':
            from Staff.Menu import staff_user_page
            staff_user_page()
        else:
            print("Invalid choice")