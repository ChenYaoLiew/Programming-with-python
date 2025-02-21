from function.query import *

def generate_student_id(existing_ids):
    """
    Generate a new student ID in format STDXXXX
    Args:
        existing_ids (list): List of existing student IDs
    Returns:
        str: New unique student ID
    """
    max_num = 0
    for id in existing_ids:
        if id.startswith("STD"):
            try:
                num = int(id[3:])
                max_num = max(max_num, num)
            except ValueError:
                continue
    
    new_num = max_num + 1
    return f"STD{new_num:04d}"

def register_account(username, password, accountType="student"):
    success = False
    # Check if account type is valid
    if accountType not in ["staff", "administrator", "teacher", "student"]:
        print("Account Type unavailable")

    # Check if the account already exists in the accounts list
    accounts = fetch_data("data/user_data.txt")

    for data in accounts:
        if username == data["username"]:
            print("Account already exists, Please try another username!")

    # Generate new student ID
    existing_ids = [data.get("student_id", "STD0000") for data in accounts]
    new_id = generate_student_id(existing_ids)

    # Add the new account to user_data.txt with student_id and fund
    new_account = {
        "username": username,
        "password": password,
        "accountType": accountType,
        "student_id": new_id,
        "fund": 0
    }
    accounts.append(new_account)

    # Save the file
    if insert_data("data/user_data.txt", accounts):
        print(f"Account for {username} successfully registered.")
        print(f"Your student ID is: {new_id}")
        success = True
    else:
        print("Error registering account. Please try again.")
        
    return success