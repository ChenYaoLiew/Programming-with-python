import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from function.query import *

def validate_student_id(student_id):
    """
    Check if a student ID exists in user_data.txt
    Args:
        student_id (str): Student ID to validate
    Returns:
        bool: True if student ID exists, False otherwise
    """
    try:
        user_list = fetch_data("data/user_data.txt")
        return any(user["student_id"] == student_id for user in user_list)
    except Exception as e:
        print(f"Error validating student ID: {e}")
        return False
