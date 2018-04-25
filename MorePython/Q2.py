#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320
import math

fact = int(raw_input("Find out the factorial of the number by inputting a number below. "))

result = math.factorial(fact)

print result
