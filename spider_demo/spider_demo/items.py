# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

LIANJIA_HOUSE_FIELDS = ['title', 'price']
LIANJIA_HOUSE_DETAIL_FIELDS = ['title', 'price', 'code', 'detail']

class LianjiaHouseItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()


class LianjiaHouseItemWithDetail(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    code = scrapy.Field()
    detail = scrapy.Field()
