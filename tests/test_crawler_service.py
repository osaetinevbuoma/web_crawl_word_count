import pytest
from bs4 import BeautifulSoup

from crawler.crawler_service import count_string_occurrence, get_word_occurrence
from crawler.custom_exceptions import UrlNotProvidedException

sentence = "Tell the audience what you're going to say. Say it. Then tell them what you've said."


def test_count_string_occurrence():
    html_doc = """
        <html>
            <head>
                <title></title>
            </head>
            <body>
                <p>
                    Tell the audience what you're going to say. Say it. Then tell them what you've said.
                </p>
            </body>
        </html>
    """
    soup = BeautifulSoup(html_doc, "lxml")
    occurrence = count_string_occurrence(soup)
    expected_result = {
        "tell": 2,
        "the": 1,
        "audience": 1,
        "what": 2,
        "you're": 1,
        "going": 1,
        "to": 1,
        "say": 2,
        "it": 1,
        "then": 1,
        "them": 1,
        "you've": 1,
        "said": 1
    }
    assert occurrence == expected_result


def test_get_word_occurrence_with_valid_url():
    occurrence = get_word_occurrence("https://bbc.co.uk")
    assert occurrence != {}
    assert len(occurrence.keys()) > 0


def test_get_word_occurrence_with_invalid_url():
    with pytest.raises(UrlNotProvidedException) as ex:
        get_word_occurrence(None)

    assert ex.value.message == "Url must be provided"
