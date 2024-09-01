from src.services.analyze import analyze_types
from src.services.analyze import base
from src.services.analyze import handlers as handlers
from src.services.analyze.analyze_types import Records

Handler = tuple[analyze_types.AnalyzerMethods, base.BaseFilterOne | base.BaseFilterPair, analyze_types.HandlingType]


handlers: list[Handler] = [
    (analyze_types.AnalyzerMethods.REPEATS_CHECK, handlers.RepeatFilter(),
     analyze_types.HandlingType.ONE_TO_ONE_HANDLING),
    (analyze_types.AnalyzerMethods.WEAK_PASSWORD_CHECK, handlers.WeakPasswordFilter(),
     analyze_types.HandlingType.ONE_TO_ONE_HANDLING),
    (analyze_types.AnalyzerMethods.NOT_PAIR_CHECK, handlers.NotPairFilter(),
     analyze_types.HandlingType.PAIR_HANDLING),
    (analyze_types.AnalyzerMethods.PAIR_WITH_ANOTHER_PASSWORD_CHECK,
     handlers.AnotherPasswordInPairFilter(),
     analyze_types.HandlingType.PAIR_HANDLING)
]


class PasswordAnalyzer:
    """
    Анализатор паролей. Прогоняет данные через хендлеры и возвращает результат всех проверок.
    """

    def __init__(self, _handlers=None):
        if _handlers is None:
            _handlers = handlers
        self.handlers = _handlers

    @staticmethod
    def __handle_one_to_one(data: analyze_types.AnalyzerInputData, method: analyze_types.AnalyzerMethods,
                            handler: base.BaseFilterOne) -> analyze_types.OutputType:
        """
        Обработка данных по одному.
        """
        return [
            analyze_types.CheckResult(
                service_name=data.input_data[index].service_name,
                analyze_method=method,
                data=handler.filter(data.input_data[index].data)
            )
            for index in range(2)
        ]

    @staticmethod
    def __handle_pair(data: analyze_types.AnalyzerInputData, method: analyze_types.AnalyzerMethods,
                      prepare_data_callback, handle_callback) -> analyze_types.OutputType:
        """
        Обработка данных в паре.
        """
        clean_data = prepare_data_callback(data)
        result = handle_callback(*clean_data), handle_callback(*reversed(clean_data))
        return [
            analyze_types.CheckResult(
                service_name=data.input_data[index].service_name,
                analyze_method=method,
                data=result[index]
            )
            for index in range(2)
        ]

    def analyze(self, data: analyze_types.AnalyzerInputData) -> analyze_types.AnalyzeResult:
        """
        Анализ паролей через хендлеры.
        """
        results = []
        for method, handler, handling_type in self.handlers:
            if handling_type == analyze_types.HandlingType.ONE_TO_ONE_HANDLING:
                results.extend(self.__handle_one_to_one(method=method, data=data, handler=handler))
            if handling_type == analyze_types.HandlingType.PAIR_HANDLING:
                results.extend(self.__handle_pair(method=method, data=data))
        return analyze_types.AnalyzeResult(analyze_result=results)
