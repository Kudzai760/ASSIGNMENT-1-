class Shape:
    def area(self) -> float:


class Circle(Shape):
 def __init__(self, radius: float):
        self.radius = radius
def area(self) -> float:
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def total_area(shapes: List[Shape]) -> float:

    return sum(shape.area() for shape in shapes)


if __name__ == "__main__":
    # Create a list of different shapes
    shapes = [
        Circle(radius=5),
        Rectangle(width=4, height=6),
        Circle(radius=3),
        Rectangle(width=2, height=8)
    ]

    # Calculate and print the total area of all shapes
    print(f"Total area of all shapes: {total_area(shapes):.2f}")
