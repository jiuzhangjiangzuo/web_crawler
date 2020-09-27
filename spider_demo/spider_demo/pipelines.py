# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from spider_demo.items import LIANJIA_HOUSE_FIELDS
import csv

class LianjiaCollectDataPipeline:
    def open_spider(self, spider):
        self.csv_file = open('data/result.csv', 'w')
        self.csv_writer = csv.DictWriter(self.csv_file, fieldnames = spider.item_fields)
        self.csv_writer.writeheader()

    def close_spider(self, spider):
        self.csv_file.close()

    def process_item(self, item, spider):
        self.csv_writer.writerow(item)
