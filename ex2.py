#Inheritence example 1

class Books:

    def __init__(self, name, genre, price):
        self.name = name
        self.genre = genre
        self.price = price

class Library(Books):
    pass

theBook = Library("Happy end", "comdey", 120)
print("book Name:", theBook.name, "Genre:", theBook.genre, "price:", theBook.price)


#second pratice example

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())
