# test 1
# class Product:
#     @classmethod
#     def cook(cls):
#         print(cls.__doc__)
#
#
# class Factory:
#     @staticmethod
#     def get_dish(type_of_meal):
#         pass
#
#
# class FactoryProducer:
#     @staticmethod
#     def get_factory(type_of_factory):
#         return {'italian': ItalianDishesFactory(), 'french': FrenchDishesFactory()}[type_of_factory]
#
#
# class ItalianDishesFactory(Factory):
#     @staticmethod
#     def get_dish(type_of_meal):
#         return {'main': FettuccineAlfredo(), 'dessert': Tiramisu()}[type_of_meal]
#
#
# class FrenchDishesFactory(Factory):
#     @staticmethod
#     def get_dish(type_of_meal):
#         return {'main': DuckALOrange(), 'dessert': CremeBrulee()}[type_of_meal]
#
#
# class FettuccineAlfredo(Product):
#     """Italian main course prepared: Fettuccine Alfredo"""
#
#
# class Tiramisu(Product):
#     """Italian dessert prepared: Tiramisu"""
#
#
# class DuckALOrange(Product):
#     """French main course prepared: Duck À L'Orange"""
#
#
# class CremeBrulee(Product):
#     """French dessert prepared: Crème brûlée"""


# test 2
# class Goods:
#     def __init__(self, price, discount_strategy=None):
#         self.price = price
#         self.discount_strategy = discount_strategy(price) if discount_strategy else price
#
#     def __str__(self):
#         return self.price_after_discount()
#
#     def price_after_discount(self):
#         return f'Price: {self.price}, price after discount: {self.discount_strategy}'
#
#
# def on_sale_discount(order):
#     return order / 2
#
#
# def twenty_percent_discount(order):
#     return order * 0.2


# test 3
# class MotorCycle:
#     def __init__(self):
#         self.name = "MotorCycle"
#
#     def TwoWheeler(self):
#         return "TwoWheeler"
#
#
# class Truck:
#     def __init__(self):
#         self.name = "Truck"
#
#     def EightWheeler(self):
#         return 'EightWheeler'
#
#
# class Car:
#     def __init__(self):
#         self.name = "Car"
#
#     def FourWheeler(self):
#         return 'FourWheeler'
#
#
# class Adapter:
#     def __init__(self, obj, **adapted_methods):
#         """We set the adapted methods in the object's dict"""
#         self.objects_dict = {'name': obj, 'wheels': adapted_methods}
#
#     def __getattr__(self, attr):
#         return getattr(self.objects_dict[attr], attr) if attr == 'name' else self.objects_dict[attr][attr]
#
#     def original_dict(self):
#         print(self.objects_dict)


# test 4
class Washing:
    """Washing..."""


class Rinsing:
    """Rinsing..."""


class Spinning:
    """Spinning..."""


class WashingMachine(Washing, Rinsing, Spinning):
    def __init__(self):
        self.startWashing()

    @classmethod
    def startWashing(cls):
        for x in cls.__mro__[1:-1]:
            print(x.__doc__)


# test 5
class LeafElement:
    def __init__(self, *args):
        self.position = args[0]

    def showDetails(self):
        print(end='\t')
        print(self.position)


class CompositeElement:
    def __init__(self, *args):
        self.position = args[0]
        self.children = []

    def add(self, child):
        self.children += [child]

    def remove(self, child):
        self.children.remove(child)

    def showDetails(self):
        print(self.position)
        for x in self.children:
            print(end='\t')
            x.showDetails()

