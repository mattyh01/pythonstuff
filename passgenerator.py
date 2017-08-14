import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@$%^!?"
wordlist = []


with open("sowpods.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        wordlist.append(line.rstrip())


user = raw_input("Hello, please pick how strong you want your password to be. (weak, medium, strong) ")

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
