from abc import ABC, abstractmethod

from src.services.analyze.analyze_types import Records, ListPasswordRecords


class BaseFilterOne(ABC):

    def __init__(self):
        pass
    """
    Базовый класс при сравнении списка записей
    """

    @abstractmethod
    def _filter(self, data: ListPasswordRecords) -> ListPasswordRecords:
        """
        Получить пары, у которых не совпадают пароли.
        """
        raise NotImplementedError

    @abstractmethod
    def _prepare_data(self, data: ListPasswordRecords) -> ListPasswordRecords:
        """
        Подготовка данных при фильтрации одного списка.
        """
        raise NotImplementedError

    def filter(self, data: ListPasswordRecords) -> ListPasswordRecords:
        """
        Фильтрация.
        """
        clean_data = self._prepare_data(data)
        return self._filter(clean_data)


class BaseFilterPair(ABC):
    """
    Базовый класс для фильтроции двух списков записей.
    """

    @abstractmethod
    def _compare(self, first: ListPasswordRecords, second: ListPasswordRecords) -> ListPasswordRecords:
        """
        Сравнение двух списков.
        """
        raise NotImplementedError

    def filter(self, data: Records) -> Records:
        """
        Фильтрация.
        """
        clean_data = self._prepare_data(data)
        return self._compare(*clean_data), self._compare(*reversed(clean_data))

    @abstractmethod
    def _prepare_data(self, data: Records) -> Records:
        """
        Подготовка данных при сравнение двух списков.
        """
        raise NotImplementedError
