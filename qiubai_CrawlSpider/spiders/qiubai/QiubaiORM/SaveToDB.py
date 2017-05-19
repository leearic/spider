# -*- coding:utf-8 -*-

import sys, os

from qiubai.settings import path
if path not in sys.path:
    sys.path.append(path)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qiubaifrontend.settings")
django.setup()
from spiders.models import QiuShi, User, Comment

class QiushiORM(object):
    def Saveqiushi(self, items):

        try:
            qiushi = QiuShi()
            commenta = Comment()
            qiushi.page_url = items["page_url"]
            qiushi.user     = items["user"]
            qiushi.contents  = items["content"]
            qiushi.type     = items["type"]
            qiushi.url      = items["url"]
            qiushi.url0     = items["url0"]
            qiushi.smiling = items["smiling"]
            qiushi.comment_count = items["comment_count"]

            # print "开始写入关键数据库"
            for i in range(0, len(items["cuser"])):
                commenta.user = items["cuser"][i]
                commenta.qiushiURL = items["page_url"]
                commenta.comment = items["comment"][i]
                commenta.save()
            qiushi.save()
        except:
            pass


    def SaveUser(self, items):
        try:
            user = User()
            user.name       = items['name']
            user.fans       = items['fans']
            user.follow     = items['follow']
            user.comment    = items['comment']
            user.marriage   = items['marriage']
            user.occupation = items['occupation']
            user.constellation = items['constellation']
            user.age        = items['age']
            user.save()
        except:
            pass



