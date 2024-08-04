from src.services.analyze.analyze_types import NotPairResult, AnalyzeResult, PairResult
from src.services.analyze.password_analyzer_utils import PasswordAnalyzerUtils


class PasswordAnalyzer:

    def __init__(self, password_analyzer_utils: PasswordAnalyzerUtils = PasswordAnalyzerUtils()):
        self.__password_analyzer_utils = password_analyzer_utils

    def analyze(self, yandex_passwords, google_passwords) -> AnalyzeResult:
        google_repeat_result: list[tuple[str, str, str]] = self.__password_analyzer_utils.find_repeats(
            data=google_passwords
        ).repeats
        yandex_repeat_result: list[tuple[str, str, str]] = self.__password_analyzer_utils.find_repeats(
            data=yandex_passwords
        ).repeats
        not_pair_record_result: NotPairResult = self.__password_analyzer_utils.find_not_pairs(
            google_passwords=google_passwords,
            yandex_passwords=yandex_passwords
        )
        pair_result: PairResult = self.__password_analyzer_utils.find_pairs_with_another_password(
            google_passwords=google_passwords,
            yandex_passwords=yandex_passwords
        )
        return AnalyzeResult(
            google_repeats=google_repeat_result,
            yandex_repeats=yandex_repeat_result,
            yandex_not_pair=not_pair_record_result.yandex,
            google_not_pair=not_pair_record_result.google,
            pair_result_google=pair_result.google,
            pair_result_yandex=pair_result.yandex,
        )
