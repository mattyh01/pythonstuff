import random

randomnum = random.randint(1, 9)
guess = 0
tries = 0


while randomnum != guess and guess != "exit":

	try:

	        print randomnum
		guess = int(raw_input("Guess a number between 1 and 9! "))



		if guess > randomnum:

			print ("No! Try again, too high")

			tries = tries + 1

		elif guess < randomnum:

			print ("No! Try again, too low")

			tries = tries + 1

		else:

			print ("Correct!!")

			print ("Correct! You took " + str(tries) + " guesses")

	except: 
			print("Non integer used, exiting.")
			break
