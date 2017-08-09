import random

user = (raw_input("Roll the dice? (Y, N) "))
count = 0
dice = 0

def generate_die(dice):
    dice = random.randint(1,6)
    print "The number rolled is %s \n" % dice


while user == "Y":
    generate_die(dice)
    count += 1
    user = raw_input("Try again? ")

else:
    print "Exiting... You rolled the dice %s times" % count
