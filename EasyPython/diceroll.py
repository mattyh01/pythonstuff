import time, random

# Matts dice roll simulator!

print "Rolling the dice now!"


def roll():
    time.sleep(2)
    val = random.randint(1, 6)
    print "The value is %s!" % val
    time.sleep(2)
    a = raw_input("Would you like to roll again? ")
    

roll()

time.sleep(2)


if a == "yes":
    roll()
else:
   exit 


