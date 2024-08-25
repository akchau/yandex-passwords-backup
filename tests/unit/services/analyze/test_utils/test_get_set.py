import unittest

from src.services.analyze.utils import get_set


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
                    ('four', 'three'),
                    ('one_two', 'two_one'),
                    ('one', 'two')
                }

            )
        ]

        for value, result in test_values:
            self.assertEqual(get_set(value, depth=2), result)

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
                    ('five', 'four', 'three'),
                    ('one_two', 'three', 'two_one'),
                    ('one', 'three', 'two'),
                    ('four', 'one', 'two'),

                }

            )
        ]

        for value, result in test_values:
            self.assertEqual(get_set(value, depth=3), result)
