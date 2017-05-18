# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from cosplay.items import AcgItem


class A17173Spider(scrapy.Spider):
    name = "17173"
    allowed_domains = ["17173.com"]
    start_urls = (
        'http://acg.17173.com/cosplay/',
        # 'http://acg.17173.com/content/06062016/101602650_1.shtml',
        # 'http://acg.17173.com/news/04232015/163445518_1.shtml'
    )

    def parse(self, response):

        image_page_url = response.xpath('//div[@class="comm-pn"]/ul/li[@class="item"]/div/a/@href').extract()
        for i in image_page_url:
            yield Request(url=i, callback=self.Get_Pages)

        try:
            next = response.xpath('//div[@class="pagination"]/ul/li/a/@href').extract()
            for i in next:
                yield  Request(url=i, callback=self.parse)
        except:
            pass


    def Get_Pages(self, response):

        try:
            next = response.xpath('//div[@class="gb-final-mod-pagination-in"]/a/@href').extract()
            next.append(response.url)
            if next:
                for i in next:
                    yield Request(url=i, callback=self.get_image_details)
            else:
                yield Request(url=response.url, callback=self.get_image_details)
        except:
            pass

    def get_image_details(self, response):

        image_url = response.xpath('//div[@class="gb-final-mod-article"]/p[@class="p-image"]/a/@href').extract()
        if len(image_url) < 1:
            image_url= response.xpath('//div[@class="gb-final-mod-article"]/p[@align="center"]/a/img/@src').extract()
        if len(image_url) < 1:
            image_url = response.xpath('//div[@class="gb-final-mod-article"]/p[@class="p-image"]/img/@src').extract()

        title = response.xpath('//div[@class="gb-final-pn-article"]/h1[@class="gb-final-tit-article"]/text()').extract()
        content = response.xpath('//div[@class="gb-final-mod-article"]/p/text()').extract()
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

        items = AcgItem()
        items["title"] = title[0]

        items["url"]  = response.url
        if len(content) == 0:
            items['content'] = "."
        else:
            # print len(content)
            items['content'] = content[0]

        # print items['content']
        items["image"] = item
        return items

