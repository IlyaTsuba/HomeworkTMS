# task1
class BMIError(Exception):
    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return f"Probably, you entered unreal data!"


try:
    weight = int(input("Set weight in kilograms: "))
    height = float(input("Set height in meters: "))

    if (weight > 300 or weight < 0) or (height > 2.4 or height < 0.6):
        raise BMIError
    BMI = round(weight / height ** 2)
    if BMI < 18.5:
        print(f"Your BMI {BMI} falls within the underweight range.")
    elif 18.5 <= BMI < 25:
        print(f"Your BMI {BMI} falls within the healthy weight range.")
    elif 25 <= BMI < 30:
        print(f"Your BMI {BMI} falls within the overweight range.")
    else:
        print(f"Your BMI {BMI} falls within the obesity range.")

except ZeroDivisionError:
    print("Height can't be 0!")
except ValueError:
    print("Set correct data type. Float for height, Integer for weight.")


# task 2

class Task2:

    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    @property
    def numbers(self):
        return f"{self.__num2} {self.__num2}"

    @numbers.setter
    def numbers(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def summ(self):
        return self.__num1 + self.__num2

    def subtraction(self):
        return self.__num1 - self.__num2

    def multiplication(self):
        return self.__num1 * self.__num2

    def division(self):
        return self.__num1 / self.__num2


try:
    num1 = int(input("Set 1st number: "))
    num2 = int(input("Set 2nd number: "))
    obj = Task2(num1, num2)

    print(obj.summ())
    print(obj.multiplication())
    print(obj.subtraction())
    print(obj.division())

except ZeroDivisionError as e:
    print("num2 can't be 0 Error: ", e)
except ValueError:
    print("num1 and num2 must be integers!")
else:
    print("You are krasavchik!")
finally:
    print("Thank you!")
