from enum import Enum

from pydantic import BaseModel


class HandlingType(str, Enum):
    ONE_TO_ONE_HANDLING = "ONE_TO_ONE"
    PAIR_HANDLING = "PAIR_HANDLING"


class AnalyzerMethods(str, Enum):
    """
    Методы анализа.
    """
    REPEATS_CHECK = "repeats_check"
    NOT_PAIR_CHECK = "not_pair_check"
    PAIR_WITH_ANOTHER_PASSWORD_CHECK = "pair_with_another_password_check"
    WEAK_PASSWORD_CHECK = "weak_password_check"


ListPasswordRecords = list[tuple[str, str, str]]


class ServiceData(BaseModel):
    service_name: str
    data: ListPasswordRecords


Input_Type = tuple[ServiceData, ServiceData]

Records = tuple[ListPasswordRecords, ListPasswordRecords]


class AnalyzerInputData(BaseModel):
    """
    Входные данные для анализа.
    """
    input_data: Input_Type

    @property
    def records(self) -> Records:
        return self.input_data[0].data, self.input_data[1].data


class CheckResult(ServiceData):
    """
    Результат проверки данных одного сервиса.
    """
    analyze_method: AnalyzerMethods


OutputType = list[CheckResult]


class AnalyzeResult(BaseModel):
    """
    Результат анализа.

    """
    analyze_result: OutputType
