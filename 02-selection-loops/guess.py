# User has to guess a random number
import random 

r = random.randint(1, 100)
print(r)

guess = 0
counter = 0

while guess != r:
    # counter = counter + 1
    counter += 1
    guess = int(input("Guess: "))
    if guess == r:
        print("Congrats!")
    elif guess > r:
        print("Go DOWN")
    else:
        print("Go UP")

print("Number found in", counter, "guesses")