names = ["Peter", "John", "Mary", "Mike", "Ann",
         "Nick", "Jerry", "Tom", "William", "Sue"]


# Get a letter from the user (ch)
ch = input("Give a letter: ")

counter = 0
# For every name N in the list
for name in names:
    # If first letter of N is equal to ch
    if name[0].lower() == ch.lower():
        # print it
        print(name)
        counter = counter + 1

if counter == 0:
    print("No name found")