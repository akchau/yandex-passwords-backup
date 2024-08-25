# import unittest
#
# from src.services.analyze.handlers import PasswordAnalyzerUtils
#
#
# class TestCleanRepeats(unittest.IsolatedAsyncioTestCase):
#
#     def setUp(self):
#         self.utils = PasswordAnalyzerUtils()

#
#     def test_good_case_without_repeats_in_domain_login(self):
#         """
#         C отличием только в пароле.
#         """
#         test_data = [
#             ('one', 'two', 'three'),
#             ('one', 'two', 'four'),
#             ('one_two', 'two_one', 'three'),
#             ('three', 'four', 'five')
#         ]
#         self.assertEqual(
#             self.utils._clean_repeats(data=test_data),
#             [
#                 ('one', 'two', 'three'),
#                 ('one_two', 'two_one', 'three'),
#                 ('three', 'four', 'five')
#
#             ]
#         )
#
#     def test_good_case_with_empty(self):
#         """
#         Тест с пустым словарем.
#         """
#         test_data = []
#         self.assertEqual(self.utils._clean_repeats(data=test_data), [])
#
#     def test_good_case_without_repeats_but_inversion(self):
#         """
#         Cлучай когда нет одинаковых, но если поменять местами, то будут одинаковые.
#         """
#         test_data = [
#             ('one', 'two', 'three'),
#             ('two', 'one', 'four'),
#             ('one_two', 'two_one', 'three'),
#             ('three', 'four', 'five')
#         ]
#         self.assertEqual(
#             self.utils._clean_repeats(data=test_data),
#             [
#                 ('one', 'two', 'three'),
#                 ('two', 'one', 'four'),
#                 ('one_two', 'two_one', 'three'),
#                 ('three', 'four', 'five')
#
#             ]
#         )