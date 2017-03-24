# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "images"
    allowed_domains = ["uumnt.com/"]
    start_urls = (
        'http://www.uumnt.com/',
    )

    def parse(self, response):
        # 获取栏目连接

        pass
