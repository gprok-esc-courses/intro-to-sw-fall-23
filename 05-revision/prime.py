# Find if a number is prime or not

while True:
    try:
        n = int(input("Give a number: "))
        break
    except ValueError:
        print("Wrong input")

is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Is Prime")
else:
    print("Not a prime")
