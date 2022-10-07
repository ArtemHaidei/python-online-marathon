#test 1
# def outer(name):
#     def inner():
#         print(f'Hello, {name}!')
#
#     return inner


#test 2
#def create(string1): return lambda string2: string1 == string2


#test 3
from re import search


# def create_account(user_name: str, password: str, secret_words: list):
#     if len([x for x in [r'[a-z]', r'[A-Z]', r'[0-9]', r'[^a-zA-Z0-9]'] if search(x, password)]) != 4 \
#             or len(password) < 6:
#         raise ValueError
#
#     def check(check_pasword, check_words):
#         if check_pasword != password:
#             return False
#
#         if len(check_words) != len(secret_words):
#             return False
#
#         [check_words.remove(x) for x in secret_words if x in check_words]
#         if len(check_words) > 1:
#             return False
#
#         return True
#     return check
#
#
# tom = create_account("Tom", "Qwerty1_", ["1", "word"])
# check1 = tom("Qwerty1_", ["1", "word"])
# check2 = tom("Qwerty1_", ["word"])
# check3 = tom("Qwerty1_", ["word", "2"])
# check4 = tom("Qwerty1!", ["word", "12"])


#test 4
# def divisor(n):
#     return iter([x for x in range(1, n + 1) if n % x == 0] + [None, None])
#
# three = divisor(3)
# print(next(three))
# print(next(three))
# print(next(three))


#test 5
# def logger(func):
#     def wrapper(*args, **kwargs):
#         lst = [str(x) for x in args]
#         if kwargs: lst += [str(x) for x in kwargs.values()]
#
#         if func(*args, **kwargs) is None:
#             print(f'Executing of function {func.__name__} with arguments {", ".join(lst)}...')
#             return
#         print(f'Executing of function {func.__name__} with arguments {", ".join(lst)}...')
#         return func(*args, **kwargs)
#     return wrapper
# #
# #
# @logger
# def concat(*args, **kwargs):
#     lst = [str(x) for x in args]
#     if kwargs: lst += [str(x) for x in kwargs.values()]
#     return ''.join(lst)
#
#
# @logger
# def sum(a, b):
#     return a + b
#
#
# @logger
# def print_arg(arg):
#     print(arg)
#
#
# print(concat(1))
# print(concat('first string', second=2, third='second string'))
# print(concat('first string', {'first kwarg' :0, 'second kwarg': 'second kwarg'}))
# print(sum(2, 3))
# print_arg(2)


#test 6
from random import shuffle


# def randomWord(lst):
#     if not lst:
#         lst += [None]
#
#     shuffle(lst)
#     for x in lst:
#         yield x
#
#     for x in randomWord(lst):
#         yield x


# def randomWord(a):
#     if not a:
#         yield
#
#     shuffle(a)
#     lst = iter(a)
#     index = 0
#
#     while True:
#         if index < len(a):
#             yield next(lst)
#             index += 1
#         else:
#             shuffle(a)
#             lst = iter(a)
#             index = 0