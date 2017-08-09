word = "EVAPORATE"

print ("Hello, and welcome to hangman!")
print ("You have six guesses before you lose. Good luck!")

for i in range(100):

     guess = str(raw_input('Please input a letter. '))

     i = i + 1

     for j in word: 

        if guess == j:

         	print("Correct! The word is as follows...") 

                 

        else:

		continue



  			


