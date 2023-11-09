# Extract all digits from a number into a list
# Without converting number to string

digits = []

n = int(input("Give a number: "))
temp = n

while temp != 0:
    remainder = temp % 10
    digits.append(remainder)
    temp = temp // 10

print(digits)