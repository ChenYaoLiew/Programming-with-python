def read_student_file():
    # Read and return all student records from file, Returns list of student dictionaries
    student_list = []
    file = open('./Text.txt', 'r')
    for line in file:
        if line.strip():
            student = line.strip('\n').split(',')
            student_list.append({
                'Student ID': student[0],
                'Student Name': student[1],
                'Student Funds': float(student[2])
                # float makes it a scientific number
            })
    file.close()
    return student_list

def validate_student_id(student_id, student_list):
    # Check if student ID exists in records
    for student in student_list:
        if student['Student ID'] == student_id:
            return True, student
    return False

def validate_student_name(student_name, student_list):
    # Check if student name exists in records
    for student in student_list:
        if student['Student Name'] == student_name:
            return True, student
    return False, None

def update_student_record(student_list):
    # Trigger when need update to the text.txt file
    file = open('./Text.txt', 'w')
    for student in student_list:
        line = f"{student['Student ID']},{student['Student Name']},{student['Student Funds']}\n"
        file.write(line)
    file.close()
    return True

def view_records():
    student_list = []
    with open('./Text.txt', 'r') as file:
        for line in file:
            student = line.strip('\n').split(',')

            new_student_template = {'Student ID':student[0],'Student Name':student[1],'Student Funds':float(student[2])}
            student_list.append(new_student_template)
    for student in student_list:
        print(student)

def deposit(student_id,name):
    student_list = read_student_file()
    exists, student = validate_student_id(student_id, student_list) or validate_student_name(name, student_list)

    if not exists:
        print("Student ID not found.")
        return
    amount = input("Enter deposit amount: $")
    if float(amount) < 0:
        print("Invalid amount. Please enter a positive number.")
        return
    for student in student_list:
        student['Student Funds'] += float(amount)
        break

    if update_student_record(student_list):
        print(f"Successfully deposited ${float(amount):.2f}")
        print(f"New balance: ${student['Student Funds']:.2f}")

def withdrawal(student_id,name):
    student_list = read_student_file()
    exists, student = validate_student_id(student_id, student_list) or validate_student_name(name, student_list)

    if not exists:
        print("Student ID not found.")
        return
    amount = input("Enter withdraw amount: $")
    if float(amount) < 0:
        print("Invalid amount. Please enter a positive number.")
        return
    if student['Student Funds'] - float(amount) < 0:
        print("Insufficient funds. Withdrawal would result in a negative balance.")
        return
    for student in student_list:
        student['Student Funds'] -= float(amount)
        break

    if update_student_record(student_list):
        print(f"Successfully withdraw ${float(amount):.2f}")
        print(f"New balance: ${student['Student Funds']:.2f}")

def transfer(student_id,name):
    student_list = read_student_file()
    exists, student = validate_student_id(student_id, student_list) or validate_student_name(name, student_list)
    if not exists:
        print("Student ID not found.")
        return
    transfer_to_id = input("Transfer to (Student ID):")
    transfer_to_name = input("Transfer to (Student Name):")
    amount = input("Enter transfer amount: $")
    if float(amount) < 0:
        print("Invalid amount. Please enter a positive number.")
        return
    exists, student_to = validate_student_id(transfer_to_id, student_list) or validate_student_name(transfer_to_name, student_list)
    if not exists:
        print("Student ID not found.")
        return

    if student['Student Funds'] - float(amount) < 0 or student_to['Student Funds'] - float(amount) < 0:
        print("Insufficient funds. Would result in a negative balance.")
        return

    for student in student_list:
        student['Student Funds'] -= float(amount)
        student_to['Student Funds'] += float(amount)
        break

    if update_student_record(student_list):
        print(f"Successfully transferred ${float(amount):.2f}")
        print(f"Sender's new balance: ${student['Student Funds'] - float(amount):.2f}")
        print(f"Recipient's new balance: ${student_to['Student Funds'] + float(amount):.2f}")

def manage_student_records():
    # starting point(start the loop)
    while True:
        print("\nStudent Records Management")
        print("1. View Student Records")
        print("2. Process Deposit")
        print("3. Process Withdrawal")
        print("4. Process Transfer")
        print("5. Quit")

        choice = input("\nEnter your choice (1-5): ")

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please try again.")
            continue
        if choice == '1':
            view_records()
            continue
        elif choice == '2':
            student_id = input("Enter student ID: ")
            name = input("Enter your name: ")
            deposit(student_id,name)
            continue
        elif choice == '3':
            student_id = input("Enter student ID: ")
            name = input("Enter your name: ")
            withdrawal(student_id,name)
        elif choice == '4':
            student_id = input("Enter student ID: ")
            name = input("Enter your name: ")
            transfer(student_id,name)
        elif choice == '5':
            break

manage_student_records()