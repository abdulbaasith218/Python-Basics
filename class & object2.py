#constructor

class student:
    def __init__(self,fname,age):  #__init_  : constractor
        self.name=fname
        self.age=age

    def display(self):
        print(f'Name: {self.name}, Age: {self.age}')

s1=student(fname="Gomtham", age=10)
s1.display()