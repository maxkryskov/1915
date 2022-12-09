class Human:
    def __init__(self, name = "Human"):
        self.name = name
class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
    def add_passengers(self, Human):
        self.passengers.append(Human)
    def print_passengers_name(self):
        if self.passengers !=[]:
            print(f"Names of {self.brand} passengers:")
            for passengers in self.passengers:
                print(passengers.name)
        else:
            print(f"There are no passengers in {self.brand}")
Max = Human("Maxim")
Sviatoslav = Human("Sviatoslav")
Maxim = Human("Maxim")
car = Auto("Mersedes")
car.add_passengers(Max)
car.add_passengers(Sviatoslav)
car.add_passengers(Maxim)
car.print_passengers_name()
car1 = Auto("Tesla")
car1.print_passengers_name()
print()


