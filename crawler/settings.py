"""Project wide settings for `ArticleSpider`"""

from itertools import chain

from fake_useragent import UserAgent
from scrapy.linkextractors import IGNORED_EXTENSIONS

# scrapy standard settings:
# http://doc.scrapy.org/en/1.1/topics/settings.html#user-agent
USER_AGENT = UserAgent().random

# http://doc.scrapy.org/en/1.1/topics/settings.html#robotstxt-obey
ROBOTSTXT_OBEY = True

# http://doc.scrapy.org/en/1.1/topics/settings.html#log-level
LOG_LEVEL = 'INFO'

# http://doc.scrapy.org/en/1.1/topics/settings.html#item-pipelines
ITEM_PIPELINES = {
    'crawler.pipelines.ParseRawHtml': 1
}

# custom settings below:
# Manually configured domains for now
ARTICLE_SPIDER_ALLOWED_DOMAINS = [
    "drstevesavage.com",
]

ARTICLE_SPIDER_START_URLS = [
    "http://drstevesavage.com",
]

defaults = IGNORED_EXTENSIONS
url_with_query_string = [r'.*\?.*']
DENY_LIST = list(chain(url_with_query_string, defaults))
