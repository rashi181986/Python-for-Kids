import math

class Circle:
    def __init__(self, radius):
        # Initialize the circle with a radius
        self.radius = radius

    def compute_area(self):
        # Formula: π * r^2
        return math.pi * (self.radius ** 2)

    def compute_perimeter(self):
        # Formula: 2 * π * r
        return 2 * math.pi * self.radius

# Example Usage:
my_circle = Circle(5)

print(f"Radius: {my_circle.radius}")
print(f"Area: {my_circle.compute_area():.2f}")
print(f"Perimeter: {my_circle.compute_perimeter():.2f}")
