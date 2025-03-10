import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from function.query import *

def read_resource_file():
    # Read and return all resource records from file, Returns list of resource dictionaries
    resource_list = fetch_data("data/resource_data.txt")
    return resource_list

def generate_resource_id(existing_ids):
    """
    Generate a new resource ID in format RESXXXX
    Args:
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
        "status": status,  # Now using boolean value
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
    # Check if resource_id exists in records
    for resource in resource_list:
        if resource['resource_id'] == resource_id:
            return True, resource
    return False, None

def validate_resource_name(resource_name, resource_list):
    # Check if resource_name exists in records
    for resource in resource_list:
        if resource['resource_name'] == resource_name:
            return True, resource
    return False, None

def update_resource_record(resource_list):
    """
    Update resource records in the file using the query functions
    Args:
        resource_list (list): List of resource dictionaries to update
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Convert all amount values to int before saving
        for resource in resource_list:
            resource['amount'] = int(resource['amount'])
            
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
    resource_list = read_resource_file()
    for resource in resource_list:
        print(f"Resource ID: {resource['resource_id']}, Resource Name: {resource['resource_name']}, Amount: {resource['amount']}, Status: {resource['status']}, Amend Date Start: {resource['amend_date_start']}, Amend Date End: {resource['amend_date_end']}, Amend For: {resource['amend_for']}")
        print("-" * 100)  # Add a separator line between resources

def manage_resource():
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
            data["status"] = False
            
            # Use insert_data from query.py to save the changes
            if insert_data("data/resource_data.txt", resource_list):
                print("Resource updated successfully!")
            else:
                print("Error updating resource!")
            return

    if not found:
        print("Resource not found!")

def add_resource():
    resource_name = input("Enter resource_name: ")
    amount = input("Enter amount: ")
    
    # Get existing resource list to generate new ID
    resource_list = read_resource_file()
    existing_ids = [data.get("resource_id", "RES0000") for data in resource_list]
    resource_id = generate_resource_id(existing_ids)
    
    # Set empty strings for amend dates and amend_for
    amend_date_start = ""
    amend_date_end = ""
    amend_for = ""
    status = False  # Default status is False for new resources

    # Try to register the resource
    register_resource(resource_id, resource_name, amount, status, amend_date_start, amend_date_end, amend_for)

def view_resource_by_id():
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
    resource_id = input("Enter resource_id to update: ")
    resource_list = read_resource_file()
    found = False

    for data in resource_list:
        if data["resource_id"] == resource_id:
            found = True
            print("\nWhat would you like to update?")
            print("1 - Update Resource Name")
            print("2 - Update Amount")
            print("3 - Update Status")
            
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
                    print("\nCurrent status: Available")
                    print("1 - Set to Unavailable")
                    if input("Enter 1 to change status: ") == "1":
                        data["status"] = False
                        print("Status updated to Unavailable!")
                else:  # If False (Unavailable)
                    print("\nCurrent status: Unavailable")
                    print("1 - Set to Available")
                    if input("Enter 1 to change status: ") == "1":
                        data["status"] = True
                        # Clear amendment data
                        data["amend_date_start"] = ""
                        data["amend_date_end"] = ""
                        data["amend_for"] = ""
                        print("Status updated to Available and amendment data cleared!")
                
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
        print("1. View All Resources")
        print("2. View Resource by ID")
        print("3. Manage Resource")
        print("4. Add Resource")
        print("5. Update Resource")
        print("6. Delete Resource")
        print("7. Back")

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

manage_resource_allocation_main()