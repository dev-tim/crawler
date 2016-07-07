import pytest

from scrapy.http import TextResponse, Request


@pytest.fixture
def sample_urls():
    return [
        'http://www.foo.com/',
        'http://www.foo.com/?foo=bar'
    ]


@pytest.fixture
def url():
    return 'http://www.foo.com/'


@pytest.fixture
def response(url):
    response = TextResponse(
        url=url,
        request=Request(url=url),
        body='<html></html>',
        encoding='utf-8'
    )
    return response
