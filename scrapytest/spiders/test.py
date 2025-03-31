import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["test.com"]
    start_urls = ["https://toscrape.com/"]

    def parse(self, response):
        print("dfsdgsdgfsdgsdgsdlgfhsdkgsudguIvjKDvfjyE")
