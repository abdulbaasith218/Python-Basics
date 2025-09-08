class Student:
    def __init__(self, name, grade):   # Fixed __init__
        self.name = name
        self.grade = grade

    def display(self):
        print(f'{self.name} is in grade {self.grade}')


# Creating objects properly
s1 = Student(name="Gomtham", grade=10)
s2 = Student(name="Nandini", grade=12)
s3 = Student(name="Nita", grade=11)

# Displaying results
s1.display()
s2.display()
s3.display()
