# -*- coding: utf-8 -*-
__author__ = 'aric'
import sys, os
import hashlib

from cosplay.settings import DJpath


if DJpath not in sys.path:
    sys.path.append(DJpath)

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mikufan.settings")
django.setup()


from webapps.models import Coser, Images,  Category
class CoserORM(object):
    def Save_Coser_Info(self, item):
        DJcoser = Coser()
        cate  = Category()
        try:
            DJcoser.title = item["title"]
            DJcoser.content = item["content"]
            DJcoser.come_from   = item["url"]
            DJcoser.topimage = item["image"][0]

            # category = models.ForeignKey(DJcoser_Category, related_name=u"DJcoser_Category")
            DJcoser.save()

            dir_guid = hashlib.sha1(item["url"].encode('utf8')).hexdigest()

            for image in item["image"]:
                image_guid = hashlib.sha1(image.encode('utf8')).hexdigest()
                i = Images()
                i.real_url = image
                i.relate_url = '/images/%s/%s.jpg' % (dir_guid, image_guid)
                i.coser = DJcoser
                i.save()

            cate.category = '游戏'
            cate.coser = DJcoser
            cate.save()


            print("ok" * 10)
        except Exception as e:
            print("=error=l"*15)
            print(e)

