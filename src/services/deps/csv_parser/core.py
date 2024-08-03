import csv
from typing import Callable


class CsvParser:

    @staticmethod
    def parse_csv(path, row_handler: Callable):
        parsed_data = []
        with open(path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                parsed_data.append(row_handler(row))
        return parsed_data
