class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"{self.year} {self.make} {self.model} is now running.")

    def stop(self):
        self.is_running = False
        print(f"{self.year} {self.make} {self.model} has been stopped.")


# Creating instances of the Car class
car1 = Car("Toyota", "Camry", 2023)
car2 = Car("Tesla", "Model S", 2022)

# Using methods on the objects
car1.start()
car2.start()

car1.stop()
