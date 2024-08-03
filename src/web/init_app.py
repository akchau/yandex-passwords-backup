from dataclasses import dataclass
from typing import Type

from src.domain import PasswordDomain
from src.services.google_sheets_parser import GoogleSheetsParser
from src.services.yandex_password_parser import YandexPasswordParser
from src.settings import settings


@dataclass
class AppDataClassesType:
    yandex_parser_class: Type[YandexPasswordParser]
    google_parser_class: Type[GoogleSheetsParser]
    domain_class: Type[PasswordDomain]



@dataclass
class AppDataType:
    domain: PasswordDomain


AppDataClasses = AppDataClassesType(
    yandex_parser_class=YandexPasswordParser,
    domain_class=PasswordDomain,
    google_parser_class=GoogleSheetsParser
)


__yandex_parser = AppDataClasses.yandex_parser_class(
    archive_password=settings.ARCHIVE_PASSWORD,
    input_dir_path=settings.INPUT_PATH,
    temp_dir_path=settings.TEMP_DATA_PATH
)

__google_parser = AppDataClasses.google_parser_class()
__domain = AppDataClasses.domain_class(yandex_parser=__yandex_parser, google_sheets_parser=__google_parser)


def get_app_data() -> AppDataType:
    return AppDataType(domain=__domain)
