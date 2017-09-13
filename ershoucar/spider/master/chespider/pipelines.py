# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from chespider.utils import MyRedis

from . import settings

from utils.SysLog import SpiderLog


class ChespiderPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    def process_item(self, item, spider):
        myredis = MyRedis.Redis_MQ()
        SpiderLog.log(settings.BOT_NAME, item)

        print

        # myredis.set('DetailURL', item['DetailURL'])
        # print item['DetailURL']
    #
    # def item_completed(self, results, item, info):
    #     """Called per item when all media requests has been processed"""
    #     print  item['DetailURL']
    #     return item