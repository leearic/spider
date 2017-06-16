# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Cos8Item(scrapy.Item):
    # define the fields for your item here like:
    html_base_url = scrapy.Field()
    img_base_url = scrapy.Field()
    img_content = scrapy.Field()

    
