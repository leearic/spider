# -*- coding: utf-8 -*-

# from scrapy.contrib.pipeline.images import ImagesPipeline
# from scrapy.http import Request
# from scrapy.exceptions import DropItem
from qiubai.QiubaiORM import SaveToDB



class QiuShiPipeline(object):


    def process_item(self, item, spider):
        if 'type' not in item:
            return item
        else:
            qiushi = SaveToDB.QiushiORM()
            qiushi.Saveqiushi(item)
        # self.content.insert(dict(item))
        return item

    def spider_closed(self, spider):
        pass



class UserPipeline(object):
    def process_item(self, item, spider):
        if 'follow' not in item:
            return item
        else:
            qiushi = SaveToDB.QiushiORM()
            qiushi.SaveUser(item)

        # self.content.insert(dict(item))
        return item

    def spider_closed(self, spider):
        pass

