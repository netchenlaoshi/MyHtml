# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Wangzhenquan55121904935Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code=scrapy.Field()
    name = scrapy.Field()
    liutongshizhi = scrapy.Field()
    zongshizhi = scrapy.Field()
    liutongguben = scrapy.Field()
    zongguben = scrapy.Field()
    pass
