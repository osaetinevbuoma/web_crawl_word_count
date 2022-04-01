import requests
from bs4 import BeautifulSoup

from crawler.custom_exceptions import UrlNotFoundException


class Parser:
    """
    Although we are using BeautifulSoup library to parse HTML content, the purpose of
    the Parser wrapper class is to wrap the functionality our selected parsing library. This way, if
    in the future there is the need to use a different parsing library, that switch can be done
    very easily in the Parser class without affecting the rest of the application.
    """

    @staticmethod
    def parse(url):
        try:
            page = requests.get(url, stream=True)
            return BeautifulSoup(page.content, "lxml")
        except requests.exceptions.RequestException as ex:
            raise UrlNotFoundException(f'{url} does not exist') from ex
