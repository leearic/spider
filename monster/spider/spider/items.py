# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class newsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    news         = scrapy.Field()
    url          = scrapy.Field()
    title        = scrapy.Field()
    content      = scrapy.Field()
    content_time = scrapy.Field()
    content_from = scrapy.Field()
    content_type = scrapy.Field()
    content_web  = scrapy.Field()
    save_time    = scrapy.Field()
    content_html = scrapy.Field()