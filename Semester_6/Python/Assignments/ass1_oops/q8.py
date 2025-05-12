class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def display_info(self):
        print(f" Vehical model Number is {self.model} make by {self.make}")

class Car(Vehicle):
    def __init__(self,make,model,doors):
        super().__init__(make,model)
        self.doors=doors
    def display(self):
        super().display_info()
        print(f"number of doors {self.doors}")

v=Vehicle("Toyota", "Corolla")
v.display_info()
c=Car("Toyota", "Corolla",4)
c.display()