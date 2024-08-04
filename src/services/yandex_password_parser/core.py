from src.services.yandex_password_parser.handlers import CsvPasswordHandler
from src.services.yandex_password_parser.yandex_password_parser_exceptions import NotOneFileInPasswordArchive

from src.services.data_manager import InputDirManager, TempDataManager
from src.services.deps.csv_parser import CsvParser
from src.services.deps.zip_unpacker import ZipUnpacker


class YandexPasswordParser:
    """
    Парсер паролей Yandex.
    """

    def __init__(self, temp_dir_path: str, archive_password: str):
        self.__unpacker = ZipUnpacker(password=archive_password)
        self.__csv_parser = CsvParser()
        self.__temp_dir_path = temp_dir_path

    def __unzip_yandex_password_archive(self, path: str) -> str:
        paths = self.__unpacker.unzip_archive_with_password(zip_filepath=path,
                                                            dest_path=self.__temp_dir_path)
        if len(paths) == 1:
            return paths[0]
        else:
            raise NotOneFileInPasswordArchive("В архиве лежит не один csv-файл.")

    def get_passwords_data(self, path: str):
        path = self.__unzip_yandex_password_archive(path=path)
        passwords_data = self.__csv_parser.parse_csv(path=path, row_handler=CsvPasswordHandler.parse_row)
        return passwords_data
