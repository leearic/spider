# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request


from spider.utils import orm
import time


from spider.items import newsItem


class ExampleSpider(scrapy.Spider):
    name = 't'
    allowed_domains = ['ifeng.com']
    start_urls = ['http://news.ifeng.com/listpage/11502/0/1/rtlist.shtml']

    def parse(self, response):
        aa = orm.News()
        news = aa.get_daily_news_url()
        for i in news:
            print i.url
            time.sleep(2)
            yield Request(url=i.url, callback=self.parse_news, meta={'response': response, 'news': i})

    def parse_news(self, response):
        aa = orm.News()
        item = newsItem()
        try:
            # news = response.meta['news']
            url = response.url
            title =  response.xpath('//div[@id="artical"]/h1[@id="artical_topic"]/text()').extract()[0]
            content = response.xpath('//div[@id="main_content"]').extract()[0]
            content_time =response.xpath('//*[@id="artical_sth"]/p/span[@itemprop="datePublished"]/text()').extract()[0]
            content_from = response.xpath('//*[@id="artical_sth"]/p/span[3]/span/a/text()').extract()[0]
            content_type = u'文字新闻'
            content_web = self.allowed_domains[0]
            save_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            content_html = response.body

            # item["news"] = news
            item["url"] = url
            item["title"] = title
            item["content"] = content
            item["content_time"] = content_time
            item["content_from"] = content_from
            item["content_type"] = content_type
            item["content_web"] = content_web
            item["save_time"] = save_time
            item["content_html"] = content_html


            aa.save_News(item)

            # print "*" * 10


        except:
            pass
