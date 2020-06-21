# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class zhujiahao49Item(scrapy.Item):
    code = scrapy.Field()  # 股票代码
    name = scrapy.Field()  # 股票简称
    liutongshizhi = scrapy.Field()  # 流通市值
    zongshizhi = scrapy.Field()  # 总市值
    liutongguben = scrapy.Field()  # 流通股本吧
    zongguben = scrapy.Field()  # 总股本
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


