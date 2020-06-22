# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class wfm551219049370622(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field()
    name = scrapy.Field()
    liutongshizhi = scrapy.Field()
    zhongshizhi = scrapy.Field()
    liutongguben = scrapy.Field()
    zhongguben = scrapy.Field()
    # pass


class StockspiderItem1(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code1 = scrapy.Field()
    name1=scrapy.Field()
    liutongshizhi1 = scrapy.Field()
    zhongshizhi1 = scrapy.Field()
    liutongguben1 = scrapy.Field()
    zhongguben1 = scrapy.Field()
