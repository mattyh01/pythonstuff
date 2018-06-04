

def addition(num1, num2):
        result = num1 + num2

        print result



def stringtoint(str1, str2):
        result = int(str1) + int(str2)
        print result

def concat(x, y):
    print str(s1) + str(s2)

def length(x, y):
    len1 = len(x)
    len2 = len(y)
    if len1 > len2 :
        print x
    elif len1 == len2 :
        print x
        print y
    else:
        print x

def is_even(x):
    if x % 2 == 0:
        print "This number is even"
    else:
        print "This number is odd"

def diction():
    d={}
    for i in range (1,21):
        d[i]=i**2
        print d[i]       #Prints the value key (which is i in this case)
    for x in d.keys():   #Prints the key
        print x
    #d[4]=4**4
    print d             #Prints d, the dictionary

def list_func():
    l=[]
    for i in range (1,21):
        ii = i**i
        l.append(ii)
        print i


#s1 = raw_input("String 1 please. ")
#s2 = raw_input("String 2 please. ")
#addition(1, 3)
#stringtoint(1, 3)
#concat(s1, s2)
#length(s1, s2)
#is_even(0)
#diction()
list_func()
