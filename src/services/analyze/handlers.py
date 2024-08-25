from src.services.analyze import analyze_types, base, algorythms


class RepeatFilter(base.BaseFilterOne):
    """
    Фильтр повторов.
    """

    def _prepare_data(self, data: analyze_types.ListPasswordRecords) -> analyze_types.ListPasswordRecords:
        """
        Подготовка не нужна.
        """
        return data

    def _filter(self, data: analyze_types.ListPasswordRecords) -> analyze_types.ListPasswordRecords:
        """
        Получение списка повторов.
        """
        return algorythms.RepeatsAlgorythm().find_repeats(data)


class UniqueFilter(base.BaseFilterOne):
    """
    Фильтр уникальных записей.
    """

    def _prepare_data(self, data: analyze_types.ListPasswordRecords) -> analyze_types.ListPasswordRecords:
        """
        Подготовка не нужна.
        """
        return data

    def _filter(self, data: analyze_types.ListPasswordRecords) -> analyze_types.ListPasswordRecords:
        """
        Получение списка повторов.
        """
        return algorythms.RepeatsAlgorythm().find_repeats(data, unique=True)


class WeakPasswordFilter(base.BaseFilterOne):
    """
    Фильтр слабых паролей.
    """

    def _prepare_data(self, data: analyze_types.ListPasswordRecords) -> analyze_types.ListPasswordRecords:
        """
        Фильтруем только уникальные значения.
        """
        return algorythms.RepeatsAlgorythm().find_repeats(data, unique=True)

    def _filter(self, data: analyze_types.ListPasswordRecords) -> analyze_types.ListPasswordRecords:
        """
        Проверка паролей на слабость.
        """
        return algorythms.WeakPasswordSearchAlgorythm().find_weak_passwords(data)


class NotPairFilter(base.BaseFilterPair):
    """
    Фильтр непар.
    """

    def _compare(self, first: analyze_types.ListPasswordRecords,
                 second: analyze_types.ListPasswordRecords) -> analyze_types.ListPasswordRecords:
        """
        Получение записей у которых нет пары по url-логин в другом источнике.
        """
        return algorythms.CompareListRecordAlgorythm().find_first_in_second(first, second, depth=2, include=False)

    def _prepare_data(self, data: analyze_types.Records) -> analyze_types.Records:
        """
        Фильтруем только уникальные значения.
        """
        return UniqueFilter().filter(data[0]), UniqueFilter().filter(data[1])


class PairFilter(base.BaseFilterPair):
    """
    Фильтр пар.
    """
    def _compare(self, first: analyze_types.ListPasswordRecords,
                 second: analyze_types.ListPasswordRecords) -> analyze_types.ListPasswordRecords:
        """
        Получение записей у которых есть пара по url-логин в другом источнике.
        """
        return algorythms.CompareListRecordAlgorythm().find_first_in_second(first, second, depth=2)

    def _prepare_data(self, data: analyze_types.Records) -> analyze_types.Records:
        """
        Фильтруем только уникальные значения.
        """
        return UniqueFilter().filter(data[0]), UniqueFilter().filter(data[1])


class AnotherPasswordInPairFilter(base.BaseFilterPair):
    """
    Фильтр пар у которых отличается пароль.
    """

    def _compare(self, first: analyze_types.ListPasswordRecords,
                 second: analyze_types.ListPasswordRecords) -> analyze_types.ListPasswordRecords:
        """
        Получение пар у которых отличается пароль.
        """
        return algorythms.CompareListRecordAlgorythm().find_first_in_second(first, second, depth=3, include=False)

    def _prepare_data(self, data: analyze_types.Records) -> analyze_types.Records:
        """
        Фильтруем только пары.
        """
        return PairFilter().filter(data)
