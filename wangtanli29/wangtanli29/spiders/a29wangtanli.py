# -*- coding: utf-8 -*-
import scrapy

from wangtanli29.items import Wangtanli29Item


class a29wangtanliSpider(scrapy.Spider):
    name = 'a29wangtanli'
    allowed_domains = ['wangtanli29.com']
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

    def each_stock(self, response,i):
        item = Wangtanli29Item()
        item['code'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[1]/a/text()'.format(i))
        item['name'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[2]/a/text()'.format(i))
        item['liutongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[3]/text()'.format(i))
        item['zongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[4]/text()'.format(i))
        item['liutongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[5]/text()'.format(i))
        item['zongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[6]/text()'.format(i))
        #print("code=", item['code'])
        #print("name=", item['name'])
        #print("liutongshizhi=", item['liutongshizhi'])
        #print('liutongguben=', item['liutongguben'])
        #print("zongshizhi=", item['zongshizhi'])
        #print("zongguben=", item['zongguben'])
        return item
