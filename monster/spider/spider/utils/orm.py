# -*- coding: utf-8 -*-

import sys, os

from spider.settings import ormpath
if ormpath not in sys.path:
    sys.path.append(ormpath)

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm.settings")
django.setup()



import hashlib



from webapps.models import Day_News, Daily_News, News_Real_Content


class News(object):

    def _url_2_md5(self, url):

        m2 = hashlib.md5()
        m2.update(url)
        return m2.hexdigest()


    def save_Day_url(self, url):
        # 保存前一天的URL

        day = Day_News()
        day.url = url
        day.md5 = self._url_2_md5(url)
        day.save()


    def save_Daily_url(self, url):
        # 保存当天的所有URL
        daily = Daily_News()
        daily.url = url
        daily.md5  = self._url_2_md5(url)
        daily.save()


    def save_News(self, content):
        # 保存当条新闻
        inews = News_Real_Content()


        try:
        # news.news =  content['news']
            inews.url = content['url']
            inews.title = content['title']
            inews.content = content['content']
            inews.content_time = content['content_time']
            inews.content_from = content['content_from']
            inews.content_type = content['content_type']
            inews.content_web = content['content_web']
            inews.save_time = content['save_time']
            inews.content_html = content['content_html']

        # print inews.content_html
            inews.save()
        except Exception as e:
            print e







    def get_day_news_url(self):
        # 获取按天计算的URL
        news = Day_News.objects.all()
        return news

    def get_daily_news_url(self):
        # 获取按天计算的URL
        news = Daily_News.objects.all()
        return news



