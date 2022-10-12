# test 1
# import re
#
#
# def valid_email(email):
#     try:
#         check_re = r'[\w]{3,}@[a-z]{3,}(\.[a-z]{2,})?\.[a-z]{2,3}'
#         if not re.match(check_re, email):
#             raise Exception
#     except:
#         return "Email is not valid"
#     else:
#         return "Email is valid"


# test 2
# def check_odd_even(number):
#     try:
#         return "Entered number is even" if number % 2 == 0 else "Entered number is odd"
#     except:
#         return "You entered not a number."


# test 3
# class ToSmallNumberGroupError(Exception):
#     def __str__(self):
#         return "We obtain error: Number of your group can't be less than 10"
#
#
# def check_number_group(number):
#     try:
#         if int(number) > 10:
#             return f"Number of your group {number} is valid"
#         raise ToSmallNumberGroupError
#     except ToSmallNumberGroupError:
#         return "We obtain error:Number of your group can't be less than 10"
#     except:
#         return "You entered incorrect data. Please try again."


# test 4
# def divide(numerator, denominator):
#     try:
#         return f'Result is {numerator / denominator}'
#     except ZeroDivisionError:
#         return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
#     except TypeError:
#         return "Value Error! You did not enter a number!"


# test 5
# class MyError(ValueError):
#     pass
#
#
# def check_positive(number):
#     try:
#         if isinstance(number, str): number = float(number)
#
#         if number >= 0:
#             return f"You input positive number: {number}"
#         raise MyError
#     except MyError:
#         return f"You input negative number: {float(number)}. Try again."
#     except ValueError:
#         return "Error type: ValueError!"
#
#
# print(check_positive(24))      # "You input positive number: 24"
# print(check_positive(-19))     # "You input negative number: -19. Try again."
# print(check_positive("38"))    # "You input positive number: 38"
# print(check_positive("abc"))   # "Error type: ValueError!"


# test 6
# def day_of_week(day):
#     try:
#         if int(day) <= 0:
#             raise IndexError
#         return ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][int(day) - 1]
#     except IndexError:
#         return "There is no such day of the week! Please try again."
#     except ValueError:
#         return "You did not enter a number! Please try again."


# test 7
# import cmath
#
#
# def solve_quadric_equation(a, b, c):
#     try:
#         if a in ('0', 0):
#             raise ZeroDivisionError
#         a, b, c = [float(x) if isinstance(x, str) else x for x in (a, b, c)]
#         D = b ** 2 - 4 * a * c
#         x1 = (-b - D ** 0.5) / (2 * a)
#         x2 = (-b + D ** 0.5) / (2 * a)
#         return f"The solution are x1={x1} and x2={x2}"
#     except ZeroDivisionError:
#         return "Zero Division Error"
#     except ValueError:
#         return "Could not convert string to float"




