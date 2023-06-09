class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def __str__(self):
        if self.taste:
            return f"You have soda with {self.taste} taste."
        else:
            return "You have soda with no taste."


obj1 = Soda("strawberry")

print(obj1)


class Math:

    def addition(self, x, y):
        return f"{x} + {y} = {x + y}"

    def subtraction(self, x, y):
        return f"{x} - {y} = {x - y}"

    def multiplication(self, x, y):
        return f"{x} * {y} = {x * y}"

    def division(self, x, y):
        return f"{x} / {y} = {x / y}"


obj2 = Math()
print(obj2.addition(2, 3))

class Car:

    def __init__(self, color=None, type=None, year=None):
        self.color = color
        self.type = type
        self.year = year

    def start_engine(self):
        print("Car is started!")

    def turn_off_car(self):
        print("Car is turned off!")

    def set_color(self, color):
        self.color = color

    def set_type(self, type):
        self.type = type

    def set_year(self, year):
        self.year = year


car1 = Car()
car1.start_engine()
car1.turn_off_car()
car1.set_color("blue")
car1.set_year(2015)
car1.set_type("bus")

print(car1.color)
print(car1.year)
print(car1.type)
