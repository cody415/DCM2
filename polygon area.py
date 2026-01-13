class Polygon:
    def area(self):
        print("Area method not implemented in base class.")


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


# Demonstration
shapes = [
    Rectangle(10, 5),
    Square(6),
    Triangle(8, 4),
    Circle(7)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} Area:", shape.area())
