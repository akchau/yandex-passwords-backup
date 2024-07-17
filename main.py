def runserver(*args, **kwargs) -> None:
    print("Сервер запущен")



REGISTERED_COMMANDS = {
    'runserver': runserver
}


def main(command_pool: dict[str, Callable]) -> None:
    """
    Главная функция приложения.
    :param command_pool: dict[str, Callable]
    :return:
    """
    args = sys.argv
    args_len = len(args)
    # Обработка случая, команда без аргументов.
    if args_len == 1:
        raise StartCommandError(f'Вы должны указать аргументы при обращении к файлу {__name__}. '
                                f'Возможные аргументы: {list(command_pool.keys())}')
    elif args_len >= 2:
        # Поиск целевой функции по команде
        command = args[1]
        target_func = command_pool.get(command, None)
        # Обработка неизвестной команды
        if target_func is None:
            raise StartCommandError(f'Данной команды не существует. '
                                    f'Возможные команды: {list(command_pool.keys())}')
        # Формируем список аргументов команды
        if args_len > 2:
            args = args[2:]
        else:
            args = []
        # Запуск с аргументами
        target_func(args)


if __name__ == '__main__':
    main(command_pool=REGISTERED_COMMANDS)
