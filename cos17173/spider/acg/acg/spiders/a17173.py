# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from acg.items import AcgItem


class A17173Spider(scrapy.Spider):
    name = "17173"
    allowed_domains = ["17173.com"]
    start_urls = (
        'http://acg.17173.com/cosplay/',
    )

    def parse(self, response):

        image_page_url = response.xpath('//div[@class="comm-pn"]/ul/li[@class="item"]/div/a/@href').extract()
        for i in image_page_url:
            yield Request(url=i, callback=self.get_image_details)

        try:
            next = response.xpath('//div[@class="pagination"]/ul/li/a/@href').extract()
            for i in next:
                yield  Request(url=i, callback=self.parse)
        except:
            pass


    def get_image_details(self, response):

        image_url = response.xpath('//div[@class="gb-final-mod-article"]/p[@class="p-image"]/a/@href').extract()
        if len(image_url) < 1:
            image_url= response.xpath('//div[@class="gb-final-mod-article"]/p[@align="center"]/a/img/@src').extract()
        if len(image_url) < 1:
            image_url = response.xpath('//div[@class="gb-final-mod-article"]/p[@class="p-image"]/img/@src').extract()

        title = response.xpath('//div[@class="gb-final-pn-article"]/h1[@class="gb-final-tit-article"]/text()').extract()
        item = []
        for i in image_url:
            if len(image_url) < 1:
                pass
            else:
                aa = i.split('url=')
                if len(aa) > 1:
                    item.append(aa[1])
                else:
                    item.append(i)
        try:
            next = response.xpath('//div[@class="gb-final-mod-pagination-in"]/a[@class="gb-final-page-next"]/@href').extract()
            for i in next:
                Request(url=i, callback=self.get_image_details)
        except:
            pass

        items = AcgItem()
        items["name"] = title
        items["url"]  = response.url
        items["image"] = item

        return items




