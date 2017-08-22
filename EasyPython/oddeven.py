
num = raw_input("Hi - please input any number. ")

num = int(num)

if (num % 2 == 1): 

   print("This number is odd!")

elif (not(num % 4)):

  print(str(num) + " is a multiple of 4.")

else:

   num = str(num)

   print(num + " is even!")

print("Done.")
