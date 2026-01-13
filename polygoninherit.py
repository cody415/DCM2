from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


# Create objects of different polygons
rect = Rectangle(10, 5)
sq = Square(6)
tri = Triangle(8, 4)
cir = Circle(7)

# Display areas
print("Area of Rectangle:", rect.area())
print("Area of Square:", sq.area())
print("Area of Triangle:", tri.area())
print("Area of Circle:", cir.area())
