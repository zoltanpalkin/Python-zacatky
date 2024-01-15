#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class auto:
    def __init__ (self,max_speed,milage):
        self.max_speed = max_speed
        self.milage = milage
    
    def show(self):
        print(f"max speed is {self.max_speed}, milage {self.milage}")


bmw = auto(300,5000)
bmw.show()