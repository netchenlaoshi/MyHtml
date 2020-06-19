import  scrapy


class linyumeng19Item(scrapy.Item):
     name = scrapy.Field()
     Responsibility = scrapy.Field()

class gupiao19Item(scrapy.Item):
    code = scrapy.Field()
    name = scrapy.Field()
    liutongshizhi = scrapy.Field()
    zhongshizhi = scrapy.Field()
    liutongguben = scrapy.Field()
    zhongguben = scrapy.Field()


