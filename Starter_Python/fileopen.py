user = raw_input("What would you like to name the file as? ")

openfile = open(user, 'w')
openfile.write("Hello")
openfile.close()
