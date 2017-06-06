fibonacci = [1, 1]



def fib(input):

	for i in range(user):

		calc = fibonacci[-2] + fibonacci[-1]
		fibonacci.append(calc)


	print ("Total of fib numbers: " + str(calc))
	print fibonacci

try: 

	user = int(raw_input("How many Fibonacci numbers to generate? "))

	fib(user)

except:

	print ("Not a number, try again")

