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
