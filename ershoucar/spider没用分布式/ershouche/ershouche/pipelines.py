# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from utils import DjangoORM
import hashlib

class ErshouchePipeline(ImagesPipeline):
    name = ''
    # 从item中获取图片的真实地址，并执行下载请求
    def get_media_requests(self, item, info):

        for image_url in (item['url0'], item['url1'], item['url2'], item['url3'], item['url4'], item['url5'], item['url6'], item['url7']):
            yield Request(image_url[0])
        self.name = item["url"][0]
    def item_completed(self, results, item, info):
        save_Data = DjangoORM.CarORM()
        save_Data.SaveCarInfo(item)
        return item

    def file_path(self, request, response=None, info=None):
        url = request.url
        image_guid = hashlib.sha1(url).hexdigest()  # change to request.url after deprecation
        name = hashlib.sha1(self.name).hexdigest()

        return '%s/%s.jpg' % (name, image_guid)