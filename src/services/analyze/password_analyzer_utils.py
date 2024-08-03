from src.services.analyze.analyze_types import NotPairResult, PairResult


class PasswordAnalyzerUtils(object):

    @staticmethod
    def find_repeats(data: list[tuple[str, str, str]]) -> list[tuple[str, str, str]]:
        memory = []
        repeats = []
        for domain, login, password in data:
            unique_domain_tuple = (domain, login)
            domain_tuple = (domain, login, password)
            if unique_domain_tuple not in memory:
                memory.append(unique_domain_tuple)
            else:
                if unique_domain_tuple not in repeats:
                    repeats.append(domain_tuple)
        return repeats

    def find_not_pairs(self,
                      google_passwords: list[tuple[str, str, str]],
                      yandex_passwords: list[tuple[str, str, str]]) -> NotPairResult:
        yandex_passwords_without_repeat: list[tuple[str, str, str]] = self._clean_repeats(data=yandex_passwords)
        google_passwords_without_repeat: list[tuple[str, str, str]] = self._clean_repeats(data=google_passwords)

        yandex_passwords_without_repeat_without_password: list[tuple[str, str]] = [
            (record[0], record[1]) for record in self._clean_repeats(data=yandex_passwords)
        ]
        google_passwords_without_repeat_without_password: list[tuple[str, str]] = [
            (record[0], record[1]) for record in self._clean_repeats(data=google_passwords)
        ]

        yandex_set = set(tuple(sorted(t)) for t in yandex_passwords_without_repeat_without_password)
        google_set = set(tuple(sorted(t)) for t in google_passwords_without_repeat_without_password)

        yandex_unique_list = [t for t in yandex_passwords_without_repeat if tuple(sorted((t[0], t[1]))) not in google_set]
        google_unique_list = [t for t in google_passwords_without_repeat if tuple(sorted((t[0], t[1]))) not in yandex_set]
        return NotPairResult(
            google=google_unique_list,
            yandex=yandex_unique_list,
        )

    def find_pairs(self, google_passwords: list[tuple[str, str, str]],
                   yandex_passwords: list[tuple[str, str, str]]) -> PairResult:

        yandex_passwords_without_repeat: list[tuple[str, str, str]] = self._clean_repeats(data=yandex_passwords)
        google_passwords_without_repeat: list[tuple[str, str, str]] = self._clean_repeats(data=google_passwords)

        yandex_passwords_without_repeat_without_password: list[tuple[str, str]] = [
            (record[0], record[1]) for record in self._clean_repeats(data=yandex_passwords)
        ]
        google_passwords_without_repeat_without_password: list[tuple[str, str]] = [
            (record[0], record[1]) for record in self._clean_repeats(data=google_passwords)
        ]

        yandex_set = set(tuple(sorted(t)) for t in yandex_passwords_without_repeat_without_password)
        google_set = set(tuple(sorted(t)) for t in google_passwords_without_repeat_without_password)

        yandex_pair_list = [t for t in yandex_passwords_without_repeat if tuple(sorted((t[0], t[1]))) in google_set]
        google_pair_list = [t for t in google_passwords_without_repeat if tuple(sorted((t[0], t[1]))) in yandex_set]
        return PairResult(
            google=google_pair_list,
            yandex=yandex_pair_list,
        )

    @staticmethod
    def _clean_repeats(data: list[tuple[str, str, str]]) -> list[tuple[str, str, str]]:
        memory = []
        unique_records = []
        for domain, login, password in data:
            compare_tuple = (domain, login)
            domain_tuple = (domain, login, password)
            if compare_tuple not in memory:
                memory.append(compare_tuple)
                unique_records.append(domain_tuple)
        return unique_records