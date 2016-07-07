"""
The model for `ArticleSpider`.
"""

import scrapy


class PageItem(scrapy.Item):
    """
        A `PageItem` corresponds to a single HTML page
        retrieved by `ArticleSpider`. We only store the
        URL for now.
    """
    url = scrapy.Field()
