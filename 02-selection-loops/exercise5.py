# Write a program to display the following menu:
# 1. Open File 
# 2. Save File 
# 3. Delete File 
# 0. Exit 
# Choose :>
# And depending on users’ choice 
# display a respective message, 
# like “File opened ...” for option 1. 
# If the user will choose zero, 
# the program will terminate.

while True:
    print("1. Open File")
    print("2. Save File")
    print("3. Delete File")
    print("0. Exit")
    choice = int(input("Choose :> "))

    if choice == 1:
        print("Opening file ...")
    elif choice == 2:
        print("Saving file ...")
    elif choice == 3:
        print("Deleting file ...")
    elif choice == 0:
        print("Bye!")
        break
    else:
        print("Wrong choice.")