from src.services.analyze.analyze_types import NotPairResult, PairResult, RepeatsResult


class PasswordAnalyzerUtils(object):

    @staticmethod
    def find_repeats(data: list[tuple[str, str, str]]) -> RepeatsResult:
        """
        Поиск повторяющихся записей по паре домен-логин.
        :param data: Данные паролей.
        :return: Повторы.
        """
        memory = []
        repeats = []
        not_repeats = []
        for domain, login, password in data:
            unique_domain_tuple = (domain, login)
            domain_tuple = (domain, login, password)
            if unique_domain_tuple not in memory:
                memory.append(unique_domain_tuple)
                not_repeats.append(domain_tuple)
            else:
                if domain_tuple not in repeats:
                    repeats.append(domain_tuple)
        return RepeatsResult(
            repeats=repeats,
            not_repeats=not_repeats
        )

    def find_not_pairs(self,
                       google_passwords: list[tuple[str, str, str]],
                       yandex_passwords: list[tuple[str, str, str]]) -> NotPairResult:
        yandex_passwords_without_repeat: list[tuple[str, str, str]] = self.find_repeats(data=yandex_passwords).not_repeats
        google_passwords_without_repeat: list[tuple[str, str, str]] = self.find_repeats(data=google_passwords).not_repeats

        yandex_passwords_without_repeat_without_password: list[tuple[str, str]] = [
            (record[0], record[1]) for record in yandex_passwords_without_repeat
        ]
        google_passwords_without_repeat_without_password: list[tuple[str, str]] = [
            (record[0], record[1]) for record in google_passwords_without_repeat
        ]

        yandex_set = set(tuple(sorted(t)) for t in yandex_passwords_without_repeat_without_password)
        google_set = set(tuple(sorted(t)) for t in google_passwords_without_repeat_without_password)

        yandex_unique_list = [t for t in yandex_passwords_without_repeat if tuple(sorted((t[0], t[1]))) not in google_set]
        google_unique_list = [t for t in google_passwords_without_repeat if tuple(sorted((t[0], t[1]))) not in yandex_set]
        return NotPairResult(
            google=google_unique_list,
            yandex=yandex_unique_list,
        )

    def find_pairs_with_another_password(self, google_passwords: list[tuple[str, str, str]],
                                         yandex_passwords: list[tuple[str, str, str]]) -> PairResult:

        yandex_passwords_without_repeat: list[tuple[str, str, str]] = self.find_repeats(data=yandex_passwords).not_repeats
        google_passwords_without_repeat: list[tuple[str, str, str]] = self.find_repeats(data=google_passwords).not_repeats

        yandex_passwords_without_repeat_without_password: list[tuple[str, str]] = [
            (record[0], record[1]) for record in yandex_passwords_without_repeat
        ]
        google_passwords_without_repeat_without_password: list[tuple[str, str]] = [
            (record[0], record[1]) for record in google_passwords_without_repeat
        ]

        yandex_set = set(tuple(sorted(t)) for t in yandex_passwords_without_repeat_without_password)
        google_set = set(tuple(sorted(t)) for t in google_passwords_without_repeat_without_password)

        yandex_set_with_password = set(tuple(sorted(t)) for t in yandex_passwords_without_repeat)
        google_set_with_password = set(tuple(sorted(t)) for t in google_passwords_without_repeat)

        return PairResult(
            google=[t for t in google_passwords_without_repeat
                    if tuple(sorted((t[0], t[1]))) in yandex_set and
                    tuple(sorted(t)) not in yandex_set_with_password],
            yandex=[t for t in yandex_passwords_without_repeat
                    if tuple(sorted((t[0], t[1]))) in google_set and
                    tuple(sorted(t)) not in google_set_with_password]
        )
