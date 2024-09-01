import unittest

from src.services.analyze.algorythms import CompareListRecordAlgorythm


class TestFindFirstInSecond(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.algorythm = CompareListRecordAlgorythm()

    def test_good_case_depth_2_true(self):
        result = self.algorythm._item_in_second(
            item=("one", "two", "three"),
            list_of_records=[
                ("one", "two", "four")
            ],
            depth=2
        )
        self.assertEqual(result, True)

    def test_good_case_depth_2_false(self):
        result = self.algorythm._item_in_second(
            item=("one", "two", "three"),
            list_of_records=[("one", "four", "two")],
            depth=2
        )
        self.assertEqual(result, False)

    def test_good_case_depth_3_false(self):
        test_data = [
            (
                ("one", "two", "three"),
                [("one", "two", "four")]

            ),
            (
                ("one", "three", "two"),
                [("one", "two", "three")]

            )
        ]
        for data, list_of_records, in test_data:
            result = self.algorythm._item_in_second(
                item=data,
                list_of_records=list_of_records,
                depth=3
            )
            self.assertEqual(result, False)

    def test_good_case_depth_3_true(self):
        test_data = [
            (
                ("one", "two", "three"),
                [("one", "two", "three")]

            ),
            (
                ("seven", "eight", "nine"),
                [
                    ("ten", "eleven", "twelwe"),
                    ("odin", "dva", "tri"),
                    ("seven", "eight", "nine")
                ]

            )
        ]
        for data, list_of_records, in test_data:
            result = self.algorythm._item_in_second(
                item=data,
                list_of_records=list_of_records,
                depth=3
            )
            self.assertEqual(result, True)