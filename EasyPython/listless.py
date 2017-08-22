a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []

for i in a:
   if i < 5:
     b.append(i)

print b

num = int(raw_input("Enter a number. "))

for i in a:
   if i < num:
    c.append(i)

print "These are the smaller numbers: %s" % c
   
   

