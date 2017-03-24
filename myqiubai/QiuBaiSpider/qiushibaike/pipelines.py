# -*- coding: utf-8 -*-

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
from qiushibaike import settings
from qiushibaike.utils import SQL
import  MySQLdb

class QiushibaikePipeline(ImagesPipeline):
    sql = SQL.SQL_Conn()
    def get_media_requests(self, item, info):

        for user_image in item["user_image"]:
            if user_image != "N":
                #print u"开始下载图片咯，用户头像:"+ user_image
                yield  Request(user_image)
        for thumb in item["thumb"]:
            if thumb != "N":
                #print u"开始下载图片咯，图片文件:"+ thumb
                yield  Request(thumb)
    def item_completed(self, results, item, info):
        image_paths = [[x['path'] for ok, x in results if ok]]
        if not image_paths:
            raise DropItem("Item contains no images")
        self.sql.save(item)
        return