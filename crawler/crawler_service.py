import re

from crawler.custom_exceptions import UrlNotProvidedException
from crawler.parser import Parser


def get_word_occurrence(url):
    if url == "" or url is None:
        raise UrlNotProvidedException("Url must be provided")

    parsed_content = Parser.parse(url)
    return count_string_occurrence(parsed_content)


def count_string_occurrence(content):
    occurrence = {}

    for sentence in content.stripped_strings:
        words = re.findall(r"\b\S+\b", sentence)
        for word in words:
            if word.lower() in occurrence:
                occurrence[word.lower()] += 1
            else:
                occurrence[word.lower()] = 1

    return dict(sorted(occurrence.items(), key=lambda item: item[0]))
