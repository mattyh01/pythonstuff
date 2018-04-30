import sys

class Employee:

    emp_count = 0
    id_inc = 1
    raise_amount = 1.05

    def __init__(self, emp_id, fname, lname, pay):
        self.emp_id = emp_id
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + "." + lname + "@ibm.com"
        Employee.emp_count += 1
        Employee.id_inc += 1 # Incrementor for ID when created

        #All variables are initalised here. When the objects (in this case
        #employees) are created, then the attributes of said object must be
        #input when creating the object (so you need to fill al variables
        #apart from self)

    def hello(self): #Simple function to print hello statement
        print "Hello {} nice to meet you.".format(self.fname)

    def apply_payrise(self): #Function to apply payrise according to the value in pay amount
        self.pay = int(self.pay * self.raise_amount)

    @classmethod  #Class Method - DECORATOR
    def set_raise_amt(cls, amount): #We use cls here as Class is a special variable
        cls.raise_amt = amount #Similar to self, but SPECIFIC TO Class

emp_1 = Employee(Employee.id_inc, "Matt", "Holmes", 30000)
emp_2 = Employee(Employee.id_inc, "Test", "User", 40000)


print hello(emp_1)
Employee.apply_payrise(emp_1) #< Here we call the class first, then the
print emp_1.pay               #function we want to execute, along with the
                              #object we want the function to execute on
                              #- this is the standard way of performing this
                            #print Employee.__dict__ # Prints out the attributes of the Class/Object

emp_1.raise_amount = 1.07   #Here the object (emp1) is specfically set so that
                            #the raise amount is 1.07


#You can access class variables from either the Class itself (so in this case
#Class.raise_amount or via the instance self.raise_amount - this is because
#the instance contains the attribute
