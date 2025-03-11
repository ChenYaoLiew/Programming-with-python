from function.query import *

def generate_user_id(existing_ids):
    """
    Generate a new user ID in format UIDXXXX
    Args:
        existing_ids (list): List of existing student IDs
    Returns:
        str: New unique user ID
    """
    max_num = 0
    for user_id in existing_ids:
        if user_id.startswith("UID"):
            try:
                num = int(user_id[3:])
                max_num = max(max_num, num)
            except ValueError:
                continue
    
    new_num = max_num + 1
    return f"UID{new_num:04d}"

def register_account(username, password, account_type="student"):
    success = False
    # Check if account type is valid
    if account_type not in ["staff", "administrator", "teacher", "student"]:
        print("Account Type unavailable")

    # Check if the account already exists in the accounts list
    accounts = fetch_data("../data/user_data.txt")
    # Get the student course data as a list
    for data in accounts:
        if username == data["username"]:
            print("Account already exists, Please try another username!")
            return success

    # Generate new student ID
    existing_ids = [data.get("student_id", "UID0000") for data in accounts]
    new_id = generate_user_id(existing_ids)

    # Add the new account to user_data.txt with student_id and fund, if account_type is student, it will insert extra details data
    if account_type == "student":
        new_account = {
            "username": username,
            "password": password,
            "account_type": account_type,
            "student_id": new_id,
            "fund": float(0),
            "phone_num": "Empty",
            "country": "Empty",
            "emergency_info": "Empty",
            "feedback": "Empty"
        }
        accounts.append(new_account) # insert new student account into accounts

        # Save the file
        if insert_data("data/user_data.txt", accounts):
            print(f"Account for {username} successfully registered.")
            print(f"Your student ID is: {new_id}")
            success = True
        else:
            print("Error registering account. Please try again.")

    else:
        new_account = {
            "username": username,
            "password": password,
            "account_type": account_type,
            "student_id": new_id,
            "fund": float(0),
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