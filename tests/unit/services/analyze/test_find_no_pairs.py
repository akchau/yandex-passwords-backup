import unittest

from src.services.analyze.analyze_types import NotPairResult
from src.services.analyze.handlers import PasswordAnalyzerUtils


class TestFindNoPairs(unittest.IsolatedAsyncioTestCase):

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
            self.utils.find_not_pairs(
                yandex_passwords=test_data_yandex,
                google_passwords=test_data_google,
            ),
            NotPairResult(
                google=[
                    ("good", "bad", "neutral")

                ],
                yandex=[
                    ("three", "four", "five"),
                    ("apple", "orange", "banana")
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
            self.utils.find_not_pairs(
                yandex_passwords=test_data_yandex,
                google_passwords=test_data_google,
            ),
            NotPairResult(
                google=[
                    ("one", "two", "four"),
                    ("good", "bad", "neutral"),
                ],
                yandex=[
                    ("three", "four", "five"),
                    ("apple", "orange", "banana"),
                ]
            )
        )
