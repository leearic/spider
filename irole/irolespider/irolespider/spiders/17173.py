# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector 
from scrapy.http import Request
from irolespider import settings
from irolespider.items import Cos8Item

from irolespider.utils import Spider_Django


class MycosSpider(scrapy.Spider):
    name = "17173"
    # allowed_domains = ["cosplay8.com"]
    # start_urls = (
    #     'http://news.17173.com/gameview/cos/',
    # )
    urls = "http://news.17173.com/gameview/cos/"
    def start_requests(self):
        yield scrapy.Request(self.urls, callback=self.parse,
                             meta={"use_splash": True})

    def parse(self, response):
        sel = Selector(response)
        #获取图片详细页面
        img_page_url = sel.xpath('//div[@class="yxdy"]/ul/li/a/@href').extract()
        for i in img_page_url:
            # print i
            yield  Request(i, callback=self.Get_Imag_URL)
        # 获取图片list 页面
        page_url = sel.xpath('//div[@class="paginationdg"]/ul/li/a/@href').extract()
        for relative_url in page_url:
            page_real_url = response.url + relative_url
            # print page_real_url
            yield  Request(page_real_url, callback=self.parse)
    #  ----------------------------------------------------------------------

    def Get_Imag_URL(self, response):

        aa = Spider_Django.django_sql()
        if aa.is_crawled(response.url):
            """获取图片的真实地址"""

            sel = Selector(response)
            img_url = sel.xpath('//p[@align="center"]/a/img/@src').extract()
            context = sel.xpath('//h1[@class="gb-final-tit-article"]/text()').extract()
            items = []
            item = Cos8Item()
            for relative_img_url in img_url:
                img_real_url = relative_img_url
                item["img_base_url"] = [img_real_url]
                item["html_base_url"] = response.url

                print "====================="
                print img_real_url
                print response.url

            for aa in context:
                item["img_content"] = [aa]
                items.append(item)
            # return  items
        else:
            print response.url + " is crawled !"
            pass