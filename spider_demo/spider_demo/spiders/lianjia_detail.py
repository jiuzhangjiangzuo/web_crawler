import json
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from spider_demo.items import LianjiaHouseItemWithDetail, LIANJIA_HOUSE_DETAIL_FIELDS

class LianjiaDetailSpider(CrawlSpider):
    name = 'lianjia_detail'
    allowed_domains = ['hz.lianjia.com']
    start_urls = ['https://hz.lianjia.com/zufang/']
    num_of_item = 0
    item_fields = LIANJIA_HOUSE_DETAIL_FIELDS

    rules = (
        # Handle List Page. Limited only pages 1(start_urls),2 for demo purpose
        Rule(LinkExtractor(allow=r'/zufang/pg[2]{1}/'), callback='parse_list', follow=True),
    )

    def parse_start_url(self, response, **kwargs):
        return self.parse_list(response)

    def parse_list(self, response):
        titles = response.xpath("//p[@class='content__list--item--title']/a/text()").getall()    # Note: --title
        prices = response.xpath("//span[@class='content__list--item-price']/em/text()").getall() # Note: -price
        codes = response.xpath("//div[@class='content__list--item']/@data-house_code").getall()
        links = response.xpath("//p[@class='content__list--item--title']/a/@href").getall()

        for title, price, code, link in zip(titles, prices, codes, links):
            item = LianjiaHouseItemWithDetail(title=title.strip(), price=price.strip(), code=code.strip())
            yield response.follow(link, self.parse_detail, cb_kwargs=dict(item=item))

    def parse_detail(self, response, item):
        descriptions = response.xpath("//div[@class='content__article__info']/ul/li/text()").getall()
        detail = []
        for desc in descriptions:
            desc = desc.strip()
            if len(desc):
                detail.append(desc)

        item['detail'] = json.dumps(detail)
        return item
