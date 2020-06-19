# -*- coding: utf-8 -*-
import scrapy
from huangzichen11.items import Huangzichen11Item

class Huangzichen011Spider(scrapy.Spider):
    name = 'huangzichen011'
    allowed_domains = ['stockstar.com']
    start_urls = ['http://quote.stockstar.com/stock/sha.shtml']

    def parse(self, response):
        for i in range(2, 2, 1):
            self.start_urls.append("http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_{}.html".format(i))
        for url in self.start_urls:
            if url=="http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_32.html":
                yield scrapy.Request(url, callback=self.stocks_of_page1)
            else:
                yield scrapy.Request(url, callback=self.stocks_of_page)

    def stocks_of_page(self, response):
        for i in range(1, 31, 1):
            yield (self.each_stock_item(response, i))
    def stocks_of_page1(self, response):
        for i in range(1, 12, 1):
            yield (self.each_stock_item(response, i))

    def each_stock_item(self, response, i):
        item = Huangzichen11Item()
        item['code'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[1]/a/text()'.format(i)).extract()[0]
        item['name'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[2]/a/text()'.format(i)).extract()[0]
        item['liutongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[3]/text()'.format(i)).extract()[0]
        item['zongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[4]/text()'.format(i)).extract()[0]
        item['liutongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[5]/text()'.format(i)).extract()[0]
        item['zongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[6]/text()'.format(i)).extract()[0]

        return item

