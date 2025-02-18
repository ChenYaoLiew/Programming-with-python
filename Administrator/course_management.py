from Administrator.menu import administrator_user_page

def manageCourse()
    print("'1' - View Accounts\n'2' - Add Account\n'3' - Update Account\n'4' - Delete Account\n'5' - Back")

    choice = input("Enter your choice: ")
    if choice == '1':
        viewAccounts()
    elif choice == '2':
        addAccount()
    elif choice == '3':
        updateAccount()
    elif choice == '4':
        deleteAccount()
    elif choice == '5':
        administrator_user_page()