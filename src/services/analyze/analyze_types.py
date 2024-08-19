from enum import Enum

from pydantic import BaseModel

PasswordRecord = tuple[str, str, str]

ListPasswordRecords = list[PasswordRecord]


class AnalyzerMethods(str, Enum):
    """
    Методы анализа.
    """
    REPEATS_CHECK = "repeats_check"
    NOT_PAIR_CHECK = "not_pair_check"
    PAIR_WITH_ANOTHER_PASSWORD_CHECK = "pair_with_another_password_check"


class ServiceData(BaseModel):
    service_name: str
    data: ListPasswordRecords


class AnalyzerInputData(BaseModel):
    """
    Входные данные для анализа.
    """
    input_data_cloud: ServiceData
    input_data_backup: ServiceData


class CheckResult(BaseModel):
    """
    Результат проверки двух источников на повторяющиеся записи.

    - results: CheckResult - результат проверки.
    """
    results: list[ServiceData]


class AnalyzeResult(BaseModel):
    """
    Результат анализа.

    - repeats_check_result: CheckResult - результат проверки повторяющихся записей.
    - not_pairs_login_check_result: CheckResult - результат проверки не парных записей.
    - pair_with_another_password_check_result: CheckResult - результат проверки парных записей.
    - good_pairs_num: int
    """
    repeats_check: CheckResult
    not_pair_check: CheckResult
    pair_with_another_password_check: CheckResult
    weak_password_check: CheckResult
