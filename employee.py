class Employee:
    def __init__(self, name):
        self.name = name
        print("Employee created:", self.name)

    def __del__(self):
        print("Employee deleted:", self.name)


emp = Employee("Ravi")
del emp
