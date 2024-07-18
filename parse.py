import os
import csv
import pyzipper
import tldextract

from src.settings import settings


def find_file():
    for file in os.listdir(settings.INPUT_PATH):
        if file.endswith(".zip"):
            return os.path.join(settings.INPUT_PATH, file)


def get_first_level_domain(url):
    parts = tldextract.extract(url)
    return parts.domain + '.' + parts.suffix


def unzip_file_AES(zip_filepath, dest_path, password):
    with pyzipper.AESZipFile(zip_filepath) as zf:
        zf.extractall(dest_path, pwd=bytes(password, 'utf-8'))


def parse_row(row):
    domain = get_first_level_domain(row[0])
    login = row[1]
    password = row[2]
    return domain, login, password


def parse_csv(path):
    parsed_data = []
    with open(path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            parsed_data.append(parse_row(row))
    return parsed_data


if __name__ == '__main__':
    unzip_file_AES(find_file(), settings.TEMP_DATA_PATH, settings.ARCHIVE_PASSWORD)
    csv_path = os.path.join(settings.TEMP_DATA_PATH, "passwords.csv")
    data = parse_csv(csv_path)
    os.remove(csv_path)
    print(data)
