# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request


from spider.utils import orm

class ExampleSpider(scrapy.Spider):
    name = 'f'
    allowed_domains = ['ifeng.com']
    start_urls = ['http://news.ifeng.com/listpage/11502/0/1/rtlist.shtml']


    def parse(self, response):

        current_day_news =  response.url
        aa = orm.News()

        aa.save_Day_url(current_day_news)
        last_day_news = response.xpath('//*[@id="backDay"]/a/@href').extract()[0]



        yield  Request(url=last_day_news, callback=self.parse)



    #
    # def parse_lastday(self, response):
    #
    #
    #     news_lists = response.xpath('//div[@class="newsList"]/ul')
    #
    #     for i in news_lists:
    #         news_list = i.xpath('li/a/@href').extract()
    #         for news in news_list:
    #             print u'新闻地址: ' + news
    #             yield Request(url=news, callback=self.parse_content)
    #
    #     try:
    #         next_page = response.xpath('//div[@class="m_page"]/span[2]/a/@href').extract()[0]
    #     except:
    #         next_page = response.xpath('//div[@class="m_page"]/span/a/@href').extract()[0]
    #
    #
    #     yield Request(url=next_page, callback=self.parse_lastday)
    #
    #
    # def parse_content(self, responese):