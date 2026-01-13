from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def move(self):
        print("Dog runs on four legs.")


class Bird(Animal):
    def move(self):
        print("Bird flies in the sky.")


class Fish(Animal):
    def move(self):
        print("Fish swims in water.")


dog = Dog()
bird = Bird()
fish = Fish()

dog.move()
bird.move()
fish.move()
