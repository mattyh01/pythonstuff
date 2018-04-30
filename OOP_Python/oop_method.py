import sys, datetime

#REMEMBER - DOT NOTATION FOR ATTRIBUTES, BRACKETS FOR OBJECTS

class Employee:

    emp_count = 0  #These are class variables
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

        '''All variables are initalised here. When the objects (in this case
        #employees) are created, then the attributes of said object must be
        #input when creating the object (so you need to fill al variables
        #apart from self)'''

    def hello(self):
        print "Hello {}, nice to meet you.".format(self.fname)

    def apply_payrise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod #This is a decorator - this class method sets the raise amount
                    #for the class

    def set_payrise_cls(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        emp_id, fname, lname, pay = emp_str.split('-')
        return cls(emp_id, fname, lname, pay)

    @classmethod
    def from_commasep(cls, comma_str):
        emp_id, fname, lname, pay = comma_str.split(',')
        return cls(emp_id, fname, lname, pay)

    @staticmethod #this doesen't take any variables
    def isworkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "No!"
        return "Yes."

class Developer(Employee):
    def __init__(self, emp_id, fname, lname, pay, language):
        Employee.__init__(self, emp_id, fname, lname, pay) #Initialise from parent class
        self.language = language
    raise_amount = 1.24 #Here we set a different raise amount for the Class Develoepr


class Manager(Employee):
    def __init__(self, emp_id, fname, lname, pay, band, employees=None):
        Employee.__init__(self, emp_id, fname, lname, pay)
        self.band = band
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    raise_amount = 1.70

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def add_emp(self, emp):
        if emp  in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fname())

emp_1 = Employee(Employee.id_inc, "Matt", "Holmes", 30000)
emp_2 = Employee(Employee.id_inc, "Test", "User", 40000)

dev_1 = Developer(Employee.id_inc, "Junior", "Developer", 24000, "C++ ")
dev_2 = Developer(Employee.id_inc, "Senior", "Tester", 34880, "Java")

mgr_1 = Manager(Employee.id_inc, "Bastard", "Manager", 24000, 8, [emp_1])

print mgr_1.fname + " " + mgr_1.lname +  " is at a band " + str(mgr_1.band)

#print help(Developer) #Good for looking up what the class contains
print(isinstance(mgr_1, Manager)) # Useful to see if first arg is an instance of the second arg
print(issubclass(Developer, Employee))
print dev_1.pay

print dev_1.language
print dev_2.language



emp_str_1 = ('99-Alex-McCarthy-76500')
comma_str_2 = ('44,Fraser,Forster,81250')


new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_commasep(comma_str_2)

date = datetime.date(2001, 11, 5)

#print Employee.hello(new_emp_2)


#print "Is today a working day?"
#print ((Employee.isworkday(date)))

#print emp_1.raise_amount
#Employee.apply_payrise(emp_1) # Here we call the class first, then the
                            #function we want to execute, along with the
                            #object we want the function to execute on
                            #this is the standard way of performing this'''

#emp_1.apply_payrise         #Here we call the function apply_payrise, which calculates pay * raise_amount

#print emp_1.pay                        #print Employee.__dict__ # Prints out the attributes of the Class/Object'''

#Employee.set_payrise_cls(1.07) #This is done via the class variable

                            ##Here the object (emp1) is specfically set so that'''
#print Employee.raise_amount  #Print out the amount to be raised


#print emp_1.pay
#print emp_1.emp_id
#print emp_2.emp_id

                            #You can access class variables from either the Class itself (so in this case
                            #Class.raise_amount or via the instance self.raise_amount - this is because
                            #the instance contains the attribute'''


'''Strings'''

#employee_string = ('99-John-Doe-20000')
#print emp_id
#new_emp_1 = Employee(emp_id, fname, lname, pay)
#print new_emp_1.lname

#Above is simple, it is in hyphen format, split based on char
#then write the variables into the split Strings
#write the new instance (new_emp_1) as a class object
