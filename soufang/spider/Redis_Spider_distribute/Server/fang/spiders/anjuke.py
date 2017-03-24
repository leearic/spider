# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import  Request

from fang.items import ServerItem

class ASpider(scrapy.Spider):
    name = "server"
    allowed_domains = ["anjuke.com"]
    start_urls = (
        'http://www.anjuke.com/sy-city.html',
    )

    def parse(self, response):

        # 从全国地区获取到每一个地区的二级域名
        urls =  response.xpath('//div[@class="cities_boxer"]/div/dl/dd/a/@href').extract()
        zones =  response.xpath('//div[@class="cities_boxer"]/div/dl/dd/a/text()').extract()

        for i in xrange(len(urls)):
            url = urls[i]+'/sale/'
            yield Request(url=url, callback=self.get_zone_house_info, meta={'zone': zones[0]})

    def get_zone_house_info(self, response):
        zone =  response.meta['zone']
        pages = response.xpath('//div[@class="multi-page"]/a/@href').extract()
        for page in pages:
            yield  Request(url=page, callback=self.get_zone_house_info, meta={'zone': zone})

        urls = response.xpath('//div[@class="sale-left"]/ul/li/div[@class="house-details"]/div/a/@href').extract()
        for i in urls:
            yield  self.get_house_detail_info(zone, i)
            # yield  Request(url=i, callback=self.get_house_detail_info, meta={'zone': zone})

    def get_house_detail_info(self, zone, url):
        # anjuitems = []
        anjuitem = ServerItem()
        anjuitem["zone"] = zone
        anjuitem["url"] = url
        return anjuitem
