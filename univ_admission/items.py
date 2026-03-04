import scrapy

class JbcrcItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
    category = scrapy.Field()
    year = scrapy.Field()
    source = scrapy.Field()
