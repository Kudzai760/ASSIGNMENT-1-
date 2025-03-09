class Vehicle:
    def __init__(self, make: str, model: str):

        self.make = make
        self.model = model

    def description(self) -> str:

        return f"Vehicle: {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make: str, model: str, doors: int):

        super().__init__(make, model)
        self.doors = doors

    def description(self) -> str:

        return f"Car: {self.make} {self.model} with {self.doors} doors"


class Bike(Vehicle):
    def __init__(self, make: str, model: str, type_of_bike: str):

        super().__init__(make, model)
        self.type_of_bike = type_of_bike

    def description(self) -> str:

        return f"Bike: {self.make} {self.model} ({self.type_of_bike} bike)"


if __name__ == "__main__":
    vehicle = Vehicle("Generic", "Model")
    car = Car("Toyota", "Vitz", 4)
    bike = Bike("Mountain bike", "cross country", "road")

    # Print out descriptions using the description method.
    print(vehicle.description())  # Uses the base class method.
    print(car.description())      # Uses the overridden method in Car.
    print(bike.description())     # Uses the overridden method in Bike.


