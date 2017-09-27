class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()

# Here, we define the __init__ method as taking a parameter name (along with the usual self). Here, we just create a new field also called name. Notice these are two different variables even though they are both called 'name'. There is no problem because the dotted notation self.name means that there is something called "name" that is part of the object called "self" and the other name is a local variable. Since we explicitly indicate which name we are referring to, there is no confusion.
