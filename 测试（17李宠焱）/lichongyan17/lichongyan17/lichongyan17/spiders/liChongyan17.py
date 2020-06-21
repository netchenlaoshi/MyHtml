# -*- coding: utf-8 -*-
import scrapy
from lichongyan17.items import  Lichongyan17Item

class Lichongyan17Spider(scrapy.Spider):
    name = 'liChongyan17'
    allowed_domains = ['stockstar.com']
    start_urls = ['http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_1.html']

    def parse(self, response):
        for i in range(2,31,1):
            self.start_urls.append('http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_{}.html'.format(i))
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.stocks_of_page)


    def stocks_of_page(self, response):
        items = []
        for i in range(1, 31, 1):
            yield (self.each_stock_item(response, i))



    def each_stock_item(self, response, i):
        item = Lichongyan17Item()
        item['code'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[1]/a/text()'.format(i)).extract()
        item['name'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[2]/a/text()'.format(i)).extract()
        item['liutongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[3]/text()'.format(i)).extract()
        item['zongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[4]/text()'.format(i)).extract()
        item['liutongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[5]/text()'.format(i)).extract()
        item['zongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[6]/text()'.format(i)).extract()
        return item

