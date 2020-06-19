# -*- coding: utf-8 -*-
import scrapy

from Cloud.test.linyumeng19.linyumeng19.linyumeng19.items import Linyumeng19Item


class A19linyumengSpider(scrapy.Spider):
    name = '19linyumeng'
    allowed_domains = ['http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_1.html']
    start_urls = ['http://quote.stockstar.com/stock/ranklist_a.shtml']

    def parse(self, response):
        # for i in range(2, 130, 1):
        #     self.start_urls.append('http://quote.stockstar.com/stock/sha_1_0_{}.html'.format(i))
        # for url in self.start_urls:
        #     yield scrapy.Request(url, callback=self.stock_of_page)
        yield from self.stock_of_page(response)
        pass

    def stock_of_page(self, response):
        for i in range(1, 31, 1):
            yield (self.stock_of_each(response, i))

    def stock_of_each(self, response,i):
        item = Linyumeng19Item()
        item['code'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[1]/a/text()'.format(i)).extract()[0]
        item['name'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[2]/a/text()'.format(i)).extract()[0]
        item['liutongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[3]/text()'.format(i)).extract()[0]
        item['zongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[4]/text()'.format(i)).extract()[0]
        item['liutongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[5]/text()'.format(i)).extract()[0]
        item['zongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[6]/text()'.format(i)).extract()[0]

        return item