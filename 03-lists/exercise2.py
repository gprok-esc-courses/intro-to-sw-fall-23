# Create an empty list: usernames = [] which will contain unique usernames. Then create a simple menu with the options:
# 1. Register User
# 2. Delete account
# 0. EXIT
# Option 1: Ask user for a username, then check if the username is not in the list, add it 
# and display a respective message, otherwise, display a message that the username is already in use and cannot be added.
# Option 2: Ask user for a username, if the username is in the list, delete it and display respective message, otherwise, display a message that username was not found.
# Option 3: Terminate the program.

usernames = []

while True:
    print("1. Register User")
    print("2. Delete account")
    print("0. EXIT")
    choice = int(input("Choose: "))

    if choice == 1:
        username = input("Username: ")
        if username in usernames:
            print("Username already in use")
        else:
            usernames.append(username)
            print("Username added")
    elif choice == 2:
        username = input("Username: ")
        if username in usernames:
            usernames.remove(username)
            print("Username deleted")
        else:
            print("Username is not in the list")
    elif choice == 0:
        print("Bye!")
        break
    else:
        print("Wrong option")


