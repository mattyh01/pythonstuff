class Employees():
    """Test Class for python"""
    raise_amount = 1.04

    def __init__(self, first, last, pay, email):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employees('Matt', 'Holmes', 50000, 'employee@company.com')

print( Employees.raise_amount)
print(emp1.__dict__)
print(emp1.pay())
emp1.apply_raise
print(emp1.pay())
