class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print("Name:", self.name)
        print("ID Number:", self.idnumber)


class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)
        self.salary = salary
        self.post = post


emp = Employee("Ravi", 101, 50000, "Manager")
emp.display()
