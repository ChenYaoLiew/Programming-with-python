import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from function.query import *

def read_chat_file():
    # Read and return all chat records from file, Returns list of chat dictionaries
    chat_list = fetch_data("data/chat_data.txt")
    return chat_list

def delete_chat():
    chat_list = read_chat_file()
    found = False

    # Create new list without the resource to be deleted
    updated_resources = []
    for chat in chat_list:
        if chat["view_limit"] == 0:
            found = True
        else:
            updated_resources.append(chat)
    
    if found:
        insert_data("data/chat_data.txt", updated_resources)

def update_chat(chat_list):
    """
    Update chat records in the file using the query functions
    Args:
        chat_list (list): List of chat dictionaries to update
    Returns:
        bool: True if successful, False otherwise
    """
    try:  
        # Use insert_data function to write the updated list
        success = insert_data("data/chat_data.txt", chat_list)
        
        if success:
            print("Message sent successfully.")
            return True
        else:
            print("Error sending message.")
            return False
    except Exception as e:
        print(f"Error sending message: {e}")
        return False
    
def view_chat():
    pass

def view_new_messages():
    pass

def send_message():
    pass

def communication_main():
    while True:
        delete_chat()
        print("\nCommunication")   
        print("0. View New Messages")
        print("1. View Chat")
        print("2. Send Message")
        print("3. Quit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == '0':
            view_new_messages()
        elif choice == '1':
            view_chat()
        elif choice == '2':
            send_message()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
            continue

communication_main()