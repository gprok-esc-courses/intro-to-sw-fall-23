
n = int(input("Give a number: "))

s = str(n)
rs = s[::-1]

if n < 0:
    print("Not a palindrome")
else:
    if s == rs:
        print("It's a palindrom")
    else:
        print("Not a palindrome")