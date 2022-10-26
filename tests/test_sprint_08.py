import unittest
from unittest.mock import patch, mock_open
# from sprint_08.all_functions import Cart, Product
# from sprint_08.all_functions import divide
# from sprint_08.all_functions import quadratic_equation
# from sprint_08.all_functions import Triangle, TriangleNotExistException, TriangleNotValidArgumentException
from sprint_08.all_functions import Worker
# from sprint_08.all_functions import file_parser


# task 1 / sprint_08
# class CartTest(unittest.TestCase):
#     def test_discount_0(self):
#         prod = Product('p1', 10, 4)
#         self.assertEqual(prod.discount_price(), 40)
#
#     def test_discount_10(self):
#         prod = Product('p1', 500, 10)
#         self.assertEqual(prod.discount_price(), 4000)
#
#     def test_discount_more_20(self):
#         prod = Product('p7', 1000, 25)
#         self.assertEqual(prod.discount_price(), 12500)


# task 2 / sprint_08
# class DivideTest(unittest.TestCase):
#     def test_divide_5_2(self):
#         self.assertEqual(divide(5, 2), 2.5)
#
#     def test_divide_str_num_1(self):
#         self.assertEqual(divide('13.5', 3), 4.5)
#
#     def test_divide_zero_division_error(self):
#         with self.assertRaises(ZeroDivisionError):
#             divide(75, 0)
#
#     def test_divide_type_error(self):
#         with self.assertRaises(TypeError):
#             divide(10, '4')

# task 3 / sprint_08
# class QuadraticEquationTest(unittest.TestCase):
#     def test_quadratic_equation_equal_0(self):
#         self.assertEqual(quadratic_equation(1, 2, 1), -1)
#
#     def test_quadratic_equation_more_than_0(self):
#         self.assertEqual(quadratic_equation(-1, 3, 1), (-0.303, 3.303))
#
#     def test_quadratic_equation_less_than_0(self):
#         self.assertEqual(quadratic_equation(2, 2, 1), None)
#
#     def test_quadratic_equation_value_error(self):
#         with self.assertRaises(ValueError):
#             quadratic_equation(0, 2, 1)


# task 4 / sprint_08
# class TriangleTest(unittest.TestCase):
#     def test_valid_test_data(self):
#         valid_test_data = [
#             ((3, 4, 5), 6.0),
#             ((10, 10, 10), 43.3),
#             ((6, 7, 8), 20.33),
#             ((7, 7, 7), 21.21),
#             ((50, 50, 75), 1240.19),
#             ((37, 43, 22), 406.99),
#             ((26, 25, 3), 36.0),
#             ((30, 29, 5), 72.0),
#             ((87, 55, 34), 396.0),
#             ((120, 109, 13), 396.0),
#             ((123, 122, 5), 300.0)
#         ]
#         for x in valid_test_data:
#             with self.subTest(x=x):
#                 self.assertEqual(Triangle(x[0]).area, x[1])
#
#     def test_not_valid_triangle(self):
#         not_valid_triangle = [
#             (1, 2, 3),
#             (1, 1, 2),
#             (7, 7, 15),
#             (100, 7, 90),
#             (17, 18, 35),
#             (127, 17, 33),
#             (145, 166, 700),
#             (1000, 2000, 1),
#             (717, 17, 7),
#             (0, 7, 7),
#             (-7, 7, 7),
#         ]
#         for x in not_valid_triangle:
#             with self.subTest(x=x):
#                 self.assertRaises(TriangleNotExistException, Triangle, x)
#
#     def test_not_valid_arguments(self):
#         not_valid_arguments = [
#             ('3', 4, 5),
#             ('a', 2, 3),
#             (7, "str", 7),
#             ('1', '1', '1'),
#             'string',
#             (7, 2),
#             (7, 7, 7, 7),
#             'str',
#             10,
#             ('a', 'str', 7)
#         ]
#         for x in not_valid_arguments:
#             with self.subTest(x=x):
#                 self.assertRaises(TriangleNotValidArgumentException, Triangle, x)


# test 5 / sprint_08
class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.work1 = Worker('Dima', 1000)
        self.work2 = Worker('Kostya', 50000)
        self.work3 = Worker('Lia', 5001)
        self.work4 = Worker('Nastia', 2999)
        self.work5 = Worker('Camelia', 55000)
        self.work6 = Worker('Rita')

    def tearDown(self):
        pass

    def test_worker_get_tax_value_work1(self):
        self.assertEqual(self.work1.get_tax_value(), 0.0)

    def test_worker_get_tax_value_work2(self):
        self.assertEqual(self.work2.get_tax_value(), 16550.0)

    def test_worker_get_tax_value_work3(self):
        self.assertEqual(self.work3.get_tax_value(), 500.15)

    def test_worker_get_tax_value_work4(self):
        self.assertEqual(self.work4.get_tax_value(), 199.9)

    def test_worker_get_tax_value_work5(self):
        self.assertEqual(self.work5.get_tax_value(), 18550.0)

    def test_worker_get_tax_value_work6(self):
        self.assertEqual(self.work6.get_tax_value(), 0.0)

    # @unittest.expectedFailure
    # def test_worker_except(self):
    #     Worker('Max', -500)


# test 6 / sprint_08
# class ParserTest(unittest.TestCase):
#     def setUp(self):
#         self.file_content_mock = """Hello World!!
# Hello World is in a file.
# A mocked file.
# He is not real.
# But he think he is.
# He doesn't know he is mocked"""
#         self.fake_file_path = 'file/path/mock'
#
#     def test_file_parser_count_strings(self):
#         with patch('builtins.open', mock_open(read_data=self.file_content_mock)) as file:
#             actual = file_parser(self.fake_file_path, 'is')
#             file.assert_called_once_with(self.fake_file_path, 'r')
#
#         expected = 'Found 4 strings'
#         self.assertEqual(expected, actual)
#
#     def test_file_parser_count_replace_strings(self):
#         with patch('builtins.open', mock_open(read_data=self.file_content_mock)) as file:
#             actual = file_parser(self.fake_file_path, 'is', 'are')
#             file.assert_called_once_with(self.fake_file_path, 'r+')
#         expected = 'Replaced 4 strings'
#         self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
