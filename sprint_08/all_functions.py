import unittest


# task 1
# class Product:
#     def __init__(self, name, price, count):
#         self.name, self.price, self.count = name, price, count
#         self.all_sum = price * count
#
#     def discount_price(self):
#         discount_dict = {0: 1, 5: 0.05, 7: 0.1, 10: 0.2, 20: 0.3, 21: 0.5}
#         key = max(filter(lambda x: x <= self.count, discount_dict)) if self.count <= 20 else 21
#         return self.all_sum - self.all_sum * discount_dict[key] if key >= 5 else self.all_sum
#
#
# class Cart:
#     def __init__(self, lst):
#         self.products = list(lst)
#
#     def get_total_price(self):
#         return sum([x.discount_price() for x in self.products])


# task 2
# def divide(num_1, num_2):
#     return float(num_1) / num_2


# task 3
# def quadratic_equation(a, b, c):
#     if not a:
#         raise ValueError
#     D = b ** 2 - 4 * a * c
#     if D >= 0:
#         x1 = (-b - D ** 0.5) / (2 * a)
#         x2 = (-b + D ** 0.5) / (2 * a)
#         result = tuple({round(x1, 3), round(x2, 3)})
#         return result[0] if len(result) == 1 else result


# task 4
# class TriangleNotValidArgumentException(Exception):
#     def __str__(self):
#         return 'Not valid arguments'
#
#
# class TriangleNotExistException(Exception):
#     def __str__(self):
#         return 'Can`t create triangle with this arguments'
#
#
# class Triangle:
#     def __init__(self, lst):
#         self.valid_arguments(lst)
#         self.area = self.calc_area(lst[0], lst[1], lst[2])
#
#     def get_area(self):
#         return self.area
#
#     @staticmethod
#     def calc_area(a, b, c):
#         p = (a + b + c) / 2
#         area = str((p * (p - a) * (p - b) * (p - c)) ** 0.5).split('.')
#         return float(area[0] + '.' + area[1][0:2])
#
#     @staticmethod
#     def valid_arguments(lst):
#         if not isinstance(lst, (tuple, list)) or len(lst) != 3\
#                 or not all([type(num) in (int, float) for num in lst]):
#             raise TriangleNotValidArgumentException
#
#         a, b, c = lst
#         if not all([a + b > c, a + c > b, c + b > a]):
#             raise TriangleNotExistException


# test 5
# class Worker:
#     def __init__(self, name, salary=0.0):
#         if salary < 0:
#             raise ValueError
#         self.name = name
#         self.salary = salary
#
#     def get_tax_value(self):
#         if self.salary <= 1000:
#             return 0.0
#
#         tax = {1000: 0, 3000: 0.1, 5000: 0.15, 10000: 0.21, 20000: 0.3, 50000: 0.4, 'max': 0.47}
#         result = prev = 0
#         salary = self.salary
#         for key in tax:
#             if type(key) != str and salary > key:
#                 result += (key - prev) * tax[key]
#                 salary = salary - (key - prev)
#                 prev = key
#             else:
#                 return result + salary * tax[key]


# test 6 / sprint_08
def file_parser(path_, find_, replace_=None):
    count = 0
    if replace_:
        with open(path_, 'w') as file:
            for line in file:
                if find_ in line:
                    line.replace(find_, replace_, line.count(find_))
                    count += 1
        return f'Replaced {count} strings'
    else:
        with open(path_) as file:
            for line in file:
                if find_ in line:
                    count += line.count(find_)
        return f'Found {count} strings'
