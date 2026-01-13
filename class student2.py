class Student:
    grade = "A"
    name = "Ravi"

    def display_sentence(self):
        print("This is the Student class")

    def display_details(self):
        print("Name:", Student.name)
        print("Grade:", Student.grade)


obj = Student()
obj.display_sentence()
obj.display_details()
