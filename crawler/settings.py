"""Project wide settings for `ArticleSpider`"""

from fake_useragent import UserAgent

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
