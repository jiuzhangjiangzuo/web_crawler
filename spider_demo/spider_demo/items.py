# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

LIANJIA_HOUSE_FIELDS = ['title', 'price']

class LianjiaHouseItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
