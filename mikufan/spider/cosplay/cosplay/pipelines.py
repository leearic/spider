# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
import hashlib

from cosplay.utils.DjangoORM import CoserORM

class AcgPipeline(ImagesPipeline):
    # 从item中获取图片的真实地址，并执行下载请求
    def get_media_requests(self, item, info):
        self.dirname = item["url"]
        for image_url in item['image']:
            # print("*" * 20)
            # print(image_url)
            # print("*"*20)
            yield  Request(image_url)


    def item_completed(self, results, item, info):
        image_paths = [[x['path'] for ok, x in results if ok]]
        if not image_paths:
            raise DropItem("Item contains no images")
        save_Data = CoserORM()
        save_Data.Save_Coser_Info(item)
        return
    def file_path(self, request, response=None, info=None):
        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('ImagesPipeline.image_key(url) and file_key(url) methods are deprecated, '
                          'please use file_path(request, response=None, info=None) instead',
                          category=ScrapyDeprecationWarning, stacklevel=1)
        if not isinstance(request, Request):
            _warn()
            url = request
        else:
            url = request.url
        if not hasattr(self.file_key, '_base'):
            _warn()
            return self.file_key(url)
        elif not hasattr(self.image_key, '_base'):
            _warn()
            return self.image_key(url)
        image_guid = hashlib.sha1(url.encode("utf8")).hexdigest()
        dir_guid   = hashlib.sha1(self.dirname.encode("utf8")).hexdigest()
        return '%s/%s.jpg' % (dir_guid, image_guid)