import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def price(self):
        return self.__price


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price * increment_value

    @classmethod
    def instantiate_from_class(cls):
        with open('item.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

        for item in items:
            Item(name=item.get('name'), price=item.get('__price'), quantity=item.get('quantity'))

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{Item.__class__.__name__}('{self.__name}', {self.__price}, {self.quantity})"
