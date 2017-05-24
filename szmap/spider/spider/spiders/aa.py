# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


#  Get Django Env
import sys, os
djpath  = "/home/aric/PycharmProjects/aaa/szmap"
if djpath not in sys.path:
    sys.path.append(djpath)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "szmap.settings")
django.setup()

# from Django get models

from webapp.models import szmap

import time

class AaSpider(scrapy.Spider):
    name = "aa"
    allowed_domains = ["sutpc.com"]
    start_urls = ['http://szmap.sutpc.com/sectcongmore.aspx']

    def parse(self, response):
        # print response.body
        table = response.xpath('//*[@id="zyweb"]/div[2]/div[2]/div/table/tr')

        for i in table:
            szmap_data = szmap()
            zone   = i.xpath('td[1]/text()').extract()[0]
            zhishu = i.xpath('td[2]/text()').extract()[0]
            chesu  = i.xpath('td[3]/text()').extract()[0]
            try:
                dengji = i.xpath('td[4]/span/text()').extract()[0]
            except:
                dengji = u"等级"
                # pass
            print "*" * 30
            szmap_data.zone   =  zone.strip()
            szmap_data.zhishu = zhishu.strip()
            szmap_data.chesu = chesu.strip()
            szmap_data.dengji =  dengji.strip()
            os.environ['TZ'] = 'Asia/Shanghai'
            time.tzset()
            szmap_data.addtime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
            if szmap_data.dengji == u'等级':
                pass
            else:
                szmap_data.save()

            print u"区域: " + szmap_data.zone
            print u"区域: " + szmap_data.zhishu
            print u"区域: " + szmap_data.chesu
            print u"区域: " + szmap_data.dengji

            print "Save.....OK"


        for i in range(2,4):
            # print i
            yield  Request(url='http://szmap.sutpc.com/sectcongmore.aspx?page='+str(i), callback=self.parse)


        pass
