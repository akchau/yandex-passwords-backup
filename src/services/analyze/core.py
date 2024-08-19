from src.services.analyze.analyze_types import AnalyzeResult, AnalyzerMethods, AnalyzerInputData
from src.services.analyze.base import BaseHandler
from src.services.analyze.handlers import RepeatsHandler, NotPairsHandler, PairsWithNotEqualHandler


class PasswordAnalyzer:
    """
    Анализатор паролей. Прогоняет данные через хендлеры. И возвращает результат всех проверок.
    """

    def __init__(self):
        self.handlers: list[BaseHandler] = [
            RepeatsHandler(method=AnalyzerMethods.REPEATS_CHECK),
            NotPairsHandler(method=AnalyzerMethods.NOT_PAIR_CHECK),
            PairsWithNotEqualHandler(method=AnalyzerMethods.PAIR_WITH_ANOTHER_PASSWORD_CHECK)
        ]

    def analyze(self, data: AnalyzerInputData) -> AnalyzeResult:
        result = {}
        for handler in self.handlers:
            result[handler.method] = handler.start_handle(data)
        return AnalyzeResult(**result)
