import random

#guess = int(guess)

int = random.randint(0,9)
j = 0
i = ""

while i != "exit":
   guess = raw_input("Guess a number. ")
   if guess > int:
       print "Too high! the number was " + str(int)
       i = raw_input("Try again. ")
   elif int == guess:
       print "Congratulations! You are correct!"
       break
   else:
       print "Too low! the number was " + str(int)
       i = raw_input("Try again. ")
   j = j + 1
    
print "You took " + str(j) + " guesses"
