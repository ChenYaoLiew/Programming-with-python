import json

def fetch_data(file_path):
    """
    Fetch all data from a file and parse dictionary-like strings
    Args:
        file_path (str): Path to the file to read from
    Returns:
        list: List of dictionaries parsed from the file
    """
    try:
        import ast
        with open(file_path, "r") as file:
            return [ast.literal_eval(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"File Not Found: {file_path}")
        return []
    except Exception as e:
        print(f"Parsing Error: {e}")
        return []

def insert_data(file_path, data_list):
    """
    Write data to a file in dictionary format
    Args:
        file_path (str): Path to the file to write to
        data_list (list): List of dictionaries to write to the file
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        import json
        with open(file_path, "w", encoding="utf-8") as file:
            for data in data_list:
                file.write(json.dumps(data) + "\n")
        return True
    except Exception as e:
        print(f"Error writing to file: {str(e)}")
        return False

def remove_data(file_path, data_to_remove):
    """
    Remove specific data from a file
    Args:
        file_path (str): Path to the file
        data_to_remove (str): Exact line of data to remove
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Read all lines
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Write back all lines except the one to remove
        with open(file_path, 'w') as file:
            for line in lines:
                if line.strip() != data_to_remove.strip():
                    file.write(line)
        return True
    except Exception as e:
        print(f"Error modifying file: {str(e)}")
        return False
