# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class QiuBaiSpider(scrapy.Spider):
    name = "qiushi"
    allowed_domains = ["qiushibaike.com"]
    start_urls = (
        'http://www.qiushibaike.com/',
    )
    base_url = "http://www.qiushibaike.com"
    def parse(self, response):
        # 获取用户信息
        user_image = response.xpath('//div[@class="article block untagged mb15"]/div/a/img/@src').extract()
        user_name  = response.xpath('//div[@class="article block untagged mb15"]/div/a/text()').extract()
        # 获取笑话信息
        content = response.xpath('//div[@class="content"]/text()').extract()
        # 获取图片
        thumb   = response.xpath('//div[@class="thumb"]/a/img/@src').extract()
        # 获取下一页连接地址
        try:
            next_page = response.xpath('//div[@class="pageto"]/a[@class="next"]/@href').extract()
        except Exception, e:
            pass
        if len(next_page) == 0:
            pass
        else:
            next_page = self.base_url+next_page[0]
            for i in content:
                print i.encode("gbk")
            yield  Request(next_page, callback=self.parse)