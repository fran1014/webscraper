import scrapy


class RmfcspiderSpider(scrapy.Spider):
    name = "rmfcspider"
    allowed_domains = ["www.realmadrid.com"]
    start_urls = ["https://www.realmadrid.com/es-ES"]

    def parse(self, response):
        pass
