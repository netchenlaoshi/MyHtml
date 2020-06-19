# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import scrapy

from niweikang24.items import Niweikang24Item


class A24niweikangSpider(scrapy.Spider):
    name = '24niweikang'
    allowed_domains = ['quote.stockstar.com']
    start_urls = ['http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_1.html']

    def parse(self, response):
        for i in range(1,33,1):
            self.start_urls.append('http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_{}.html'.format(i))
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.stock_of_page)

    def stock_of_page(self, response):
        for i in range(1, 32, 1):
            yield (self.each_stock_item(response, i))

    def each_stock_item(self, response,i):
        item = Niweikang24Item()
        item['code'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[1]/a/text()'.format(i)).extract()[0]
        item['jiancheng'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[2]/a/text()'.format(i)).extract()[0]
        item['liutongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[3]/text()'.format(i)).extract()[0]
        item['zongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[4]/text()'.format(i)).extract()[0]
        item['liutongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[5]/text()'.format(i)).extract()[0]
        item['zongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[5]/text()'.format(i)).extract()[0]
        return item