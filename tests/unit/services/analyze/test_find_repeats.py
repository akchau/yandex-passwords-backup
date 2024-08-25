# import unittest
#
# from src.services.analyze.handlers import PasswordAnalyzerUtils
#
#
# class TestFindRepeats(unittest.IsolatedAsyncioTestCase):
#
#     def setUp(self):
#         self.utils = PasswordAnalyzerUtils()
#
#     def test_good_case_with_repeats(self):
#         """
#         С повторами.
#         """
#         test_data = [
#             ("one", "two", "three"),
#             ("one", "two", "four"),
#             ("one_two", "two_one", "three"),
#             ("one", "two", "three"),
#             ("one", "two", "four"),
#             ("one", "two", "four"),
#             ("three", "four", "five"),
#         ]
#         self.assertEqual(
#             self.utils.find_repeats(data=test_data),
#             [
#                 ('one', 'two', 'four'),
#                 ('one', 'two', 'three'),
#                 ('one', 'two', 'four'),
#                 ('one', 'two', 'four')
#             ]
#         )
#
#     def test_good_case_without_repeats(self):
#         """
#         С повторами.
#         """
#         test_data = [
#             ("one", "two", "three"),
#             ("one_two", "two_one", "three"),
#             ("three", "four", "five"),
#         ]
#         self.assertEqual(self.utils.find_repeats(data=test_data),[])