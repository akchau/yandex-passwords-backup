from src.services.analyze.analyze_types import AnalyzerInputData, CheckResult, ServiceData
from src.services.analyze.base import BaseHandler
from src.services.analyze.utils import RepeatFilterUtil, NotPairFilter, AnotherPasswordInPairFilter, WeakPasswordFilter


def clean_repeats(data: AnalyzerInputData) -> AnalyzerInputData:
    """
    Очистить повторы.
    """
    return AnalyzerInputData(
        input_data_cloud=(
            data.input_data_backup[0], RepeatFilterUtil.get_unique_records(data.input_data_backup[1])
        ),
        input_data_backup=(
            data.input_data_cloud[0], RepeatFilterUtil.get_unique_records(data.input_data_cloud[1]))
    )


class RepeatsHandler(BaseHandler):
    """
    Обработчик повторов.
    """
    def handle(self, data: AnalyzerInputData) -> CheckResult:
        """
        Поиск повторяющихся записей по паре домен-логин в каждом списке записей.
        """
        return CheckResult(
            results=[
                ServiceData(
                    service_name=data.input_data_backup.service_name,
                    data=RepeatFilterUtil.get_repeats(data=data.input_data_backup.data)
                ),
                ServiceData(
                    service_name=data.input_data_cloud.service_name,
                    data=RepeatFilterUtil.get_repeats(data=data.input_data_cloud.data)
                )
            ]
        )


class WeakPasswordsHandler(BaseHandler):
    """
    Обработчик повторов.
    """

    def handle(self, data: AnalyzerInputData) -> CheckResult:
        """
        Поиск повторяющихся записей по паре домен-логин в каждом списке записей.
        """
        return CheckResult(
            results=[
                ServiceData(
                    service_name=data.input_data_backup.service_name,
                    data=WeakPasswordFilter().check_passwords(data=data.input_data_backup.data)),
                ServiceData(
                    service_name=data.input_data_cloud.service_name,
                    data=WeakPasswordFilter().check_passwords(data=data.input_data_cloud.data))
            ]
        )


class NotPairsHandler(BaseHandler):
    """
    Обработчик несовпадающих пар.
    """

    def prepare_data(self, data: AnalyzerInputData) -> AnalyzerInputData:
        """
        Подготовка данных:

        - Из каждого списка уберем повторяющиеся элементы.
        """
        return clean_repeats(data)

    def handle(self, data: AnalyzerInputData) -> CheckResult:
        """
        Поиск не парных записей по паре домен-логин.
        """
        google_unique_list, yandex_unique_list = NotPairFilter().find_not_pair_records(
            backup_passwords=data.input_data_backup.data,
            cloud_passwords=data.input_data_cloud.data
        )
        return CheckResult(
            results=[
                ServiceData(
                    service_name=data.input_data_backup.service_name,
                    data=google_unique_list
                ),
                ServiceData(
                    service_name=data.input_data_cloud.service_name,
                    data=yandex_unique_list
                )
            ]
        )


class PairsWithNotEqualHandler(BaseHandler):
    """
    Обработчик пар с разными паролями.
    """

    def prepare_data(self, data: AnalyzerInputData) -> AnalyzerInputData:
        """
        Подготовка данных:

        - Из каждого списка уберем повторяющиеся элементы.
        """
        clean_data: AnalyzerInputData = clean_repeats(data)
        backup_data, cloud_data = NotPairFilter().find_pair_records(
            backup_passwords=clean_data.input_data_backup[1],
            cloud_passwords=clean_data.input_data_cloud[1]
        )
        return AnalyzerInputData(
            input_data_backup=(clean_data.input_data_backup[0], backup_data),
            input_data_cloud=(clean_data.input_data_cloud[0], cloud_data)
        )

    def handle(self, data: AnalyzerInputData) -> CheckResult:
        """
        Поиск пар, у которых отличается пароль.
        """
        google_unique_list, yandex_unique_list = AnotherPasswordInPairFilter().find_another_password_in_pair(
            backup_passwords=data.input_data_backup[1],
            cloud_passwords=data.input_data_cloud[1]
        )
        return CheckResult(
            results=[
                (data.input_data_backup[0], google_unique_list),
                (data.input_data_cloud[0], yandex_unique_list)
            ]
        )
