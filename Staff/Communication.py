import sys
import os
import datetime

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from function.query import *
from function.cache import *

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

def viewed_chat_file():
    """
    Read and return all chat records from file
    Returns:
        list: List of chat dictionaries
    """
    chat_list = fetch_data("data/chat_data.txt")
    return chat_list if chat_list else []

def delete_chat():
    """
    Delete messages that have reached their view limit
    """
    chat_list = viewed_chat_file()
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

def update_chat(chat_list, operation_type=None):
    """
    Update chat records in the file using the query functions
    Args:
        chat_list (list): List of chat dictionaries to update
        operation_type (str): Type of operation ('send' or None)
    Returns:
        bool: True if successful, False otherwise
    """
    try:  
        # Use insert_data function to write the updated list
        success = insert_data("data/chat_data.txt", chat_list)
        
        if success and operation_type == 'send':
            print("Message sent successfully.")
        return success
    except Exception as e:
        print(f"Error updating chat data: {e}")
        return False

def view_new_messages():
    """
    Display only unviewed messages for the current user and returns count
    Returns:
        int: Number of new messages
    """
    student_id = get_student_id()
    chat_list = viewed_chat_file()
    
    # Filter unviewed chats where the current user is the receiver
    new_messages = [chat for chat in chat_list if 
                   chat["receiver"] == student_id and chat["viewed"] == "False"]
    
    new_message_count = len(new_messages)
    
    if not new_messages:
        print("\nNo new messages.")
        return new_message_count
    
    # Sort new messages by view_limit (ascending) and then by date
    new_messages.sort(key=lambda x: (int(x["view_limit"]), x["date"]))
    
    # Display all new messages first
    print(f"\n===== New Messages ({new_message_count}) =====")
    for i, chat in enumerate(new_messages, 1):
        print(f"\n{i}. From: User {chat['sendrt']}")
        print(f"   Time: {chat['date']}")
        print(f"   Message: {chat['data']}")
        print(f"   View limit remaining: {chat['view_limit']}")
    
    # Ask user to confirm they've read the messages
    input("\nPress Enter after you've read all messages...")
    
    # Update viewed status and view limits for all messages at once
    messages_updated = False
    for new_msg in new_messages:
        for original_chat in chat_list:
            if (original_chat["sendrt"] == new_msg["sendrt"] and 
                original_chat["receiver"] == new_msg["receiver"] and
                original_chat["date"] == new_msg["date"] and
                original_chat["viewed"] == "False"):
                original_chat["viewed"] = "True"
                original_chat["view_limit"] = str(int(original_chat["view_limit"]) - 1)
                messages_updated = True
    
    # Update the chat file with viewed status changes
    if messages_updated:
        if update_chat(chat_list):
            print("All messages marked as read.")
        else:
            print("Error updating message status.")
    
    return new_message_count

def view_chat():
    """
    Display all chat messages for the current user
    """
    student_id = get_student_id()
    chat_list = viewed_chat_file()
    
    # Filter chats where the current user is either sender or receiver
    user_chats = [chat for chat in chat_list if 
                 chat["receiver"] == student_id or chat["sendrt"] == student_id]
    
    if not user_chats:
        print("\nNo messages found.")
        return
    
    # Sort chats by view_limit (ascending) and then by date
    user_chats.sort(key=lambda x: (int(x["view_limit"]), x["date"]))
    
    # Display chats
    print("\n===== Chat History =====")
    for i, chat in enumerate(user_chats, 1):
        sender = "You" if chat["sendrt"] == student_id else f"User {chat['sendrt']}"
        receiver = "You" if chat["receiver"] == student_id else f"User {chat['receiver']}"
        
        print(f"\n{i}. From: {sender} | To: {receiver}")
        print(f"   Time: {chat['date']}")
        print(f"   Message: {chat['data']}")
        print(f"   View limit remaining: {chat['view_limit']}")
        
        # Mark as viewed if it was unviewed and addressed to current user
        if chat["receiver"] == student_id and chat["viewed"] == "False":
            for original_chat in chat_list:
                if (original_chat["sendrt"] == chat["sendrt"] and 
                    original_chat["receiver"] == chat["receiver"] and
                    original_chat["date"] == chat["date"] and
                    original_chat["viewed"] == "False"):
                    original_chat["viewed"] = "True"
                    original_chat["view_limit"] = str(int(original_chat["view_limit"]) - 1)
    
    # Update the chat file with viewed status changes
    update_chat(chat_list)

def send_message():
    """
    Send a new message to another user
    """
    student_id = get_student_id()
    
    if not student_id or student_id == "None":
        print("Error: Not logged in. Please log in again.")
        return
        
    chat_list = viewed_chat_file()
    
    # Get receiver ID
    while True:
        try:
            receiver = input("\nEnter receiver ID: ")
            if not receiver:
                print("Receiver ID cannot be empty.")
                continue
            receiver = receiver.strip()
            
            # Validate receiver ID
            if not validate_student_id(receiver):
                print("Error: Invalid receiver ID. Please enter a valid student ID.")
                continue
                
            # Prevent sending message to self
            if receiver == student_id:
                print("Error: Cannot send message to yourself.")
                continue
                
            break
        except ValueError:
            print("Invalid input. Please enter a valid ID.")
    
    # Get message content
    while True:
        message = input("Enter your message: ").strip()
        if message:
            break
        print("Message cannot be empty.")
    
    # Create new chat entry with proper sender ID
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_chat = {
        "sendrt": student_id,  # Use the actual student_id
        "receiver": receiver,
        "data": message,
        "date": timestamp,
        "viewed": "False",
        "view_limit": "3"  # Default view limit
    }
    
    # Verify the message data before sending
    if not new_chat["sendrt"]:
        print("Error: Could not determine sender ID.")
        return
        
    # Add new chat to the list and update
    chat_list.append(new_chat)
    update_chat(chat_list, operation_type='send')

def communication_main():
    """
    Main communication menu loop
    """
    student_id = get_student_id()

    while True:
        delete_chat()
        print(f"\nCurrent user: {student_id}")  # Show current user
        view_new_messages()
        
        print("\nCommunication")
        print("'1' - View Chat")
        print("'2' - Send Message")
        print("'3' - Quit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == '1':
            view_chat()
        elif choice == '2':
            send_message()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
            continue