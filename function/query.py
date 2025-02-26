def fetch_data(file_path):
    """
    Fetch all data from a file and parse dictionary-like strings
    Args:
        file_path (str): Path to the file to read from
    Returns:
        list: List of dictionaries parsed from the file
    """
    try:
        data_list = []
        with open(file_path, 'r') as file:
            for line in file:
                # Remove any extra spaces or newlines
                line = line.strip()
                
<<<<<<< Updated upstream
                if line:  # Skip empty lines
                    try:
                        # Use ast.literal_eval to safely parse the dictionary string
                        import ast
                        data_dict = ast.literal_eval(line)
                        data_list.append(data_dict)
                    except:
                        print(f"Error parsing line: {line}")
                        continue
=======
                # Check if the line is a valid dictionary-like string
                if line.startswith("{") and line.endswith("}"):
                    # Remove the curly braces
                    line = line[1:-1]
                    # Split by commas to get key-value pairs
                    key_value_pairs = line.split(", ")

                    data_dict = {}
                    for pair in key_value_pairs:
                        # Split each pair into key and value
                        key, value = pair.split(": ")
                        # Remove extra quotes from keys and value s
                        key = key.strip('"')
                        value = value.strip('"')
                        data_dict[key] = value

                    # Add the parsed dictionary to the list
                    data_list.append(data_dict)
>>>>>>> Stashed changes
                    
        return data_list
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return []
    except Exception as e:
        print(f"Error reading file: {str(e)}")
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
        with open(file_path, 'w') as file:
            for i, data in enumerate(data_list):
                # Create a list of key-value pairs formatted as strings
                fields = [f'"{key}": "{value}"' for key, value in data.items()]
                # Join all fields with commas and wrap in curly braces
                data_string = "{" + ", ".join(fields) + "}"
                
                if i < len(data_list) - 1:
                    data_string += '\n'
                file.write(data_string)
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
