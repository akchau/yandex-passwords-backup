
from src.services.analyze.analyze_types import AnalyzeResult
from src.services.analyze import PasswordAnalyzer
from src.services.report import Report


class PasswordDomain:

    def __init__(self, yandex_parser, google_sheets_parser):
        self.__yandex_parser = yandex_parser
        self.__google_sheets_parser = google_sheets_parser
        self.__analyzer = PasswordAnalyzer()

    def password_synchronization(self, yandex_zip_archive_name: str) -> str:
        """
        Анализ паролей из двух смс
        :param yandex_zip_archive_name: Путь по которому лежт zip-бекап пароля.
        :return:
        """

        yandex_passwords: list[tuple[str, str, str]] = self.__yandex_parser.get_passwords_data(
            zip_archive_name=yandex_zip_archive_name
        )
        google_sheets_passwords: list[tuple[str, str, str]] = self.__google_sheets_parser.get_passwords_data()
        result: AnalyzeResult = self.__analyzer.analyze(yandex_passwords=yandex_passwords,
                                                        google_passwords=google_sheets_passwords)
        report = Report()
        report.fill(data=result)

        return report.__repr__()
