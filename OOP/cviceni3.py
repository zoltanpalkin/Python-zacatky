#OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class veichle:
    def __init__(self,name,max_speed,milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage
    def show(self):
        print(f"name {self.name}, max speed {self.max_speed}, milage {self.milage}")
class Bus(veichle):
    pass

School_bus = Bus("School Volvo", 180 ,20)
School_bus.show()

