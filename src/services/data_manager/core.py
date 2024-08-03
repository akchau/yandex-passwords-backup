import os


class InputDirManager:
    """
    Класс работы с директорией входных данных.
    """

    def __init__(self, input_path: str):
        self.__input_path = input_path

    def find_file_in_input(self, filename: str) -> str | None:
        """
        Поиск имени
        :param filename: Имя файла который ищем.
        :return: str | None - Путь к файлу или None, если нет такого файла внутри.
        """
        for file in os.listdir(self.__input_path):
            if file.endswith(".zip") and file == filename:
                return os.path.join(self.__input_path, filename)


class TempDataManager:

    def __init__(self, temp_data_path: str):
        self.__temp_data_path = temp_data_path

    def clean_temp_data_dir(self):
        temp_files = os.listdir(self.__temp_data_path)
        for file in temp_files:
            os.remove(os.path.join(self.__temp_data_path, file))