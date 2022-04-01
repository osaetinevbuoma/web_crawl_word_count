import pytest
from bs4 import BeautifulSoup

from crawler.custom_exceptions import UrlNotFoundException
from crawler.parser import Parser


def test_parser_supplied_with_valid_url():
    parsed_url = Parser.parse("https://www.bbc.co.uk")
    assert type(parsed_url) is BeautifulSoup


def test_parser_supplied_with_invalid_url():
    invalid_url = "http://www.invaliddomainname.com"
    with pytest.raises(UrlNotFoundException) as ex:
        Parser.parse(invalid_url)

    assert ex.value.message == f"{invalid_url} does not exist"
