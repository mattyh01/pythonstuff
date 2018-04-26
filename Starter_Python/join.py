import os

list = ['Hi', 'Prick', '1234']
difflist = []

i = ", ".join(list)

for x in list:
    difflist.append(x)

print difflist

print i.upper()
print ""
print ""
print "Some directory info"
print ""
current = os.getcwd()

current = current.rjust(10)


print "The current directory is %s" % current
