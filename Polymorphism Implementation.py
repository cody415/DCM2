class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a Dog. My name is {self.name} and I am {self.age} years old.")

    def make_sound(self):
        print("Woof! Woof!")


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a Cat. My name is {self.name} and I am {self.age} years old.")

    def make_sound(self):
        print("Meow! Meow!")


# Creating objects
dog1 = Dog("Bruno", 3)
cat1 = Cat("Kitty", 2)

# Polymorphism in action
for animal in (dog1, cat1):
    animal.info()
    animal.make_sound()
