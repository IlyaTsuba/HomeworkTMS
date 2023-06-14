# task1
class Good:

    def __init__(self, good_name, shop_name, price):
        self.__good_name = good_name
        self.__shop_name = shop_name
        self.__price = price

    def __str__(self):
        return f"{self.__good_name} {self.__shop_name} {self.__price}"

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

    def __repr__(self):
        return f'{self.good_name}, {self.shop_name}, {self.good_price}'


class Warehouse:

    def __init__(self, list_of_goods: list):
        self.__list_of_goods = list_of_goods
        self.__dict_of_goods = {}

        for el in self.__list_of_goods:
            self.__dict_of_goods[el.good_name] = [el.shop_name, el.good_price]

    def __add__(self, other):
        sum_of_goods = 0
        for el in other:
            sum_of_goods += self.__dict_of_goods[el][1]
        return sum_of_goods

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

