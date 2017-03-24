# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from chespider import settings
from chespider.items import MastarItem
from scrapy.http import Request


class CarSpider(scrapy.Spider):
    name = "master"
    allowed_domains = ["renrenche.com"]
    start_urls = (
        'http://www.renrenche.com/cn/ershouche/',
    )

    def parse(self, response):

        item = MastarItem()
        sel = Selector(response)
        ItemUrls = sel.xpath('//li[@class="span6 list-item"]/a/@href').extract()

        for url in ItemUrls:
            url = settings.BaseUrl + url
            item["DetailURL"] = url
            yield item
                # 获取分页信息
        pages = sel.xpath('//ul[@class="pagination"]/li/a/@href').extract()
        for page in pages:
            page = settings.BaseUrl + page
            if "javascript" in page:
                pass
            else:
                # pass
                yield Request(url=page, callback=self.parse)