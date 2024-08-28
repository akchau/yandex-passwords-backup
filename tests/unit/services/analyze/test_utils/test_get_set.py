import unittest

from src.services.analyze.algorythms import CompareListRecordAlgorythm
from src.services.analyze.analyze_exceptions import AnalyzeException


class TestGetSetCutPasswords(unittest.IsolatedAsyncioTestCase):

    def test_good_case_depth_two(self):
        test_values = [
            (
                [
                    ("one", "two", "three"),
                    ("one", "two", "four"),
                    ("one_two", "two_one", "three"),
                    ("one", "two", "three"),
                    ("one", "two", "four"),
                    ("one", "two", "four"),
                    ("three", "four", "five"),
                ],
                {
                    ('one', 'two'),
                    ('one_two', 'two_one'),
                    ('three', 'four')}

            )
        ]

        for value, result in test_values:
            self.assertEqual(CompareListRecordAlgorythm()._get_set(value, depth=2), result)

    def test_good_case_depth_three(self):
        test_values = [
            (
                [
                    ("one", "two", "three"),
                    ("one", "two", "four"),
                    ("one_two", "two_one", "three"),
                    ("one", "two", "three"),
                    ("one", "two", "four"),
                    ("one", "two", "four"),
                    ("three", "four", "five"),
                ],
                {
                    ('one', 'two', 'four'),
                    ('three', 'four', 'five'),
                    ('one', 'two', 'three'),
                    ('one_two', 'two_one', 'three')
                }

            )
        ]

        for value, result in test_values:
            print(CompareListRecordAlgorythm()._get_set(value, depth=3))
            self.assertEqual(CompareListRecordAlgorythm()._get_set(value, depth=3), result)

    def test_good_case_depth_too_much(self):
        with self.assertRaises(AnalyzeException):
            CompareListRecordAlgorythm()._get_set([("one", "two", "three")], depth=4)
