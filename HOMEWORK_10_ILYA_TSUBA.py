# task1
class Good:

    def __init__(self, good_name, shop_name, price):
        self.__good_name = good_name
        self.__shop_name = shop_name
        self.__price = price

    def __str__(self):
        return f"{self.__good_name} {self.__shop_name} {self.__price}"

    def __add__(self, other):
        if isinstance(other, Good):
            return self.__price + other.__price

    @property
    def good_name(self):
        return self.__good_name

    @good_name.setter
    def good_name(self, good_name):
        self.__good_name = good_name

    @property
    def shop_name(self):
        return self.__shop_name

    @shop_name.setter
    def shop_name(self, shop_name):
        self.__shop_name = shop_name

    @property
    def good_price(self):
        return self.__price

    @good_price.setter
    def good_price(self, price):
        self.__price = price


class Warehouse:

    def __init__(self, list_of_goods: list):
        self.__list_of_goods = list_of_goods
        self.__dict_of_goods = {}

        for el in self.__list_of_goods:
            self.__dict_of_goods[el.good_name] = [el.shop_name, el.good_price]


    @property
    def get_dict(self):
        return self.__dict_of_goods

    @property
    def get_list(self):
        return self.__list_of_goods

    def __str__(self):
        return self.__list_of_goods

    def get_good_info_per_index(self, index):
        good_info = [self.__list_of_goods[index].good_name,
                     self.__list_of_goods[index].shop_name,
                     self.__list_of_goods[index].good_price]
        return good_info

    def sort_data(self, sort_key):
        if sort_key == "name":
            self.__list_of_goods.sort(key=lambda x: x.good_name)
        elif sort_key == "price":
            self.__list_of_goods.sort(key=lambda x: x.good_price)
        elif sort_key == "shop":
            self.__list_of_goods.sort(key=lambda x: x.shop_name)

    def get_good_info_per_name(self, good_name):
        return self.__dict_of_goods[good_name]


good1 = Good("Pen", "Belbakaleia", 2000)

good2 = Good("Iphone", "TSUM", 1500)

good3 = Good("Tshirt", "Hutkasmachna", 1000)

warehouse = Warehouse([good1, good2, good3])

print(good2 + good3)


# task2
class BeeElephant:

    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    @property
    def get_beeandelephant_values(self):
        return f"Bee value = {self.bee}, Elephant value = {self.elephant}"

    def fly(self):
        return self.bee >= self.elephant

    def trumpet(self):
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzz"

    def eat(self, meal, value):
        meal = meal.lower()
        if meal not in ["nectar", "grass"]:
            print("Set correct meal")
        else:
            if meal == "nectar":
                if self.bee + value > 100:
                    print("Max value of bee is 100! Set correct value.")
                elif self.elephant - value < 0:
                    print("Min value of elephant is 0! Set correct value.")
                else:
                    self.elephant -= value
                    self.bee += value

            if meal == "grass":
                if self.elephant + value > 100:
                    print("Max value of elephant is 100! Set correct value.")
                elif self.bee - value < 0:
                    print("Min value of bee is 0! Set correct value.")
                else:
                    self.bee -= value
                    self.elephant += value


sanya = BeeElephant(50, 50)
print(sanya.get_beeandelephant_values)
sanya.eat("grass", 25)
print(sanya.fly())
print(sanya.trumpet())
print(sanya.get_beeandelephant_values)
sanya.eat("nectar", 80)
print(sanya.fly())
print(sanya.trumpet())
print(sanya.get_beeandelephant_values)


class Bus:

    def __init__(self, list_of_passengers, speed, max_seats, max_speed, free_seats, seats):
        self.__speed = speed
        self.__max_seats = max_seats
        self.__max_speed = max_speed
        self.__list_of_passengers = list_of_passengers
        self.__free_seats = free_seats
        self.__seats = seats
        if len(self.__list_of_passengers) <= self.__max_seats:
            self.__free_seats = True
        else:
            self.__free_seats = False

        for i in range(1, self.__max_seats + 1):  # Making a bus
            self.__seats[i] = None

        for i in range(len(self.__list_of_passengers)):  # Boarding
            seats[i + 1] = self.__list_of_passengers[i]

    @property
    def speed(self):
        return self.__speed

    @property
    def max_seats(self):
        return self.__max_seats

    @property
    def max_speed(self):
        return self.__max_speed

    @property
    def list_of_passangers(self):
        return self.__list_of_passengers

    @property
    def free_seats(self):
        return self.__free_seats

    @property
    def seats(self):
        return self.__seats

    def boarding(self, indicator, num_of_pass, names_of_pass):
        if indicator == "+":
            if len(self.__list_of_passengers) + len(names_of_pass) > self.__max_seats:
                print("You can't board more passengers than number of seats!")
            else:
                for _ in range(num_of_pass):
                    for passenger in names_of_pass:
                        self.__list_of_passengers.append(passenger)
                        for seat_num, passengers in self.__seats.items():
                            if self.__seats[seat_num] is None:
                                self.__seats[seat_num] = passenger
                                break

        if indicator == "-":
            if len(self.__list_of_passengers) - len(names_of_pass) < 0:
                print("There are less passengers than you want to unboard")
            else:
                for i in range(num_of_pass):
                    for seat_num, passenger in self.__seats.items():
                        if passenger in names_of_pass:
                            self.__seats[seat_num] = None
                            self.__list_of_passengers.remove(passenger)

    def bus_speed(self, indicator, value):
        if indicator == "up":
            if self.__speed + value > self.__max_speed:
                print(
                    f"Bus speed now is {self.__speed}. Max speed is {self.__max_speed}. You can't go {self.__speed + value}!")
            else:
                self.__speed += value
                print(f"The bus is moving faster. Bus speed now is {self.__speed}.")
        if indicator == "down":
            if self.__speed - value <= 0:
                self.__speed = 0
                print(f"Bus is stopped!")
            else:
                self.__speed -= value
                print(f"The bus is moving slower. Bus speed now is {self.__speed}.")

    def __isub__(self, other):
        if len(self.__list_of_passengers) == 0:
            print("There are less passengers than you want to unboard")
        elif isinstance(other, str):
            for seat_num, passenger in self.__seats.items():
                if passenger == other:
                    self.__seats[seat_num] = None
                    self.__list_of_passengers.remove(other)
                    break
        return self

    def __iadd__(self, other):
        if len(self.__list_of_passengers) == 10:
            print("You can't board more passengers than number of seats!")
        elif isinstance(other, str):
            for seat_num, passenger in self.__seats.items():
                self.__list_of_passengers.append(other)
                if passenger is None:
                    self.__seats[seat_num] = other
                    break
        return self

    def __contains__(self, item):
        if isinstance(item, str):
            if item in self.__list_of_passengers:
                print(f"Passenger {item} is in bus!")
            else:
                print(f"Passenger {item} is not in bus!")



bus1 = Bus(["Ivanov", "Petrov", "Sidorov", "Tsuba", "Erokhina"], 90, 10, 120, True, {})

print(bus1.seats)
print(bus1.list_of_passangers)
bus1.boarding("-", 1, ["Ivanov"])
print(bus1.seats)
print(bus1.list_of_passangers)
bus1.boarding("+", 1, ["Ivanov", "Pimenau"])
print(bus1.seats)
print(bus1.list_of_passangers)
bus1.bus_speed("up", 10)
bus1 -= "Ivanov"
print(bus1.seats)
print(bus1.list_of_passangers)
bus1 += "Ivanov"
print(bus1.seats)
print(bus1.list_of_passangers)
"Fedorov" in bus1