from zxcvbn import zxcvbn
from src.services.analyze.analyze_types import ListPasswordRecords


def get_set(passwords_list: ListPasswordRecords, depth: int) -> set:
    """
    Получение сета кортежей c определенной глубиной.
    """
    return set(tuple(sorted(t)) for t in [tuple_in_depth(record, depth) for record in passwords_list])


def tuple_in_depth(data: tuple[str, str, str], depth: int):
    return tuple(
        sorted(
            tuple(
                [data[index] for index in range(depth)]
            )
        )
    )


def find_first_in_second(first: ListPasswordRecords, second: ListPasswordRecords,
                         depth: int, include=True) -> ListPasswordRecords:
    if include:
        return [t for t in first if tuple_in_depth(t, depth) in get_set(second, depth)]
    else:
        return [t for t in first if tuple_in_depth(t, depth) not in get_set(second, depth)]


def check_password_to_weak(password: str) -> bool:
    """
    Проверка пароля на слабость.
    """
    results = zxcvbn(password)
    score = results.get('score')
    if isinstance(score, int) and score < 3:
        return True
    return False


def find_repeats(data: ListPasswordRecords, unique=False) -> ListPasswordRecords:
    """
    Получение списка повторов.
    """
    seen = set()
    duplicates = set()
    unique_records = set()
    for record in data:
        pair = tuple(record[:2])
        if pair in seen:
            duplicates.add(record)
        else:
            seen.add(pair)
            unique_records.add(record)
    return list(unique_records) if unique else list(duplicates)
