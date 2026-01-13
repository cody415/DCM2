class Parrot:
    species = "Bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age


parrot1 = Parrot("Mithu", 2)
parrot2 = Parrot("Chiku", 4)

print("Class variable (species):", Parrot.species)
print("Parrot1 -> Name:", parrot1.name, ", Age:", parrot1.age)
print("Parrot2 -> Name:", parrot2.name, ", Age:", parrot2.age)
