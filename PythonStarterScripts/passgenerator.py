import random, time, MySQLdb, sys

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@$%^!?"
wordlist = []

# Open sowpods file for easy passwords, takes random sample

with open("sowpods.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        wordlist.append(line.rstrip())

#DB connection to store passwords for each user

try:

	db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="",
                     db="python_test"
                     )

except:

	print "Unable to connect to database - please check details"

cur = db.cursor()

name = raw_input("Hello, welcome to password generator. What is your name? ")
print ""
print ("Excellent - hello %s. ") % name
time.sleep(2)
print ""
user = raw_input("Please pick how strong you want your password to be. (weak, medium, strong) ")

f.close()

if user == "weak":
    p = "".join(random.sample(wordlist, 1))
    print "Your password is %s." % p

elif user == "medium":
    p = "".join(random.sample(chars,8))
    print "Your password is %s." % p

elif user == "strong":
    length = int(raw_input("You picked strong. How long would you like your password? "))
    p = "".join(random.sample(chars, length))
    print "Your password is %s." % p

else:
    print("Incorrect option. Exiting...")
    sys.exit()

print "Printing to DB..."

try:
    cur.execute("""INSERT INTO passwords (name, pass) VALUES (%s, %s)""", (name, p))
    db.commit()
    print "DB Write successful."

except:
    print "Failure printing to database."
