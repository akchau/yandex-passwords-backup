import uuid
from datetime import datetime

from src.domain.domain_types import SourceType


class Report:

    LINE_STRING = "-" * 100

    def __init__(self):
        self.__detail = ""
        self.__id = str(uuid.uuid4())
        self.__add_header()

    def __add_header(self):
        self.__add_line()
        self.__detail = f"{self.__detail}\nОтчет №{self.__id} от {datetime.now()}"
        self.__add_line()

    def __add_string(self, string) -> None:
        self.__detail = f"{self.__detail}\n{string}"

    def __add_line(self):
        self.__add_string(self.LINE_STRING)

    def __add_record(self, data, title, message):
        self.__add_line()
        self.__add_string(title)
        for host, login, _ in data:
            self.__add_string(string=message.format(host=host, login=login))
        self.__add_line()

    def __add_not_pair_records(self, data, service: str):
        self.__add_record(
            title=f"ПРОВЕРКА ПАР ПАРОЛЕЙ {len(data)} НЕ НАШАЛА ПАРЫ НА СЕРВИСЕ {service} :\n",
            message="{host} {login}",
            data=data
        )

    def __add_pair_records(self, data, service: str):
        self.__add_record(
            title=f"ПРОВЕРКА ПАР ПАРОЛЕЙ {len(data)} НАШАЛА ПАРЫ НА СЕРВИСЕ У КОТОРЫХ ОТЛИЧАЮТСЯ ПАРОЛИ {service} :\n",
            message="{host} {login}",
            data=data
        )

    def __add_repeat(self, data, service: str):
        self.__add_record(
            title=f"ПРОВЕРКА ПОВТОРОВ ВЫЯВИЛА {len(data)} ПОВТОРЫ на сервисе: {service}\n",
            message="{host} {login}",
            data=data
        )

    def fill(self, data):
        if data.google_repeats:
            self.__add_repeat(data=data.google_repeats, service=SourceType.GOOGLE)
        if data.yandex_repeats:
            self.__add_repeat(data.yandex_repeats, service=SourceType.YANDEX)
        if data.yandex_not_pair:
            self.__add_not_pair_records(data=data.yandex_not_pair, service=SourceType.YANDEX)
        if data.google_not_pair:
            self.__add_not_pair_records(data=data.yandex_not_pair, service=SourceType.GOOGLE)
        if data.pair_result_yandex:
            self.__add_pair_records(data=data.pair_result_yandex, service=SourceType.YANDEX)
        if data.pair_result_google:
            self.__add_pair_records(data=data.pair_result_google, service=SourceType.GOOGLE)
        self.__add_string(string=f"НАЙДЕНО {data.good_pairs_num} ПАР.")

    def __repr__(self):
        return self.__detail
