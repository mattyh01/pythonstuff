a = int(raw_input("Input a number for divising. "))
list = []

for num in range(1, 100):
    if num % a == 0:
       list.append(num)

print list 
