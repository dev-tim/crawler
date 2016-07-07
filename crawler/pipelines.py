"""
    As defined in `settings.py`, we provide classes here which
    perform a single, well defined operation on a `PageItem` created
    by `ArticleSpider`.
"""

import logging

logger = logging.getLogger()


class ParseRawHtml():
    """@TODO"""

    def process_item(self, item, spider):
        """@TODO"""
        logger.info("Parsing item: {}".format(item))
        return item
