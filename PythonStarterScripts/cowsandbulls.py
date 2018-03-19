import random, sys

randnum = random.randint(1000,9999)

print "Welcome to the Cows and Bulls game."




#def __init__(self):
 #  self.bull = bull
  # self.cow = cow
   #self.user = user


#user = raw_input()



#could probably initatilise some stuff here

user = 0

while user != randnum :

    bull=0
    cow=0

    user = raw_input("Enter a number. ")

    listnum = str(randnum)
    userlist = str(user)
    looping=0

    for looping in range(0, 4):

        if listnum[looping] == userlist[looping] :

           bull = bull + 1

           if bull == 4:

               print "Correct! The number was {}".format(user)

               sys.exit()

        else:

               cow = cow + 1





    print "{} cows, {} bulls".format(cow, bull)


print "The number is {}".format(randnum)
