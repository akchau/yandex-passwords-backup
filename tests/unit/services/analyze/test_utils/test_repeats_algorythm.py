import unittest

from src.services.analyze.algorythms import RepeatsAlgorythm


class TestFindRepeats(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.repeats_algo = RepeatsAlgorythm()

    def test_good_case_unique(self):
        test_data = [
            (
                [
                    [
                        ("one", "two", "three"),
                        ("one", "two", "four"),
                    ]
                ],
                [
                    [
                        ("one", "two", "three")
                    ]
                ]
            )
        ]
        for test_item, expected_result in test_data:
            self.assertEqual(self.repeats_algo.find_repeats(data=test_item, unique=True), expected_result)