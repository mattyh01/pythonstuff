
def collatz(number):
    '''Doc

    Strings.'''
    if number % 2 == 0:
        number = number * 2
        print number

    else:
      number = 3 * number + 1
      print number

try:
    user = int(raw_input("Type a number! "))

    collatz(user)

except:

    print ("Not a number")

#collatz(user)
