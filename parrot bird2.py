class Parrot:
    species = "Bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self):
        print(self.name, "is singing")

    def dance(self):
        print(self.name, "is dancing")


parrot1 = Parrot("Mithu", 2)
parrot2 = Parrot("Chiku", 4)

print("Class variable (species):", Parrot.species)
print("Parrot1 -> Name:", parrot1.name, ", Age:", parrot1.age)
print("Parrot2 -> Name:", parrot2.name, ", Age:", parrot2.age)

parrot1.sing()
parrot1.dance()
parrot2.sing()
parrot2.dance()
