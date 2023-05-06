import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class YubaSpider(scrapy.Spider):
    name = "yuba"
    allowed_domains = ["www.doseeing.com"]
    start_urls = ["https://www.doseeing.com/room/48699"]

    # rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)

    def parse(self, response):
        item = {}
        item['pub_time'] = '2023-03-01 22:22:22'
        self.logger.info("ruurrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        self.logger.info(response.body, 'utf-8')
        self.logger.info("ruurrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        return item
