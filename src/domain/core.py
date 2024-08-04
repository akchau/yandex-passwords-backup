from src.services.analyze import PasswordAnalyzer, AnalyzeResult
from src.services.data_manager import InputDirManager, TempDataManager
from src.services.report import Report


class PasswordDomain:
    """
    Домен работы с паролями.

    - Синхронизирует пароли из двух источников.

    PasswordDomain(yandex_parser, google_sheets_parser)
    """

    def __init__(self, yandex_parser, google_sheets_parser, input_dir_path: str, temp_dir_path: str):
        self.__input_manager = InputDirManager(input_path=input_dir_path)
        self.__temp_data_manager = TempDataManager(temp_data_path=temp_dir_path)
        self.__yandex_parser = yandex_parser
        self.__google_sheets_parser = google_sheets_parser
        self.__analyzer = PasswordAnalyzer()

    def password_synchronization(self, yandex_zip_archive_name: str) -> str:
        """
        Анализ паролей из двух смс
        :param yandex_zip_archive_name: Имя архива zip-бекап пароля.
        :return: отчет с результатами анализа.
        """
        path_of_archive = self.__input_manager.find_file_in_input(filename=yandex_zip_archive_name)
        yandex_passwords: list[tuple[str, str, str]] = self.__yandex_parser.get_passwords_data(
            path=path_of_archive
        )
        google_sheets_passwords: list[tuple[str, str, str]] = self.__google_sheets_parser.get_passwords_data()

        result: AnalyzeResult = self.__analyzer.analyze(yandex_passwords=yandex_passwords,
                                                        google_passwords=google_sheets_passwords)

        self.__temp_data_manager.clean_temp_data_dir()

        report = Report()
        report.fill(data=result)

        return report.__repr__()
