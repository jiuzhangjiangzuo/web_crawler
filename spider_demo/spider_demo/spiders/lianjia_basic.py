import scrapy
import os
from lxml import etree
from spider_demo.items import LianjiaHouseItem

class LianjiaBasicSpider(scrapy.Spider):
    # 爬虫的名字
    name = 'lianjia_basic'
    # 允许的域名
    allowed_domains = ['hz.lianjia.com']
    # 起始的url
    start_urls = ['http://hz.lianjia.com/zufang/']

    DOWNLOAD_PATH = 'download_lianjia'

    # def start_requests(self):
    #     for i in range(10):
    #         url = "https://hz.lianjia.com/zufang/pg{}/#contentList".format(i)
    #         yield scrapy.FormRequest(url, callback=self.parse)

    def parse_basic(self, response):
        # 'http://hz.lianjia.com/zufang/' => ['http:', '', 'hz.lianjia.com', 'zufang', '']
        page = response.url.split("/")[-2]  # => page = 'zufang'
        filename = 'lianjia-%s.html' % page # => filename = 'lianjia-zufang.html'
        os.makedirs(self.DOWNLOAD_PATH, exist_ok=True)
        with open(os.path.join(self.DOWNLOAD_PATH, filename), 'wb') as f:     #
            f.write(response.body)
        self.log('Saved file %s' % filename)

    def parse_print_abstract(self, response):
        titles = response.xpath("//p[@class='content__list--item--title']/a/text()").getall()    # Note: --title
        prices = response.xpath("//span[@class='content__list--item-price']/em/text()").getall() # Note: -price

        print("================START===================")
        for title, price in zip(titles, prices):
            print("{} => {}".format(title.strip(), price))
        print("================END===================")

    def parse_list(self, response):
        titles = response.xpath("//p[@class='content__list--item--title']/a/text()").getall()    # Note: --title
        prices = response.xpath("//span[@class='content__list--item-price']/em/text()").getall() # Note: -price

        for title, price in zip(titles, prices):
            yield LianjiaHouseItem(title=title.strip(), price=price.strip())

    def parse_list_page_by_page(self, response):
        titles = response.xpath("//p[@class='content__list--item--title']/a/text()").getall()    # Note: --title
        prices = response.xpath("//span[@class='content__list--item-price']/em/text()").getall() # Note: -price

        for title, price in zip(titles, prices):
            yield LianjiaHouseItem(title=title.strip(), price=price.strip())

        total_page = int(response.xpath("//div[@class='content__pg']/@data-totalpage").get()) #lowercase attribute
        cur_page = int(response.xpath("//div[@class='content__pg']/@data-curpage").get())    #lowercase attribute
        if cur_page < total_page:
            yield scrapy.Request('https://hz.lianjia.com/zufang/pg{}/#contentList'.format(cur_page + 1), self.parse)

    def parse(self, response):
        #return self.parse_basic(response)
        #return self.parse_print_abstract(response)
        #return self.parse_list(response)
        return self.parse_list_page_by_page(response)
