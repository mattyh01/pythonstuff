import random

with open('sowpods.txt') as sowpods_file:
    words = list(sowpods_file)
#    hangman = random.choice(words).strip()

hangman = "EVAPORATE"
hangman = list(hangman)
guessed = '_' * len(hangman)
guessed = list(guessed)
lastguess = []

#print guessed
#print ""
#print hangman

masked_hangman = []
xcount = 0

print "Welcome to hangman!"


while xcount < 10:

    letter = raw_input("Guess a letter! ")
    letter = letter.upper()


    if letter in list(hangman):
        print ("Correct!")
        index = hangman.index(letter.upper())
        guessed[index] = letter.upper()
        hangman[index] = "_"
        print (''.join(guessed))
    else:
    #    print (''.join(guessed))
        if letter is not '':
            lastguess.append(letter.upper())
            print "Incorrect this time!"
            print (''.join(guessed))
            print ""
            xcount = xcount + 1
    print ("You have " + str((10 - int(xcount))) + " lives left.")
    print ("Incorrect letters: " + str(lastguess))

    if '_' not in guessed:
        print "You did it!"
        break



    #for i in range(len(hangman)):
    #    if letter
