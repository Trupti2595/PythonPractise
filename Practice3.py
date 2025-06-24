#Define a circle class te create a circle with radius r using the constructor
#Define an Area() method of the class which calculates the area of the circle

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

r1 = Circle(21)
print(r1.area())
print(r1.perimeter())