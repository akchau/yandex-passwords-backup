from zxcvbn import zxcvbn

from src.services.analyze.analyze_exceptions import AnalyzeException
from src.services.analyze.analyze_types import ListPasswordRecords


class CompareListRecordAlgorythm:
    """
    Алгоритм сравнения элементов.
    """

    def _get_set(self, passwords_list: ListPasswordRecords, depth: int) -> set:
        """
        Получение сета кортежей c определенной глубиной.
        """
        return set(tuple(t) for t in [self._tuple_in_depth(record, depth) for record in passwords_list])

    @staticmethod
    def _tuple_in_depth(data: tuple[str, str, str], depth: int):
        if 0 < depth <= len(data):
            return tuple(
                tuple(
                    [data[index] for index in range(depth)]
                )
            )
        raise AnalyzeException("Глубина превышает длину списка или отрицательное число.")

    def _item_in_second(self, item: tuple[str, str, str], list_of_records: ListPasswordRecords, depth: int):
        """
        Проверяем есть-ли
        """
        return self._tuple_in_depth(item, depth) in self._get_set(list_of_records, depth)

    def find_first_in_second(self, first: ListPasswordRecords, second: ListPasswordRecords,
                             depth: int, include=True) -> ListPasswordRecords:
        if include:
            return [t for t in first if self._item_in_second(t, second, depth)]
        else:
            return [t for t in first if not self._item_in_second(t, second, depth)]


class WeakPasswordSearchAlgorythm:

    def find_weak_passwords(self, data: ListPasswordRecords) -> ListPasswordRecords:
        weak_passwords = []
        for password_record in data:
            if self._check_password_to_weak(password_record[2]):
                weak_passwords.append(password_record)
        return weak_passwords

    @staticmethod
    def _check_password_to_weak(password: str) -> bool:
        """
        Проверка пароля на слабость.
        """
        results = zxcvbn(password)
        score = results.get('score')
        if isinstance(score, int) and score < 3:
            return True
        return False


class RepeatsAlgorythm:

    @staticmethod
    def find_repeats(data: ListPasswordRecords, unique=False) -> ListPasswordRecords:
        """
        Получение списка повторов.
        """
        seen = set()
        duplicates = set()
        unique_records = set()
        for record in data:
            pair = tuple(record[:2])
            if pair in seen:
                duplicates.add(record)
            else:
                seen.add(pair)
                unique_records.add(record)
        return list(unique_records) if unique else list(duplicates)
