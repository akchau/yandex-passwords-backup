from src.services.analyze.analyze_types import ListPasswordRecords


class RepeatFilterUtil:
    """
    Фильтр повторов.
    """

    @staticmethod
    def get_repeats(data: ListPasswordRecords) -> ListPasswordRecords:
        """
        Получение списка повторов.
        """
        seen = set()
        duplicates = set()
        for record in data:
            pair = tuple(record[:2])
            if pair in seen:
                duplicates.add(record)
            else:
                seen.add(pair)
        return list(duplicates)

    @staticmethod
    def get_unique_records(data: ListPasswordRecords) -> ListPasswordRecords:
        """
        Отрезание повторов и генерация списка уникальных записей.
        """
        seen = set()
        unique_records = set()
        for record in data:
            pair = tuple(record[:2])
            if pair not in seen:
                unique_records.add(record)
                seen.add(pair)
        return list(unique_records)


class NotPairFilter:
    """
    Фильтр пар.
    """

    @staticmethod
    def __get_set_cut_passwords(passwords_list: ListPasswordRecords) -> set:
        """
        Получение сета кортежей состоящего только из url-login.
        """
        return set(tuple(sorted(t)) for t in [(record[0], record[1]) for record in passwords_list])

    def __compare_to_pair(self, passwords_list: ListPasswordRecords,
                          compare_passwords_list: ListPasswordRecords) -> ListPasswordRecords:
        """
        Получение записей у которых есть пара по url-логин в другом источнике.
        """
        return [t for t in passwords_list if
                tuple(sorted((t[0], t[1]))) not in self.__get_set_cut_passwords(compare_passwords_list)]

    def __compare_to_not_pair(self, passwords_list: ListPasswordRecords,
                              compare_passwords_list: ListPasswordRecords) -> ListPasswordRecords:
        """
        Получение записей у которых нет пары по url-логин в другом источнике.
        """
        return [t for t in passwords_list if
                tuple(sorted((t[0], t[1]))) not in self.__get_set_cut_passwords(compare_passwords_list)]

    def find_not_pair_records(self, backup_passwords: ListPasswordRecords,
                              cloud_passwords: ListPasswordRecords
                              ) -> tuple[ListPasswordRecords, ListPasswordRecords]:
        """
        Найти записи с уникальной парой url в двух источниках.
        """
        return (self.__compare_to_not_pair(passwords_list=backup_passwords, compare_passwords_list=cloud_passwords),
                self.__compare_to_not_pair(passwords_list=cloud_passwords, compare_passwords_list=backup_passwords))

    def find_pair_records(self, backup_passwords: ListPasswordRecords,
                          cloud_passwords: ListPasswordRecords) -> tuple[ListPasswordRecords, ListPasswordRecords]:
        """
        Найти записи с условием пара url-логин совпадает в двух источниках.
        """
        return (
            self.__compare_to_pair(passwords_list=backup_passwords, compare_passwords_list=cloud_passwords),
            self.__compare_to_pair(passwords_list=cloud_passwords, compare_passwords_list=backup_passwords)
        )


class AnotherPasswordInPairFilter:
    """
    Фильтр пар у которых отличается пароль.
    """

    @staticmethod
    def __get_set_with_password(passwords_list: ListPasswordRecords) -> set:
        """
        Получение сета с кортежами состоящих из записей.
        """
        return set(tuple(sorted(t)) for t in passwords_list)

    def __compare_pairs(self, passwords_list: ListPasswordRecords,
                        compare_passwords_list: ListPasswordRecords) -> ListPasswordRecords:
        """
        Получение пар у которых отличается пароль.
        """
        return [
            t for t in passwords_list
            if tuple(sorted(t)) not in self.__get_set_with_password(compare_passwords_list)
        ]

    def find_another_password_in_pair(self, backup_passwords: ListPasswordRecords,
                                      cloud_passwords: ListPasswordRecords
                                      ) -> tuple[ListPasswordRecords, ListPasswordRecords]:
        """
        Получить пары, у которых не совпадают пароли.
        """
        google_pairs_with_not_equal_password: ListPasswordRecords = self.__compare_pairs(
            passwords_list=cloud_passwords,
            compare_passwords_list=backup_passwords)
        yandex_pairs_with_not_equal_password: ListPasswordRecords = self.__compare_pairs(
            passwords_list=cloud_passwords,
            compare_passwords_list=backup_passwords
        )
        return google_pairs_with_not_equal_password, yandex_pairs_with_not_equal_password
