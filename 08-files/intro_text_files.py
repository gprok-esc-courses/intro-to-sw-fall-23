
file = open("document.txt", "r")
copy_file = open("document-copy.txt", "w") 

lines = file.readlines()

for line in lines:
    print(line)
    copy_file.write(line)