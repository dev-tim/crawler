"""
    Our first `scrapy` spider is born.
"""

from itertools import chain

from scrapy.linkextractors import IGNORED_EXTENSIONS, LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from items import PageItem
from settings import ARTICLE_SPIDER_ALLOWED_DOMAINS, ARTICLE_SPIDER_START_URLS


defaults = IGNORED_EXTENSIONS
url_with_query_string = [r'.*\?.*']
deny = list(chain(url_with_query_string, defaults))

extractor = LinkExtractor(
    deny=deny,
    unique=True
)

follower_rule = Rule(
    link_extractor=extractor,
    callback='retrieve_html',
    follow=True
)


class AricleSpider(CrawlSpider):
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
        self.logger.info("Processing following URL: {}".format(response.url))
        return PageItem(url=response.url)
