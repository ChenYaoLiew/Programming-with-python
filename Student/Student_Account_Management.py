
def manage_account(student_info):
    while True:
        print(f'\nStudent Name: {student_info['username']}')
        print(f'Student ID: {student_info['student_id']}')
        print(f'Student Fund: {student_info['fund']}')
        print("\n'1' - Change password")
        print("'2' - Back")

        choice = input('Enter your choice: ')
        if choice == '1':
            pass
        elif choice == '2':
            break
        else:
            print('Invalid choice!')
