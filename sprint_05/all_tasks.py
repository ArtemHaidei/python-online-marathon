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
#
#
# # test 3
# class ToSmallNumberGroupError(Exception):
#     def __str__(self):
#         return "We obtain error:Number of your group can't be less than 10"
#
#
# def check_number_group(number):
#     try:
#         if int(number) > 10:
#             return f"Number of your group {number} is valid"
#         raise ToSmallNumberGroupError
#     except ToSmallNumberGroupError as string:
#         return string
#     except:
#         return "You entered incorrect data. Please try again."
#
#
# print(check_number_group(0.8))


# test 4
# def divide(numerator, denominator):
#     try:
#         return f'Result is {numerator / denominator}'
#     except ZeroDivisionError:
#         return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
#     except TypeError:
#         return "Value Error! You did not enter a number!"
#
#
# # test 5
# class MyError(ValueError):
#     def __str__(self):
#         return "Error type: ValueError!"
#
#
# def check_positive(number):
#     try:
#         if str(number).isalpha():
#             raise MyError
#
#         return f"You input positive number: {float(number)}" if '-' not in str(number) \
#             else f"You input negative number: {float(number)}. Try again."
#     except MyError as string:
#         return string
#
#
# print(check_positive("32"))
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
#         return ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')[int(day) - 1]
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
#         if not a:
#             raise ZeroDivisionError
#         D = b ** 2 - 4 * a * c
#         x1 = (-b - cmath.sqrt(D)) / (2 * a)
#         x2 = (-b + cmath.sqrt(D)) / (2 * a)
#         return f"The solution are x1={x1} and x2={x2}"
#     except ZeroDivisionError:
#         return "Zero Division Error"
#     except TypeError:
#         return "Could not convert string to float"
#
#
# print(solve_quadric_equation(1, 3, -4))


# with open('name.txt', 'r') as f:
#     print(f.)
