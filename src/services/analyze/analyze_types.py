from pydantic import BaseModel


class AnalyzeResult(BaseModel):
    google_repeats: list[tuple[str, str, str]]
    yandex_repeats: list[tuple[str, str, str]]
    google_not_pair: list[tuple[str, str, str]]
    yandex_not_pair: list[tuple[str, str, str]]
    pair_result: list[tuple[str, str, str]]


class PairResult(BaseModel):
    google: list[tuple[str, str, str]]
    yandex: list[tuple[str, str, str]]


class NotPairResult(BaseModel):
    google: list[tuple[str, str, str]]
    yandex: list[tuple[str, str, str]]
