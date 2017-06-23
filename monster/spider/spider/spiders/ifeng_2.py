# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request


from spider.utils import orm


import time
class ExampleSpider(scrapy.Spider):
    name = 's'
    allowed_domains = ['ifeng.com']
    start_urls = ['http://news.ifeng.com/listpage/11502/0/1/rtlist.shtml']

    def parse(self, response):
        aa = orm.News()
        news = aa.get_day_news_url()
        for i in news:
            print i.url
            time.sleep(2)
            yield Request(url=i.url, callback=self.parse_news_url, meta={'response': response})

    def parse_news_url(self, response):
        aa = orm.News()

        news_lists = response.xpath('//div[@class="newsList"]/ul')
        for i in news_lists:
            news_list = i.xpath('li/a/@href').extract()
            for news in news_list:
                print u'新闻地址: ' + news
                aa.save_Daily_url(news)
        try:
            next_page = response.xpath('//div[@class="m_page"]/span[2]/a/@href').extract()[0]
        except:
            next_page = response.xpath('//div[@class="m_page"]/span/a/@href').extract()[0]

        yield Request(url=next_page, callback=self.parse_news_url)


