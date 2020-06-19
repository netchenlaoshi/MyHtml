# -*- coding: utf-8 -*-
import scrapy

from zhangzehong45.items import Zhangzehong45Item



class Zzh45zhangzehongSpider(scrapy.Spider):
    name = 'zzh45zhangzehong'
    allowed_domains = ['http://quote.stockstar.com/']
    start_urls = ['http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_1.htm']

    def parse(self, response):
        for i in range(1, 32, 1):
            self.start_urls.append('http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_{}.html'.format(i))
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.chouquyiye)

    def chouquyiye(self, response):
        for i in range(1, 32, 1):
            yield (self.each_stock(response, i))

    def each_stock(self, response, i):
        item = Zhangzehong45Item()
        item['code'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[1]/a/text()'.format(i)).extract()
        item['name'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[2]/a/text()'.format(i)).extract()
        item['liutongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[3]/text()'.format(i)).extract()
        item['zongshizhi'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[4]/text()'.format(i)).extract()
        item['liutongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[5]/text()'.format(i)).extract()
        item['zongguben'] = response.xpath('//*[@id="datalist"]/tr[{}]/td[6]/text()'.format(i)).extract()
        return item