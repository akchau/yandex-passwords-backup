import os

import pyzipper


class ZipUnpacker:
    """
    Класс работы с zip-архивом.
    """

    def __init__(self, password: str):
        self.__password = password

    def unzip_archive_with_password(self, zip_filepath: str, dest_path: str) -> list[str]:
        """
        Распаковка zip архива с паролем.
        :param zip_filepath: Путь zip-файла.
        :param dest_path: Путь для распаковки.
        :return: None
        """
        with pyzipper.AESZipFile(zip_filepath) as zf:
            filenames = zf.namelist()
            zf.extractall(dest_path, pwd=bytes(self.__password, 'utf-8'))
        return [os.path.join(dest_path, filename) for filename in filenames]
