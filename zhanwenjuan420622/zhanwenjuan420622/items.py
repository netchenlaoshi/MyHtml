# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Zhanwenjuan420622Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field()
    name = scrapy.Field()
    liutongshizhi = scrapy.Field()
    zhongshizhi = scrapy.Field()
    liutongguben = scrapy.Field()
    zhongguben = scrapy.Field()
    pass
