import tldextract


class CsvPasswordHandler:

    @staticmethod
    def __get_first_level_domain(url):
        parts = tldextract.extract(url)
        return parts.domain + '.' + parts.suffix

    @staticmethod
    def parse_row(row):
        domain = CsvPasswordHandler.__get_first_level_domain(row[0])
        login = row[1]
        password = row[2]
        return domain, login, password