class Shape:
    def __init__(self, color: str = "undefined"):

        self.color = color

    def calculate_area(self) -> float:

        print("Shape.calculate_area() called - performing common pre-area logic")
        # In this base class, we don't have a specific implementation
        return 0.0


class Rectangle(Shape):
    def __init__(self, width: float, height: float, color: str = "undefined"):

        super().__init__(color)
        self.width = width
        self.height = height

    def calculate_area(self) -> float:


        base_logic = super().calculate_area()
        rectangle_area = self.width * self.height
        print(f"Rectangle.calculate_area() computed: {self.width} * {self.height} = {rectangle_area}")
        return rectangle_area


if __name__ == "__main__":

    rect = Rectangle(width=6, height=5, color="orange")

    # Calculate and print the area.
    area = rect.calculate_area()
    print(f"A {rect.color} rectangle has an area of {area}.")