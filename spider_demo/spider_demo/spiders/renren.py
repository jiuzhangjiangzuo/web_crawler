import scrapy

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/SysHome.do']

    def parse(self, response):

        login_form = {
            'email': 'dongqs1210@163.com',
            'password': 'scrapy_demo',
            'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'
        }

        return scrapy.FormRequest(url='http://www.renren.com/PLogin.do',
                    formdata=login_form, callback=self.after_login, dont_filter=True)

    def after_login(self, response):
        with open("download/renren.html", "wb") as file:
            file.write(response.body)
