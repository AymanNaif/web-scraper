from web_scraper import __version__

from web_scraper.scraper import get_citations_needed_report, get_citations_needed_count


def test_version():
    assert __version__ == '0.1.0'


def test_count():

    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"

    assert get_citations_needed_count(URL) == 5


def test_report():
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    expected = open("citation.txt", "r")

    assert get_citations_needed_report(URL) == expected.read()
