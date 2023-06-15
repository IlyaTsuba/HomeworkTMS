from math import pi


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


class Sphere:
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def get_volume(self):  # 4πR³/3
        return f"Sphere volume is {round((4 * pi * self.r ** 3) / 3, 2)}"

    def get_square(self):  # 4πR²
        return f"Sphere square is {round(4 * pi * self.r ** 2, 2)}"

    def get_radius(self):
        return f"Radius is {self.r}"

    def get_center(self):
        return f"Sphere center coordinates are {self.x, self.y, self.z}"

    def set_radius(self, r):
        self.r = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        return (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2 <= self.r ** 2


sphere1 = Sphere(2, 3, 4, 5)

print(sphere1.get_volume())

print(sphere1.get_square())

print(sphere1.get_radius())

print(sphere1.get_center())

sphere1.set_radius(7)

print(sphere1.get_radius())

sphere1.set_center(5, 6, 7)

print(sphere1.get_center())

print(sphere1.is_point_inside(8, 9, 10))


class SuperStr(str):

    def __init__(self, string):
        self.string = string
        super().__init__()

    def is_repeatance(self, s):
        flag = False
        result = ""
        while len(result) <= len(self.string):
            result += s
            if self.string == result:
                flag = True
        return flag

    def is_palindrome(self):
        return self.string.lower() == self.string.lower()[::-1]


str5 = SuperStr("aaaaaaa")

print(str5.is_repeatance("aa"))

print(str5.is_palindrome())
