"""
    Our first `scrapy` spider is born.
"""
import logging

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from crawler.items import PageItem
from crawler.settings import (
    ARTICLE_SPIDER_ALLOWED_DOMAINS,
    ARTICLE_SPIDER_START_URLS,
    DENY_LIST
)

logger = logging.getLogger()

extractor = LinkExtractor(deny=DENY_LIST, unique=True)
follower_rule = Rule(
    link_extractor=extractor,
    callback='retrieve_html',
    follow=True
)


class ArticleSpider(CrawlSpider):
    """
    `ArticleSpider` is a very simple scrapy spider who crawls a single
    domain as defined in `ARTICLE_SPIDER_ALLOWED_DOMAINS` and creates
    `PageItem`'s for further parsing in `pipelines.py`.
    """

    name = "article_spider"
    allowed_domains = ARTICLE_SPIDER_ALLOWED_DOMAINS
    start_urls = ARTICLE_SPIDER_START_URLS
    rules = (follower_rule,)

    def retrieve_html(self, response):
        """For each `response` fed in, return a `PageItem`."""
        logger.info("Processing following URL: {}".format(response.url))
        return PageItem(url=response.url)
