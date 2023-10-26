# Ask user for a string,
# then ask for a letter
# and find how many times 
# the letter is in the string

s = "Another exercise in Python, pretty simple"
c = 'p'

slower = s.lower()

counter = 0
for character in slower:
    if character == c:
        counter = counter + 1

print(c, "appears", counter, "times")


