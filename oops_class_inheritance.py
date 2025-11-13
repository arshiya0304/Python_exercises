class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def __str__(self):
        return f"{self.make} {self.model} - {self.num_doors} doors"


car = Car("Honda", "Civic", 4)
print(car)