# -*- coding: utf-8 -*-
import scrapy
from jinqianyue14.items import jinqianyue14Item

class jinqianyue14Spider(scrapy.Spider):
    name = 'jinqianyue14'
    allowed_domains = ['quote.stockstar.com']
    start_urls = ['http://quote.stockstar.com/stock/sha.shtml']

    def parse(self, response):
        for i in range(1,33,1):
            self.start_urls.append('http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_{}.html'.format(i))
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.stock_of_page)

    def stock_of_page(self, response):
        for i in range(1, 32, 1):
            yield (self.each_stock(response, i))

    def each_stock(self, response, i):
        item = jinqianyue14Item()
        item['code'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[1]/a/text()'.format(i)).extract()
        item['name'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[2]/a/text()'.format(i)).extract()
        item['liutongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[3]/text()'.format(i)).extract()
        item['zongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[4]/text()'.format(i)).extract()
        item['liutongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[5]/text()'.format(i)).extract()
        item['zongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[6]/text()'.format(i)).extract()
        return item
