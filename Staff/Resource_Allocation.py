import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from function.query import *

def read_resource_file():
    """
    Read and return all resource records from the resource data file.
    
    This function retrieves all resource records stored in the resource_data.txt file
    using the fetch_data utility function.
    
    Parameters:
        None
        
    Returns:
        list: A list of dictionaries containing resource records
    """
    # Read and return all resource records from file, Returns list of resource dictionaries
    resource_list = fetch_data("data/resource_data.txt")
    return resource_list

def generate_resource_id(existing_ids):
    """
    Generate a new resource ID in format RESXXXX
    
    Parameters:
        existing_ids (list): List of existing resource IDs
        
    Returns:
        str: New unique resource ID
    """
    max_num = 0
    for id in existing_ids:
        if id.startswith("RES"):
            try:
                num = int(id[3:])
                max_num = max(max_num, num)
            except ValueError:
                continue
    
    new_num = max_num + 1
    return f"RES{new_num:04d}"

def register_resource(resource_id, resource_name, amount, status, amend_date_start, amend_date_end, amend_for):
    """
    Register a new resource in the system.
    
    This function validates the resource information, checks for duplicates,
    and adds the new resource to the resource data file.
    
    Parameters:
        resource_id (str): Unique identifier for the resource
        resource_name (str): Name of the resource
        amount (int): Quantity of the resource available
        status (bool): Availability status of the resource
        amend_date_start (str): Start date for resource amendment
        amend_date_end (str): End date for resource amendment
        amend_for (str): Purpose of resource amendment
        
    Returns:
        bool: True if registration successful, False otherwise
    """
    success = False
    
    # Check if the resource already exists in the resource list
    resource = fetch_data("data/resource_data.txt")
    
    # Validate inputs
    if not resource_id or not resource_name or not amount:
        print("Resource ID, name, and amount are required!")
        return False
    
    try:
        # Ensure amount is a valid number
        amount = int(amount)
    except ValueError:
        print("Amount must be a valid number!")
        return False

    # Check for duplicate resource_id
    for data in resource:
        if resource_id == data["resource_id"]:
            print("Resource already exists, Please try another resource_id!")
            return False

    # Add the new resource to resource_data.txt
    new_resource = {
        "resource_id": resource_id,
        "resource_name": resource_name,
        "amount": amount,
        "status": str(status).capitalize(),  # Ensure boolean is saved as "True" or "False"
        "amend_date_start": amend_date_start,
        "amend_date_end": amend_date_end,
        "amend_for": amend_for
    }
    resource.append(new_resource)

    # Save the file
    if insert_data("data/resource_data.txt", resource):
        print(f"Resource for {resource_name} successfully registered.")
        print(f"Your resource ID is: {resource_id}")
        success = True
    else:
        print("Error registering resource. Please try again.")
        
    return success

def validate_resource_id(resource_id, resource_list):
    """
    Check if a resource ID exists in the resource records.
    
    Parameters:
        resource_id (str): The resource ID to validate
        resource_list (list): List of resource dictionaries to check against
        
    Returns:
        tuple: (bool, dict) - Boolean indicating if ID exists and the resource data if found
    """
    # Check if resource_id exists in records
    for resource in resource_list:
        if resource['resource_id'] == resource_id:
            return True, resource
    return False, None

def validate_resource_name(resource_name, resource_list):
    """
    Check if a resource name exists in the resource records.
    
    Parameters:
        resource_name (str): The resource name to validate
        resource_list (list): List of resource dictionaries to check against
        
    Returns:
        tuple: (bool, dict) - Boolean indicating if name exists and the resource data if found
    """
    # Check if resource_name exists in records
    for resource in resource_list:
        if resource['resource_name'] == resource_name:
            return True, resource
    return False, None

def update_resource_record(resource_list):
    """
    Update resource records in the file using the query functions
    
    Parameters:
        resource_list (list): List of resource dictionaries to update
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Convert all amount values to int and ensure status is properly capitalized
        for resource in resource_list:
            resource['amount'] = int(resource['amount'])
            if isinstance(resource['status'], bool):
                resource['status'] = str(resource['status']).capitalize()
            
        # Use insert_data function to write the updated list
        success = insert_data("data/resource_data.txt", resource_list)
        
        if success:
            print("resource records updated successfully.")
            return True
        else:
            print("Error updating resource records.")
            return False
    except Exception as e:
        print(f"Error updating resource records: {e}")
        return False

def view_resource():
    """
    Display all resources with their details.
    
    This function retrieves all resource records and prints each resource's
    ID, name, amount, status, and amendment information.
    
    Parameters:
        None
        
    Returns:
        None
    """
    resource_list = read_resource_file()
    for resource in resource_list:
        print(f"Resource ID: {resource['resource_id']}, Resource Name: {resource['resource_name']}, Amount: {resource['amount']}, Status: {resource['status']}, Amend Date Start: {resource['amend_date_start']}, Amend Date End: {resource['amend_date_end']}, Amend For: {resource['amend_for']}")
        print("-" * 80)  # Add a separator line between resources

def manage_resource():
    """
    Manage a specific resource by updating its usage information.
    
    This function allows a resource to be marked as unavailable and
    updates its amendment information including usage purpose and dates.
    
    Parameters:
        None
        
    Returns:
        None
    """
    resource_id = input("Enter resource_id: ")
    # Use fetch_data from query.py
    resource_list = fetch_data("data/resource_data.txt")
    found = False

    for data in resource_list:
        if data["resource_id"] == resource_id:
            found = True
            # Convert string "False"/"True" to boolean
            if str(data["status"]).lower() == "false":
                print(f"{data['resource_id']}, {data['resource_name']} is currently unavailable")
                return
            
            amend_for = input("Enter the usage for this resource: ")
            amend_date_start = input("Enter the start date: ")
            amend_date_end = input("Enter the end date: ")
            
            # Update the data
            data["amend_for"] = amend_for
            data["amend_date_start"] = amend_date_start
            data["amend_date_end"] = amend_date_end
            data["status"] = str(False).capitalize()  # Store as "False" with capital F
            
            # Use insert_data from query.py to save the changes
            if insert_data("data/resource_data.txt", resource_list):
                print("Resource updated successfully!")
            else:
                print("Error updating resource!")
            return

    if not found:
        print("Resource not found!")

def add_resource():
    """
    Add a new resource to the system.
    
    This function prompts for resource information, generates a new
    resource ID, and registers the resource in the system.
    
    Parameters:
        None
        
    Returns:
        None
    """
    resource_name = input("Enter resource_name: ")
    amount = input("Enter amount: ")
    
    # Get existing resource list to generate new ID
    resource_list = read_resource_file()
    existing_ids = [data.get("resource_id", "RES0000") for data in resource_list]
    resource_id = generate_resource_id(existing_ids)
    
    # Set empty strings for amend dates and amend_for
    amend_date_start = "None"
    amend_date_end = "None"
    amend_for = "None"
    status = str(True).capitalize()  # Default status is False for new resources

    # Try to register the resource
    register_resource(resource_id, resource_name, amount, status, amend_date_start, amend_date_end, amend_for)

def view_resource_by_id():
    """
    Display detailed information for a specific resource by ID.
    
    This function prompts for a resource ID and displays all information
    for that specific resource if found.
    
    Parameters:
        None
        
    Returns:
        None
    """
    resource_id = input("Enter resource_id: ")
    resource_list = read_resource_file()
    found = False

    for resource in resource_list:
        if resource["resource_id"] == resource_id:
            found = True
            print("\nResource Details:")
            print("-" * 50)
            print(f"Resource ID: {resource['resource_id']}")
            print(f"Resource Name: {resource['resource_name']}")
            print(f"Amount: {resource['amount']}")
            print(f"Status: {'Available' if resource['status'] else 'Unavailable'}")
            print(f"Amend Date Start: {resource['amend_date_start']}")
            print(f"Amend Date End: {resource['amend_date_end']}")
            print(f"Amend For: {resource['amend_for']}")
            print("-" * 50)
            break

    if not found:
        print("Resource not found!")

def update_resource():
    """
    Update information for an existing resource.
    
    This function allows updating a resource's name, amount, or status.
    When status is changed to available, amendment data is cleared.
    
    Parameters:
        None
        
    Returns:
        None
    """
    resource_id = input("Enter resource_id to update: ")
    resource_list = read_resource_file()
    found = False

    for data in resource_list:
        if data["resource_id"] == resource_id:
            found = True
            print("\nWhat would you like to update?")
            print("'1' - Update Resource Name")
            print("'2' - Update Amount")
            print("'3' - Update Status")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                new_resource_name = input("Enter new resource_name: ")
                # Check if new resource_name already exists
                if any(acc["resource_name"] == new_resource_name for acc in resource_list):
                    print("resource_name already exists. Please try another.")
                    return
                data["resource_name"] = new_resource_name
                print("resource_name updated successfully!")
                
            elif choice == "2":
                new_amount = input("Enter new amount: ")
                data["amount"] = new_amount
                print("Amount updated successfully!")
                
            elif choice == "3":
                current_status = data["status"]
                if current_status:  # If True (Available)
                    print("\nCurrent status: Unavailable")
                    print("1 - Set to Available")
                    if input("Enter 1 to change status: ") == "1":
                        data["status"] = str(True).capitalize()  # Store as "True" with capital T
                        # Clear amendment data
                        data["amend_date_start"] = "None"
                        data["amend_date_end"] = "None"
                        data["amend_for"] = "None"
                        print("Status updated to Available and amendment data cleared!")

                else:  # If False (Unavailable)
                    print("\nCurrent status: Available")
                    print("1 - Set to Unavailable")
                    if input("Enter 1 to change status: ") == "1":
                        data["status"] = str(False).capitalize()  # Store as "False" with capital F
                        print("Status updated to Unavailable!")

                
            else:
                print("Invalid choice!")
                return
            
            # Save the updated accounts list
            if insert_data("data/resource_data.txt", resource_list):
                print(f"Resource for {resource_id} has been updated successfully.")
            else:
                print("Error saving updates. Please try again.")
            break
    
    if not found:
        print(f"Resource with resource_id {resource_id} not found!")

def delete_resource():
    """
    Delete a resource from the system.
    
    This function removes a resource from the resource data file
    based on the provided resource ID.
    
    Parameters:
        None
        
    Returns:
        None
    """
    resource_id = input("Enter resource_id: ")
    resource_list = read_resource_file()
    found = False

    # Create new list without the resource to be deleted
    updated_resources = []
    for resource in resource_list:
        if resource["resource_id"] == resource_id:
            found = True
        else:
            updated_resources.append(resource)
    
    if found:
        if insert_data("data/resource_data.txt", updated_resources):
            print(f"Resource {resource_id} has been deleted successfully.")
        else:
            print("Error deleting resource. Please try again.")
    else:
        print(f"Resource with resource_id {resource_id} not found!")

def manage_resource_allocation_main():
    while True:
        print("\nResource Allocation Management")
        print("'1' - View All Resources")
        print("'2' - View Resource by ID")
        print("'3' - Manage Resource")
        print("'4' - Add Resource")
        print("'5' - Update Resource")
        print("'6' - Delete Resource")
        print("'7' - Back")

        choice = input("\nEnter your choice (1-7): ")

        if choice == '1':
            view_resource()
        elif choice == '2':
            view_resource_by_id()
        elif choice == '3':
            manage_resource()
        elif choice == '4':
            add_resource()
        elif choice == '5':
            update_resource()
        elif choice == '6':
            delete_resource()
        elif choice == '7':
            from Staff.Menu import staff_user_page
            staff_user_page()
        else:
            print("Invalid choice. Please try again.")
            continue