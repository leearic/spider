# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from fang.ORM import save_to_db

class FangPipeline(object):
    def process_item(self, item, spider):

        anjuke = save_to_db.anjukeORM()
        anjuke.Save(item)

        return item


    def spider_closed(self, spider):
        pass