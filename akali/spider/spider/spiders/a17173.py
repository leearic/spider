# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

import syslog

import logging

from scrapy.mail import MailSender

# from . import settings


from spider import settings

syslog.openlog(ident="spider", logoption=syslog.LOG_PID, facility=syslog.LOG_LOCAL7)

logger = logging.getLogger("spiders")



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

                logger.error(u"开始爬详细页面信息")
                # try:
                #     # mailer = MailSender(smtphost="172.16.201.200", mailfrom="aric@easymon.com", smtpuser="aric",
                #     #                     smtppass="123456", smtpport=25)
                #
                #     # mailer.send(to="aric@easymon.com", subject="helloworld", body="hello body")
                # except Exception as e:
                #     print e
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

                syslog.syslog(syslog.LOG_INFO, i)
                syslog.syslog(syslog.LOG_ERR, i)

        except:
            pass

        # items = AcgItem()
        # items["name"] = title
        # items["url"]  = response.url
        # items["image"] = item

        # return items




