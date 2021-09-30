from scrapy import Request
from scrapy.spiders import Spider
from tutorial.items import electricityItem
from tutorial.Email import mail
import logging
import time


class ElectricitySpider(Spider):
    name = 'electricity_query'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'http://wap.xt.beescrm.com/base/electricityHd/queryResult/ele_id/7/community_id/57/building_id/300/floor_id/2180/room_id/38603/flag/1'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = electricityItem()
        remains = response.xpath('/html/body/div/div[3]/p[1]/span/text()').extract()[0]
        remains = float(remains[:len(remains)-1])
        print(type(remains))
        print(remains > 10)
        print(remains)
        if remains < 10:
            mail(str(remains))
            # logging.info("An email was sent in"+time.asctime(time.localtime(time.time())))
        item['remains'] = remains
        yield item
