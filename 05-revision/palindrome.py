# Find if a number is palindrome or not
# 12321 is a palindrome
# 12345 is not
# 161 is a palindrome
# -161 is not

n = int(input("Give a number: "))

if n < 0:
    print("NO")
else:
    s = str(n)
    is_palindrome = True
    for i in range(len(s)):
        if s[i] != s[(i+1)*-1]:
            print("NO")
            is_palindrome = False
            break
    if is_palindrome:
        print("YES")