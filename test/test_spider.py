import re


def test_deny_list(sample_urls, url):
    """`DENY_LIST` correctly filters URLS with query strings"""
    from crawler.settings import DENY_LIST

    regex = re.compile(DENY_LIST[0])
    filtered = filter(lambda url: not regex.search(url), sample_urls)
    assert url == next(filtered)


def test_expected_logging(caplog, response, url):
    """`ArticleSpider` and `ParseRawHtml` correctly log messages"""
    from crawler.items import PageItem
    from crawler.pipelines import ParseRawHtml
    from crawler.spider import ArticleSpider

    ArticleSpider.retrieve_html(ArticleSpider, response=response)
    ParseRawHtml.process_item(ParseRawHtml, PageItem(url='foo'), ArticleSpider)

    logs = [record.message for record in caplog.records()]

    assert "Processing following URL: {}".format(url) in logs
    assert "Parsing item: {'url': 'foo'}" in logs


def test_article_spider_produces_correct_urls(response, url):
    """ArticleSpider creates a `PageItem` for a given URL"""
    from crawler.spider import ArticleSpider

    result = ArticleSpider.retrieve_html(ArticleSpider, response=response)
    assert result == {'url': url}
