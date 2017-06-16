# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiuShiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 笑话相关
    page_url = scrapy.Field()      # 来源地址
    user     = scrapy.Field()      # 用户
    content  = scrapy.Field()      # 内容
    type     = scrapy.Field()      # 附带样式,比如图片或者视频 1 为图片, 2为视频, 0为只有文字
    url      = scrapy.Field()      # 图片地址(视频默认有封面)
    url0     = scrapy.Field()      # 如果是视频的话,这里就是视频地址
    smiling  = scrapy.Field()      # 笑脸数量
    comment_count  = scrapy.Field()# 评论数量
    # comment  = scrapy.Field()      # 评论

# class Comment(scrapy.Item):
    cuser    = scrapy.Field()       # 评论的用户
    comment = scrapy.Field()       # 评论的内容

class User(scrapy.Item):
    name            = scrapy.Field()            # 用户名
    fans            = scrapy.Field()            # 粉丝数量
    follow          = scrapy.Field()            # 关注数量
    comment         = scrapy.Field()            # 评论数量

    marriage        = scrapy.Field()            # 婚姻状态
    occupation      = scrapy.Field()            # 职业
    constellation   = scrapy.Field()            # 星座
    age             = scrapy.Field()            # 糗龄



