list = [4, 10, 12, 22, 58, 72]

def isnumberinorder(input):

   print list[-1]
   print list[0]


   if input < list[-1] and input > list[0]:

	      print ("True!")
              return True

   else:

             print ("Number not within number list")
             return False

print "\n"
print list
print "\n"
user = raw_input("Input a number. ")
isnumberinorder(user)

             


  
