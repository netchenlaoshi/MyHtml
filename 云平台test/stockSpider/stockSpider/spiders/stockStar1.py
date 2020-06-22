# -*- coding: utf-8 -*-
import scrapy

# from stockSpider.stockSpider.items import StockspiderItem
from stockSpider.items import StockspiderItem1


class Stockstar1Spider(scrapy.Spider):
    name = 'stockStar1'
    allowed_domains = ['stockstar.com']
    start_urls = ['http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_1.html']

    def parse(self, response):
        for i in range(1, 2, 1):
            self.start_urls.append("http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_{}.html".format(i))
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.stocks_of_page)

    def stocks_of_page(self, response):
        for i in range(1, 31, 1):
            yield (self.each_stock(response, i))

    def each_stock(self, response, i):
        item1 = StockspiderItem1()
        item1['code1'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[1]/a/text()'.format(i)).extract()[0]

        #  //*[@id="datalist"]/tr[{}]/td[3]
        #   item['code1'] = response.xpath('//*[@id="content"]/div/div[2]/div[3]/div[3]/div/div[1]/div/div[2]/a[{}]/p'.format(i)).extract()[0]
        item1['name1'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[2]/a/text()'.format(i)).extract()[0]
        item1['liutongshizhi1'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[3]/text()'.format(i)).extract()[0]
        item1['zhongshizhi1'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[4]/text()'.format(i)).extract()[0]
        item1['liutongguben1'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[5]/text()'.format(i)).extract()[0]
        item1['zhongguben1'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[6]/text()'.format(i)).extract()[0]

        return item1
