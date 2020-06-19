# -*- coding: utf-8 -*-
import scrapy
from huangqinglang14.items import Huangqinglang14Item

class Huangqinglang14Spider(scrapy.Spider):
    name = 'Huangqinglang14'
    allowed_domains = ['stockstar.com']
    start_urls = ['http://quote.stockstar.com/stock/sha.shtml']

    def parse(self, response):
        for i in range(2, 32, 1):
            self.start_urls.append("http://quote.stockstar.com/stock/sha_1_0_{}.html".format(i))
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.stocks_of_page)

        yield from self.stocks_of_page(response)

    def stocks_of_page(self, response):
        for i in range(1, 31, 1):
            item = self.each_stock(response, i)
            yield item


    def each_stock(self, response, i):
        item = Huangqinglang14Item()
        item['code'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[1]/a/text()'.format(i)).extract()[0]
        item['name'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[2]/a/text()'.format(i)).extract()[0]
        item['liutongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[3]/text()'.format(i)).extract()[0]
        item['zhongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[4]/text()'.format(i)).extract()[0]
        item['liutongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[5]/text()'.format(i)).extract()[0]
        item['zhongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[6]/text()'.format(i)).extract()[0]
        # print("liutongguben", item['code'])
        # print("name=", item['name'])
        # print("liutongshizhi=", item['liutongshizhi'])
        # print("zhongshizhi=", item['zhongshizhi'])
        # print("liutongguben=", item['liutongguben'])
        # print("zhongguben=", item['zhongguben'])
        return item