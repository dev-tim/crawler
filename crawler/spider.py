from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider
from scrapy.crawler import CrawlerProcess

results = []


def run_me():
    process = CrawlerProcess({})
    urls = ["http://drstevesavage.com"]
    process.crawl(Spider, start_urls=urls)
    process.start()


class Item(Item):
    url = Field()
    referer = Field()
    status = Field()


class Spider(CrawlSpider):
    name = "savage_crawler"

    def parse_item(self, response):
        results.append(Spider(url=response.url))

if __name__ == "__main__":
    run_me()
    print(results)
