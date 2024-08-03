from src.services.yandex_password_parser.handlers import CsvPasswordHandler
from src.services.yandex_password_parser.yandex_password_parser_exceptions import NotOneFileInPasswordArchive

from src.services.data_manager import InputDirManager, TempDataManager
from src.services.deps.csv_parser import CsvParser
from src.services.deps.zip_unpacker import ZipUnpacker


class YandexPasswordParser:
    """
    Парсер паролей Yandex.
    """

    def __init__(self, input_dir_path: str, temp_dir_path: str, archive_password: str):
        self.__input_manager = InputDirManager(input_path=input_dir_path)
        self.__unpacker = ZipUnpacker(password=archive_password)
        self.__csv_parser = CsvParser()
        self.__temp_dir_path = temp_dir_path
        self.__temp_data_manager = TempDataManager(temp_data_path=temp_dir_path)

    def __unzip_yandex_password_archive(self, zip_archive_name: str) -> str:
        path_of_archive = self.__input_manager.find_file_in_input(
            filename=zip_archive_name
        )
        paths = self.__unpacker.unzip_archive_with_password(zip_filepath=path_of_archive,
                                                            dest_path=self.__temp_dir_path)
        if len(paths) == 1:
            return paths[0]
        else:
            raise NotOneFileInPasswordArchive("В архиве лежит не один csv-файл.")

    def get_passwords_data(self, zip_archive_name: str):
        path = self.__unzip_yandex_password_archive(zip_archive_name=zip_archive_name)
        passwords_data = self.__csv_parser.parse_csv(path=path, row_handler=CsvPasswordHandler.parse_row)
        self.__temp_data_manager.clean_temp_data_dir()
        return passwords_data
