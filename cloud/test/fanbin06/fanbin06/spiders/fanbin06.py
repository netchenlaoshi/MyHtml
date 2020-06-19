# -*- coding: utf-8 -*-
import scrapy

from fanbin06.items import Wangzhenquan55121904935Item


class Fanbin06Spider(scrapy.Spider):
    name = 'fanbin06'
    allowed_domains = ['quote.stockstar.com']
    start_urls = ['http://quote.stockstar.com/stock/ranklist_a.shtml']

    def parse(self, response):
        for i in range(2, 130, 1):
            self.start_urls.append('http://quote.stockstar.com/stock/sha_1_0_{}.html'.format(i))
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.stock_of_page)
        yield from self.stock_of_page(response)
        pass

    def stock_of_page(self, response):
        for i in range(1, 31, 1):
            yield (self.stock_of_each(response, i))

    def stock_of_each(self, response,i):
        item = Fanbin55121904906Item()
        item['code'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[1]/a/text()'.format(i)).extract()[0]
        item['name'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[2]/a/text()'.format(i)).extract()[0]
        item['liutongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[3]/text()'.format(i)).extract()[0]
        item['zongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[4]/text()'.format(i)).extract()[0]
        item['liutongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[5]/text()'.format(i)).extract()[0]
        item['zongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[6]/text()'.format(i)).extract()[0]

        return item
