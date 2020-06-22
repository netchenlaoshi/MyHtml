# -*- coding: utf-8 -*-
import scrapy
from zhanwenjuan420622.items import Zhanwenjuan420622Item

class Zhanwenjuan420622Spider(scrapy.Spider):
    name = 'zhanwenjuan420622'
    allowed_domains = ['stockstar.com']
    start_urls = ['http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_1.html']

    def parse(self, response):
        for i in range(2,55,1):
            self.start_urls.append("http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_2.html".format(i))
        yield from self.stock_of_page(response)

            #yield scrapy.Request(url, callback=self.stock_of_page)

    def stock_of_page(self, response):
        for i in range(1, 32, 1):
            yield (self.each_stock(response,i))

    def each_stock(self, response, i):
        item = Zhanwenjuan420622Item()
        item['code'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[1]/a/text()'.format(i)).extract()
        item['name'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[2]/a/text()'.format(i)).extract()
        item['liutongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[3]/text()'.format(i)).extract()
        item['zhongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[4]/text()'.format(i)).extract()
        item['liutongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[5]/text()'.format(i)).extract()
        item['zhongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[6]/text()'.format(i)).extract()
        return item
