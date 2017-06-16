# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from fang.utils.InsertToRedis import RedisSever
from fang import settings

class FangPipeline(object):
    def process_item(self, item, spider):
        url = item['zone'] + ',' + item['url']
        r = RedisSever(settings.REDIS_HOST, settings.REDIS_PORT)
        r.push(url)
        return item
    def spider_closed(self, spider):
        pass