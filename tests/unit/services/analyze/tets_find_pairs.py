import unittest

from src.services.analyze.analyze_types import PairResult
from src.services.analyze.password_analyzer_utils import PasswordAnalyzerUtils


class TestFindPairs(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.utils = PasswordAnalyzerUtils()

    def test_good_case_with_pairs(self):
        test_data_yandex = [
            ("one", "two", "three"),
            ("one", "two", "four"),
            ("three", "four", "five"),
            ("apple", "orange", "banana"),
        ]

        test_data_google = [
            ("one", "two", "three"),
            ("one", "two", "four"),
            ("good", "bad", "neutral"),
        ]

        self.assertEqual(
            self.utils.find_pairs(
                yandex_passwords=test_data_yandex,
                google_passwords=test_data_google,
            ),
            PairResult(
                google=[
                    ("one", "two", "three"),
                    ("one", "two", "four"),

                ],
                yandex=[
                    ("one", "two", "three"),
                    ("one", "two", "four"),
                ]
            )
        )

    def test_good_case_without_pairs(self):
        test_data_yandex = [
            ("three", "four", "five"),
            ("apple", "orange", "banana"),
        ]

        test_data_google = [
            ("one", "two", "four"),
            ("good", "bad", "neutral"),
        ]

        self.assertEqual(
            self.utils.find_pairs(
                yandex_passwords=test_data_yandex,
                google_passwords=test_data_google,
            ),
            PairResult(
                google=[],
                yandex=[]
            )
        )
