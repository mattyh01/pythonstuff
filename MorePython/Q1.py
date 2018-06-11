#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

number = [i for i in range(2001, 3001) if i % 7 == 0 and i % 5 != 0]


list = []
list.append(str(number))

print ','.join(list)
