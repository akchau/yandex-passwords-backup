import unittest

from src.services.analyze.algorythms import CompareListRecordAlgorythm


class FindInSecond(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.algorythm = CompareListRecordAlgorythm()

    def test_good_case(self):
        TEST_DATA = [
            (
                [
                    ("one", "two", "three"),
                    ("four", "five", "six"),
                    ("seven", "eight", "nine")
                ],
                [
                    ("ten", "eleven", "twelwe"),
                    ("odin", "dva", "tri"),
                    ("seven", "eight", "nine")
                ],
                [
                    ("seven", "eight", "nine"),
                ]
            )
        ]
        for data_first, data_second, expected_result in TEST_DATA:
            result = self.algorythm.find_first_in_second(
                data_first, data_second, 3
            )
            self.assertEqual(result, expected_result)