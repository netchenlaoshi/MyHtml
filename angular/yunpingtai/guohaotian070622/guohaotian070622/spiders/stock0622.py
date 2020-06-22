# -*- coding: utf-8 -*-
import scrapy

from guohaotian070622.items import Guohaotian070622Item


class Stock0622Spider(scrapy.Spider):
    name = 'stock0622'
    allowed_domains = ['stockstar.com']
    start_urls = ['http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_1.html']

    def parse(self, response):
        for i in range(2,33,1):
            self.start_urls.append('http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_{}.html'.format(i))
        for url in self.start_urls:
            yield scrapy.Request(url,callback=self.stocks_of_page)
        #yield from self.stocks_of_page(response)

    def stocks_of_page(self, response):
        for i in range(1, 31, 1):
            yield (self.each_stock(response, i))

    def each_stock(self, response,i):
        item = Guohaotian070622Item()
        item['code'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[1]/a/text()'.format(i)).extract()[0]
        item['name'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[2]/a/text()'.format(i)).extract()[0]
        item['liutongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[3]/text()'.format(i)).extract()[0]
        item['zongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[4]/text()'.format(i)).extract()[0]
        item['liutongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[5]/text()'.format(i)).extract()[0]
        item['zongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[6]/text()'.format(i)).extract()[0]
        # print('code=', item['code'])
        # print('name=', item['name'])
        # print('liutongshizhi=', item['liutongshizhi'])
        # print('zongshizhi=', item['zongshizhi'])
        # print('liutongguben=', item['liutongguben'])
        # print('zongguben=', item['zongguben'])
        return item
