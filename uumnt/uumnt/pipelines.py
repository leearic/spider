# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request

class ImagesPipeline(ImagesPipeline):

    title = ""
    def get_media_requests(self, item, info):

        for user_image in item["image_url"]:
            yield Request(user_image)
            self.title = item["image_title"]

    def item_completed(self, results, item, info):
        image_paths = [[x['path'] for ok, x in results if ok]]
        if not image_paths:
            raise DropItem("Item contains no images")
        return

    # 修改保存图片的文件名...
    #----------------------------------------------------------------------
    def file_path(self, request, response=None, info=None):
        url = request.url
        image_guid = url.split('/')[-1]
        ttle = self.title[0].encode('gbk').split('(')[0]
        return '%s/%s.jpg' % (ttle, image_guid)
    #----------------------------------------------------------------------