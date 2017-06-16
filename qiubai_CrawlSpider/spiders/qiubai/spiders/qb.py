# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from qiubai import settings


from qiubai.items import User, QiuShiItem

class QbSpider(scrapy.Spider):
    name = "qb"
    allowed_domains = ["qiushibaike.com"]
    start_urls = (
        'http://www.qiushibaike.com/',
    )

    def parse(self, response):
        pass
        # 解析页面超级连接，到详细内容展示页面
        xiaohua_url = response.xpath('//div[@class="stats"]/span[@class="stats-comments"]/a/@href').extract()
        for i in xiaohua_url:
            url = settings.baseurl + i
            yield  Request(url, callback=self.get_per_xiaohua)
        # 获取下一页连接地址
        try:
            next_page = response.xpath('//div[@id="content-left"]/ul/li/a/@href').extract()
        except Exception, e:
            pass
        if len(next_page) == 0:
            pass
        else:
            for i in next_page:
                url1 = settings.baseurl + i
                yield  Request(url=url1, callback=self.parse)

    def get_per_xiaohua(self, response):
        # 获取用户信息
        user  = response.xpath('//div[@class="article block untagged noline mb15"]/div/a[2]/h2/text()').extract()
        # 获取笑话信息
        content = response.xpath('//div[@class="content"]/text()').extract()
        # 获取图片
        thumb   = response.xpath('//div[@class="thumb"]/img/@src').extract()
        # 获取Video
        video = response.xpath('//div[@class="video_holder"]/video/source/@src').extract()
        video_image = response.xpath('//div[@class="video_holder"]/video/@poster').extract()

        if len(thumb) != 0:
            type = ['1']
        if len(video_image) != 0:
            type = ['2']

        if len(thumb) == 0 and len(video_image) == 0:
            type = ['0']
            thumb = ['None']
            video = ['None']
            video_image = ['None']
        if len(video_image) == 0:
            video = ['None']
            video_image = ['None']

        smiling = response.xpath('//div[@class="stats"]/span[@class="stats-vote"]/i/text()').extract()
        comment_count = response.xpath('//div[@class="stats"]/span[@class="stats-comments"]/i/text()').extract()

        # 采集评论信息, 通过评论信息,采集用户信息
        cuser = response.xpath('//div[@class="comments-wrap"]/div/div/div/div[@class="replay"]/a/text()').extract()
        urls  = response.xpath('//div[@class="comments-wrap"]/div/div/div/div[@class="replay"]/a/@href').extract()
        ccomment = response.xpath('//div[@class="comments-wrap"]/div/div/div/div[@class="replay"]/span/text()').extract()

        for i in urls:
            url2 = settings.baseurl + i
            yield  Request(url=url2, callback=self.Get_User_Info)

        try:
            qiushiItems = QiuShiItem()
            qiushiItems["page_url"] = response.url
            qiushiItems["user"] = user[0]
            qiushiItems["content"] = content[0]
            qiushiItems["type"] = type[0]
            if type[0] == 1:
                qiushiItems["url"] = thumb[0]
            if type[0] == 2:
                qiushiItems["url"] = video_image[0]
                qiushiItems["url0"] = video[0]
            if type[0] == 0:
                qiushiItems["url"] = 'Null'
                qiushiItems["url0"] = 'Null'
            qiushiItems["smiling"] = smiling[0]
            qiushiItems["comment_count"] = comment_count[0]

            qiushiItems["cuser"] = cuser
            qiushiItems["comment"] = ccomment

            yield qiushiItems
        except:
            pass



    def Get_User_Info(self, response):
        user = response.xpath('//div[@class="user-header-cover"]/h2/text()').extract()
        fans = response.xpath('//div[@class="user-statis user-block"][1]/ul/li[1]/text()').extract()
        follow = response.xpath('//div[@class="user-statis user-block"][1]/ul/li[2]/text()').extract()
        comment = response.xpath('//div[@class="user-statis user-block"][1]/ul/li[3]/text()').extract()
        marriage = response.xpath('//div[@class="user-statis user-block"][2]/ul/li[1]/text()').extract()
        constellation = response.xpath('//div[@class="user-statis user-block"][2]/ul/li[2]/text()').extract()
        occupation = response.xpath('//div[@class="user-statis user-block"][2]/ul/li[3]/text()').extract()
        age = response.xpath('//div[@class="user-statis user-block"][2]/ul/li[5]/text()').extract()


        if len(marriage) == 0:
            marriage = ['Security']
        if len(occupation) == 0:
            occupation = ['Security']
        if len(constellation) == 0:
            constellation = ['Security']
        try:
            useritem = User()
            useritem["name"] = user[0]
            useritem["fans"] = fans[0]
            useritem["follow"] = follow[0]
            useritem["comment"] = comment[0]
            useritem["marriage"] = marriage[0]
            useritem["constellation"] = constellation[0]
            useritem["occupation"] = occupation[0]
            useritem["age"] = age[0]
            # print "-----已经将数据放到Item啦------"
            yield useritem
        except Exception, e:
            pass