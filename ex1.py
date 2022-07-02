#a class with instance attributess
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


#a class without any variables and methods
class Company:
    pass

#passing values to class using variable
vechicleSpec = Vehicle(150, 24)


print(vechicleSpec.max_speed, vechicleSpec.mileage)