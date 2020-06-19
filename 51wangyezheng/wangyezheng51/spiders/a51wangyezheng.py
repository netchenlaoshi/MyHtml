# -*- coding: utf-8 -*-
import scrapy

from wangyezheng51.items import Wangyezheng51Item


class A51wangyezhengSpider(scrapy.Spider):
    name = '51wangyezheng'
    allowed_domains = ['quote.stockstar.com']
    start_urls = ['http://quote.stockstar.com/stock/sha.shtml']

    def parse(self, response):
        for i in range(2, 32, 1):
            self.start_urls.append(
                "http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_{}.html".format(i))
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.stocks_of_page)

    def stocks_of_page(self, response):
        for i in range(1, 31, 1):
            yield (self.each_stock(response, i))

    def each_stock(self, response, i):  # 撰写爬虫逻辑
        item = Wangyezheng51Item()
        item['code'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[1]/a/text()'.format(i)).extract()[0]
        item['name'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[2]/a/text()'.format(i)).extract()[0]
        item['liutongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[3]/text()'.format(i)).extract()[0]
        item['zongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[4]/text()'.format(i)).extract()[0]
        item['liutongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[5]/text()'.format(i)).extract()[0]
        item['zongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[6]/text()'.format(i)).extract()[0]
        print('股票代码:', item['code'])
        print('股票简称:', item['name'])
        print('流通市值:', item['liutongshizhi'])
        print('总市值:', item['zongshizhi'])
        print('流通股本:', item['liutongguben'])
        print('总股本:', item['zongguben'])
        return item

