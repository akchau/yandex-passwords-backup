from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from src.services.analyze.analyze_types import AnalyzerMethods, AnalyzerInputData, CheckResult

ReadyForAnalyzeData = TypeVar('ReadyForAnalyzeData')


class BaseHandler(ABC, Generic[ReadyForAnalyzeData]):

    def __init__(self, method: AnalyzerMethods):
        self.__method = method

    @property
    def method(self):
        return self.__method

    def start_handle(self, data: AnalyzerInputData):
        clean_data = self.prepare_data(data)
        return self.handle(clean_data)

    @staticmethod
    def prepare_data(data: AnalyzerInputData) -> ReadyForAnalyzeData:
        return data

    @abstractmethod
    def handle(self, data: ReadyForAnalyzeData) -> CheckResult:
        raise NotImplementedError
