import scrapy

class DmozSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "https://xueshu.baidu.com/"
    ]

    def parse(self, response):
        print(response.body)