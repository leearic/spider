# -*- coding: utf-8 -*-
import sys, os
from hr.settings import djpath
if djpath not in sys.path:
    sys.path.append(djpath)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hrweb.settings")
django.setup()

from lagou.models import Companys_Info, Position_Info, Position_URL


class lagou_DB(object):

    @classmethod
    def Search_ID(self, id):
        if id == 0:
            aa = Companys_Info.objects.all()
            # print "ID == 0"
        else:
            aa = Companys_Info.objects.filter(id__gte=id)
            print "ID != 0"
        return aa

    @classmethod
    def Search_Position_URL(self, id):
        if id == 0:
            aa = Position_URL.objects.all()
            # print "ID == 0"
        else:
            aa = Position_URL.objects.filter(id__gte=id)
            print "ID != 0"
        return aa




    @classmethod
    def Save_Position_Info(self, item):
        position_Info = Position_Info()
        # lagou 网站招聘信息
        position_Info.searching_company = item["searching_company"]
        position_Info.searched_company = item["searched_company"]
        position_Info.bumen = item["bumen"]
        position_Info.zhiwei = item["zhiwei"]

        position_Info.yaoqiu = item["yaoqiu"]
        position_Info.fabushijian = item["fabushijian"]
        position_Info.zhiweiyouhuo = item["zhiweiyouhuo"]
        position_Info.zhiweimiaoshu = item["zhiweimiaoshu"]
        position_Info.gongzuodidian = item["gongzuodidian"]
        position_Info.fabuzhe = item["fabuzhe"]

        position_Info.save()

    @classmethod
    def Save_Position_URL(self, item):
        position_URL = Position_URL()
        # lagou 网站招聘信息
        position_URL.searching_company = item["searching_company"]
        position_URL.url = item["url"]

        position_URL.save()