import re


def test_deny_list(sample_urls, url):
    """`DENY_LIST` correctly filters URLS with query strings"""
    from crawler.settings import DENY_LIST

    regex = re.compile(DENY_LIST[0])
    filtered = filter(lambda url: not regex.search(url), sample_urls)
    assert url == next(filtered)


def test_article_spider_produces_correct_urls(response, url):
    """ArticleSpider creates a `PageItem` for a given URL"""
    from crawler.spider import ArticleSpider

    result = ArticleSpider.retrieve_html(ArticleSpider, response=response)
    assert result == {'url': url}
