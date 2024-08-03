from src.settings import settings
from src.services.yandex_password_parser import YandexPasswordParser

if __name__ == '__main__':
    parser = YandexPasswordParser(input_dir_path=settings.INPUT_PATH,
                                  temp_dir_path=settings.TEMP_DATA_PATH,
                                  archive_password=settings.ARCHIVE_PASSWORD)
    data = parser.get_passwords_data(zip_archive_name="yandex_browser_passwords_2024-07-18.zip")
    print(data)
