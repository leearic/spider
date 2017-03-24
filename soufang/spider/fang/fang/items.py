# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 区域
    zone =   scrapy.Field()
    # 网址
    url = scrapy.Field()
    # 商品图片
    image =  scrapy.Field()
    # 售价
    saleprice =  scrapy.Field()
    # 首付
    shoufu =  scrapy.Field()
    # 月供 *
    monthpay =  scrapy.Field()
    # 单价
    unit_price =  scrapy.Field()
    # 所在小区 *
    quarters =  scrapy.Field()
    # 位置 *
    position =  scrapy.Field()
    # 房型
    apartment =  scrapy.Field()
    # 面积
    area =  scrapy.Field()
    # 朝向
    orientation =  scrapy.Field()
    # 楼层
    floor =  scrapy.Field()
    # 装修
    renovation =  scrapy.Field()
    # 类型 *
    type =  scrapy.Field()
    # 商品详细情况
    details =  scrapy.Field()

