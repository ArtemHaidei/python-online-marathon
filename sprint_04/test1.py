# test 1
# class Employee:
#     def __init__(self, firstname, lastname, salary):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.salary = salary
#
#     @staticmethod
#     def from_string(string):
#        return Employee(*string.split('-')[:2], int(string.split('-')[-1]))
#
#
# emp1 = Employee("Mary", "Sue", 60000)
# emp2 = Employee.from_string("John-Smith-55000")
# print(emp1.firstname)
# print(emp1.salary)
# print(emp2.firstname)


# test 2
# class Pizza:
#     order_number = 1
#
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#         self.order_number = Pizza.order_number
#         Pizza.order_number += 1
#
#     @staticmethod
#     def garden_feast():
#         return Pizza(['spinach', 'olives', 'mushroom'])
#
#     @staticmethod
#     def meat_festival():
#         return Pizza(['beef', 'meatball', 'bacon'])
#
#     @staticmethod
#     def hawaiian():
#         return Pizza(['ham', 'pineapple'])
#
#
# p1 = Pizza(["bacon", "parmesan", "ham"])   # order 1
# p2 = Pizza.garden_feast()                  # order 2
# print(p1.ingredients) # ["bacon", "parmesan", "ham"]
# print(p2.ingredients) # ["spinach", "olives", "mushroom"]
# print(p1.order_number) # 1
# print(p2.order_number) # 2


# test 3
# class Employee:
#     def __init__(self, name, **kwargs):
#         self.name = name.split()[0]
#         self.lastname = name.split()[1]
#         if kwargs: [setattr(self, x, kwargs[x]) for x in kwargs]
#
#
#
# john = Employee("John Doe")
# mary = Employee("Mary Major", salary=120000)
# richard = Employee("Richard Roe", salary=110000, height=178)
# giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
# print(mary.lastname) # "Major"
# print(richard.height) # 178
# print(giancarlo.nationality) # "Italian"
# print(john.name) # "John


# test 4
# class Testpaper:
#     def __init__(self, subject, markscheme, pass_mark):
#         self.subject = subject
#         self.markscheme = markscheme
#         self.pass_mark = pass_mark
#
#
# class Student:
#     def __init__(self):
#         self.tests_taken = 'No tests taken'
#
#     def take_test(self, test, answer):
#         mark = round(len([*filter(lambda x: x in test.markscheme, answer)]) \
#                      * 100 / len(test.markscheme))
#
#         if not isinstance(self.tests_taken, dict):
#             self.tests_taken = {}
#
#         self.tests_taken[test.subject] = f'Passed! ({mark}%)' \
#             if mark >= int(test.pass_mark[:-1]) else f'Failed! ({mark}%)'
#
#
# paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
# paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
# paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")
#
# student1 = Student()
# student2 = Student()
# # print(student1.tests_taken) #"No tests taken"
# student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
# print(student1.tests_taken)  # {"Maths" : "Passed! (80%)"}
#
# student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
# student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
# print(student2.tests_taken)  # {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}


# test 5
class Gallows:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if not self.words:
            self.words.append(word)
            return self.words

        if word not in self.words and self.words[-1][-1] == word.lower()[0]:
            self.words.append(word)
            return self.words

        self.game_over = True
        return "game over"

    def restart(self):
        self.words = []
        self.game_over = False
        return "game restarted"

class Ab:
    def __init__(self):
        self.a = 100

    def get(self):
        pass

class B(Ab):
    def __init__(self):
        Ab.__init__(self)


a = Ab()
b = B()
print(b.a)























