# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
from utils import  Spider_Django


class Cos8Pipeline(ImagesPipeline):
    # 从item中获取图片的真实地址，并执行下载请求
    def get_media_requests(self, item, info):
        for image_url in item['img_base_url']:
            yield  Request(image_url)
# ----------------------------------------------------------------------
    def item_completed(self, results, item, info):
        image_paths = [[x['path'] for ok, x in results if ok]]
        if not image_paths:
            raise DropItem("Item contains no images")
        save_Data = Spider_Django.django_sql()
        save_Data.save_Item(item)
        return
    # 修改保存图片的文件名...
    # ----------------------------------------------------------------------
    def file_path(self, request, response=None, info=None):
        
        url = request.url
        image_guid = url.split('/')[-1]
        return '%s.jpg' % (image_guid)