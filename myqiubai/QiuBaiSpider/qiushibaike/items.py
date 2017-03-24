# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class QiushibaikeItem(scrapy.Item):
    user_image = scrapy.Field()
    user_name = scrapy.Field()
    content = scrapy.Field()
    thumb = scrapy.Field()
    video_image = scrapy.Field()
    video = scrapy.Field()
    laugh = scrapy.Field()
    coments = scrapy.Field()
    played = scrapy.Field()
