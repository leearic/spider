# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from qiushibaike import items
class QiuBaiSpider(scrapy.Spider):
    name = "qiubai"
    allowed_domains = ["qiushibaike.com"]
    start_urls = (
        'http://www.qiushibaike.com/',
    )
    base_url = "http://www.qiushibaike.com"
    def parse(self, response):

        # 解析页面超级连接，到详细内容展示页面
        xiaohua_url = response.xpath('//div[@class="stats"]/span[@class="stats-comments"]/a/@href').extract()
        for i in xiaohua_url:
            url = self.base_url + i
            yield  Request(url, callback=self.get_per_xiaohua)
        # 获取下一页连接地址
        try:
            next_page = response.xpath('//div[@class="pageto"]/a[@class="next"]/@href').extract()
        except Exception, e:
            pass
        if len(next_page) == 0:
            pass
        else:
            next_page = self.base_url+next_page[0]
            yield  Request(next_page, callback=self.parse)

    def get_per_xiaohua(self, response):
        # 获取用户信息
        user_image = response.xpath('//div[@class="article block untagged noline mb15"]/div/a/img/@src').extract()
        user_name  = response.xpath('//div[@class="article block untagged noline mb15"]/div/a/text()').extract()

        # 获取笑话信息
        content = response.xpath('//div[@class="content"]/text()').extract()

        # 获取图片
        thumb   = response.xpath('//div[@class="thumb"]/img/@src').extract()

        # 获取Video
        video_image = response.xpath('//div[@class="video_holder"]/video/@poster').extract()
        video = response.xpath('//div[@class="video_holder"]/video/source/@src').extract()
        # 获取评论数量和好笑数量
        stats_vote = response.xpath('//div[@class="stats"]/span/i[@class="number"]/text()').extract()
        item = items.QiushibaikeItem()
        if len(thumb) == 0:
            thumb = "NN"
        if len(video) == 0:
            video = "NN"
        if len(user_name) == 0:
            user_name  = "NN"
        if len(user_image) == 0:
            user_image = "NN"
        if len(video_image) == 0:
            video_image = "NN"
        item["user_image"] = user_image
        item["user_name"]  = user_name[1].replace("\n"," ")
        item["content"] = content[0].replace("\n"," ")
        item["thumb"] = thumb
        item["video_image"] = video_image[0]
        item["video"] = video[0]
        item["laugh"] = stats_vote[0]
        item["coments"] = stats_vote[1]
        if item["video"] != "N":
                item["played"] = stats_vote[2]
        else:
                item["played"] = "0"
        # print item["video_image"]
        # print item["video"]
        yield item