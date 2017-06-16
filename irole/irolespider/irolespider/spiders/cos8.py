# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector 
from scrapy.http import Request
from irolespider import settings
from irolespider.items import Cos8Item

from irolespider.utils import Spider_Django


class MycosSpider(scrapy.Spider):
    name = "mycos"
    allowed_domains = ["cosplay8.com"]
    start_urls = (
        'http://www.cosplay8.com/pic/chinacos/',
        'http://www.cosplay8.com/pic/worldcos/',
        'http://www.cosplay8.com/pic/cospic/', 
    )
    def parse(self, response):
        sel = Selector(response)
        #获取图片详细页面
        img_page_url = sel.xpath('//div[@class="pagew center hauto pic_list"]/ul/li/a/@href').extract()
        for i in img_page_url:
            img_page_real_url = settings.base_url + i
            yield  Request(img_page_real_url, callback=self.Get_Imag_URL)
        # 获取图片list 页面
        page_url = sel.xpath('//div[@class="pagebox center mbottom yahei"]/a/@href').extract()
        for relative_url in page_url:
            page_real_url = response.url + relative_url
            yield  Request(page_real_url, callback=self.parse)
    # ----------------------------------------------------------------------
    def Get_Imag_URL(self, response):

        aa = Spider_Django.django_sql()
        if aa.is_crawled(response.url):
            """获取图片的真实地址"""

            sel = Selector(response)
            img_url = sel.xpath('//img[@id="bigimg"]/@src').extract()
            context = sel.xpath('//div[@class="p_box hauto tcenter"]/h1/text()').extract()
            items = []
            item = Cos8Item()
            for relative_img_url in img_url:
                img_real_url = settings.base_url + relative_img_url
                item["img_base_url"] = [img_real_url]
                item["html_base_url"] = response.url
            for aa in context:
                item["img_content"] = [aa]
                items.append(item)
            return  items
        else:
            print response.url + " is crawled !"
            pass