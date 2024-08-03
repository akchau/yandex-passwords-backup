import unittest

from src.services.analyze.analyze_types import AnalyzeResult
from src.services.analyze.core import PasswordAnalyzer


class TestAnalyze(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.analyzer = PasswordAnalyzer()

    def test_good_case_good_pair(self):
        test_yandex_passwords = [
            ("one", "twon", "three"),
            ("one", "two", "four"),
        ]

        test_google_password = [
            ("one", "twon", "three"),
            ("one", "two", "four"),
        ]
        self.assertEqual(
            self.analyzer.analyze(
                yandex_passwords=test_yandex_passwords,
                google_passwords=test_google_password
            ),
            AnalyzeResult(
                yandex_not_pair=[],
                google_not_pair=[],
                yandex_repeats=[],
                google_repeats=[],
                pair_result=[
                    ("one", "twon", "three"),
                    ("one", "two", "four"),
                ]
            )
        )


    # def test_good_case_repeats(self):
    #     test_yandex_passwords = [
    #         ("one", "two", "three"),
    #         ("one", "two", "four"),
    #     ]
    #
    #     test_google_password = [
    #         ("one", "two", "three"),
    #         ("one", "two", "four"),
    #     ]
    #     self.assertEqual(
    #         self.analyzer.analyze(
    #             yandex_passwords=test_yandex_passwords,
    #             google_passwords=test_google_password
    #         ),
    #         AnalyzeResult(
    #             yandex_not_pair=[],
    #             google_not_pair=[],
    #             yandex_repeats=[],
    #             google_repeats=[],
    #             pair_result=[
    #                 ("one", "two", "three"),
    #                 ("one", "two", "four"),
    #             ]
    #         )
    #     )