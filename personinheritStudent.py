class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print("Full Name:", self.fname, self.lname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

    def display(self):
        super().printname()
        print("Graduation Year:", self.year)


student1 = Student("Ravi", "Patel", 2026)
student1.display()
