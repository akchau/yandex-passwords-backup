import unittest

from src.services.analyze import PasswordAnalyzer
from src.services.analyze.analyze_types import AnalyzerInputData, ServiceData, AnalyzeResult, CheckResult, \
    AnalyzerMethods

TEST_STRONG_PASSWORD_ONE = "JEhfk-hewjfd98jk7-ejkb8j"
TEST_WEAK_PASSWORD_TWO = "test"
TEST_STRONG_PASSWORD_THREE = "JEhfk-hewjfd98jk7-ejkb8k"
TEST_STRONG_PASSWORD_FOUR = "JEhfk-hewjfd98jk7-ejkb8l"
TEST_SERVICE_ONE_NAME = "service_one"
TEST_SERVICE_TWO_NAME = "service_two"
TEST_RECORD_1_STRONG = ("url.ru", "login1", TEST_STRONG_PASSWORD_ONE)
TEST_RECORD_1_STRONG_ANOTHER_PASS = ("url.ru", "login1", TEST_STRONG_PASSWORD_FOUR)
TEST_RECORD_2_WEAK = ("url.ru", "login1", TEST_WEAK_PASSWORD_TWO)
TEST_RECORD_3_STRONG = ("url.ru", "login3", TEST_STRONG_PASSWORD_THREE)


class TestAnalyze(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.analyzer = PasswordAnalyzer()

    def test_good_case_with_repeat(self):

        result = self.analyzer.analyze(
            data=AnalyzerInputData(
                input_data=(
                    ServiceData(
                        service_name=TEST_SERVICE_ONE_NAME,
                        data=[
                            TEST_RECORD_1_STRONG,
                            TEST_RECORD_1_STRONG
                        ]
                    ),
                    ServiceData(
                        service_name=TEST_SERVICE_TWO_NAME,
                        data=[
                            TEST_RECORD_1_STRONG,
                        ]
                    )
                )
            ))
        expected_result = AnalyzeResult(
            analyze_result=[
                CheckResult(
                    analyze_method=AnalyzerMethods.REPEATS_CHECK,
                    service_name=TEST_SERVICE_ONE_NAME,
                    data=[TEST_RECORD_1_STRONG]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.REPEATS_CHECK,
                    service_name=TEST_SERVICE_TWO_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.WEAK_PASSWORD_CHECK,
                    service_name=TEST_SERVICE_ONE_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.WEAK_PASSWORD_CHECK,
                    service_name=TEST_SERVICE_TWO_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.NOT_PAIR_CHECK,
                    service_name=TEST_SERVICE_ONE_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.NOT_PAIR_CHECK,
                    service_name=TEST_SERVICE_TWO_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.PAIR_WITH_ANOTHER_PASSWORD_CHECK,
                    service_name=TEST_SERVICE_ONE_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.PAIR_WITH_ANOTHER_PASSWORD_CHECK,
                    service_name=TEST_SERVICE_TWO_NAME,
                    data=[]
                )
            ]
        )
        self.assertEqual(result, expected_result)

    def test_good_case_with_weak(self):

        result = self.analyzer.analyze(
            data=AnalyzerInputData(
                input_data=(
                    ServiceData(
                        service_name=TEST_SERVICE_ONE_NAME,
                        data=[
                            TEST_RECORD_2_WEAK
                        ]
                    ),
                    ServiceData(
                        service_name=TEST_SERVICE_TWO_NAME,
                        data=[
                            TEST_RECORD_2_WEAK,
                        ]
                    )
                )
            ))
        expected_result = AnalyzeResult(
            analyze_result=[
                CheckResult(
                    analyze_method=AnalyzerMethods.REPEATS_CHECK,
                    service_name=TEST_SERVICE_ONE_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.REPEATS_CHECK,
                    service_name=TEST_SERVICE_TWO_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.WEAK_PASSWORD_CHECK,
                    service_name=TEST_SERVICE_ONE_NAME,
                    data=[TEST_RECORD_2_WEAK]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.WEAK_PASSWORD_CHECK,
                    service_name=TEST_SERVICE_TWO_NAME,
                    data=[TEST_RECORD_2_WEAK]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.NOT_PAIR_CHECK,
                    service_name=TEST_SERVICE_ONE_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.NOT_PAIR_CHECK,
                    service_name=TEST_SERVICE_TWO_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.PAIR_WITH_ANOTHER_PASSWORD_CHECK,
                    service_name=TEST_SERVICE_ONE_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.PAIR_WITH_ANOTHER_PASSWORD_CHECK,
                    service_name=TEST_SERVICE_TWO_NAME,
                    data=[]
                )
            ]
        )
        self.assertEqual(result, expected_result)

    def test_good_case_with_not_pair(self):
        result = self.analyzer.analyze(
            data=AnalyzerInputData(
                input_data=(
                    ServiceData(
                        service_name=TEST_SERVICE_ONE_NAME,
                        data=[
                            TEST_RECORD_1_STRONG
                        ]
                    ),
                    ServiceData(
                        service_name=TEST_SERVICE_TWO_NAME,
                        data=[
                            TEST_RECORD_3_STRONG,
                        ]
                    )
                )
            ))
        expected_result = AnalyzeResult(
            analyze_result=[
                CheckResult(
                    analyze_method=AnalyzerMethods.REPEATS_CHECK,
                    service_name=TEST_SERVICE_ONE_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.REPEATS_CHECK,
                    service_name=TEST_SERVICE_TWO_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.WEAK_PASSWORD_CHECK,
                    service_name=TEST_SERVICE_ONE_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.WEAK_PASSWORD_CHECK,
                    service_name=TEST_SERVICE_TWO_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.NOT_PAIR_CHECK,
                    service_name=TEST_SERVICE_ONE_NAME,
                    data=[TEST_RECORD_1_STRONG]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.NOT_PAIR_CHECK,
                    service_name=TEST_SERVICE_TWO_NAME,
                    data=[TEST_RECORD_3_STRONG]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.PAIR_WITH_ANOTHER_PASSWORD_CHECK,
                    service_name=TEST_SERVICE_ONE_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.PAIR_WITH_ANOTHER_PASSWORD_CHECK,
                    service_name=TEST_SERVICE_TWO_NAME,
                    data=[]
                )
            ]
        )
        self.assertEqual(result, expected_result)

    def test_good_case_with_pair_with_another_password(self):
        result = self.analyzer.analyze(
            data=AnalyzerInputData(
                input_data=(
                    ServiceData(
                        service_name=TEST_SERVICE_ONE_NAME,
                        data=[
                            TEST_RECORD_1_STRONG
                        ]
                    ),
                    ServiceData(
                        service_name=TEST_SERVICE_TWO_NAME,
                        data=[
                            TEST_RECORD_1_STRONG_ANOTHER_PASS,
                        ]
                    )
                )
            ))
        expected_result = AnalyzeResult(
            analyze_result=[
                CheckResult(
                    analyze_method=AnalyzerMethods.REPEATS_CHECK,
                    service_name=TEST_SERVICE_ONE_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.REPEATS_CHECK,
                    service_name=TEST_SERVICE_TWO_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.WEAK_PASSWORD_CHECK,
                    service_name=TEST_SERVICE_ONE_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.WEAK_PASSWORD_CHECK,
                    service_name=TEST_SERVICE_TWO_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.NOT_PAIR_CHECK,
                    service_name=TEST_SERVICE_ONE_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.NOT_PAIR_CHECK,
                    service_name=TEST_SERVICE_TWO_NAME,
                    data=[]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.PAIR_WITH_ANOTHER_PASSWORD_CHECK,
                    service_name=TEST_SERVICE_ONE_NAME,
                    data=[TEST_RECORD_1_STRONG]
                ),
                CheckResult(
                    analyze_method=AnalyzerMethods.PAIR_WITH_ANOTHER_PASSWORD_CHECK,
                    service_name=TEST_SERVICE_TWO_NAME,
                    data=[TEST_RECORD_1_STRONG_ANOTHER_PASS]
                ),
            ]
        )
        self.assertEqual(result, expected_result)