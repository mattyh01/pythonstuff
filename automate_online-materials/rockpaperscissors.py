import random

guess = raw_input("Guess a number.")
guess = int(guess)

int = random.randint(0,9)

if guess > int:
    print "Too high! Try again."
elif int > guess:
    print "Too low! Try again."
elif guess > 9:
    print "Number out of bounds."
elif int = guess:
    print "Congratulations! You are correct!"
elif guess = "exit":
    break



print int
