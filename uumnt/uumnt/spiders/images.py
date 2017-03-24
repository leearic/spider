# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from uumnt import items

class ExampleSpider(scrapy.Spider):
    name = "imgs"
    allowed_domains = ["uumnt.com"]
    start_urls = (
        'http://www.uumnt.com/',
    )

    Base_URL = 'http://www.uumnt.com'

    def parse(self, response):
        # 获取栏目连接
        base_tab = response.xpath('//div[@class="tags_list"]/dl/dt/a/@href').extract()
        for i in base_tab:
            url = self.Base_URL+i
            try:
                yield Request(url, callback=self.image_tabs)
            except Exception as e:
                print e

    def image_tabs(self, response):
        #获取栏目列表里的图片链接
        urls = response.xpath('//div[@class="wf-main"]/div/a/@href').extract()
        for i in urls:
            yield Request(i, callback=self.get_image_url)

        #获取翻页链接
        pages = response.xpath('//div[@class="page"]/ul/li/a/@href').extract()
        for i in pages:
            url = self.Base_URL+i
            try:
                yield Request(url, callback=self.image_tabs)
            except Exception, e:
                print e

    def get_image_url(self, response):
        mysplite =   response.url.split('/')
        base_fenye_url = response.url.split(mysplite[len(mysplite)-1])
        base_fenye_url = base_fenye_url[0]

        # 获取图片页面的翻页图片链接
        urls = response.xpath('//div[@id="fenye"]/li/a/@href').extract()
        for i in urls:
            real_image_page_url = base_fenye_url+i
            yield  Request(real_image_page_url, callback=self.get_image_url)

        # 获取图片真实地址
        Base_image_url = "http://img.uumnt.com"
        image_url = response.xpath('//div[@class="bbox"]/a/img/@src').extract()
        image_title = response.xpath('//div[@class="bbt"]/h2/strong/a/text()').extract()

        if Base_image_url not in image_url[0]:
            image_url[0] = Base_image_url+image_url[0]
        item = items.ImagesItem()
        item["image_url"] = image_url
        item["image_title"] = image_title

        yield  item