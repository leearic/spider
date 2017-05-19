# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import DesiredCapabilities
from scrapy.selector import Selector
import time
from szsti.hexunutils.Save_2_DB import Hexun
from szsti.hexunutils.PageAnalysis import hexun_Analysis



class SzSpider(scrapy.Spider):
    name = "hx_srfb"
    # allowed_domains = ["hexun--delete.com"]
    # start_urls = ['http://stockdata.stock.hexun.com/gszl/ggml-000001.shtml']

    allowed_domains = ["hexun.com"]
    start_urls = ['http://www.hexun.com/']


    # 初始化，这里要调用无头浏览器
    def __init__(self):
        self.driver = webdriver.Chrome()
        # id,如果中间爬取失败,可以设置继续爬取值重新爬取数据,默认从0开始
        id = 1826
        self.units = Hexun.Search_ID(id)
        self.Base_Request_Url = 'http://stockdata.stock.hexun.com/gszl/srfb-'

    def parse(self, response):

        # 从数据中拿取数据,组装 URL
        for unit in self.units:
            self.Request_url = self.Base_Request_Url + str(unit.Code) + '.shtml'

            print u"收入分布 search Code: " + unit.Code
            print "*" * 30

            time.sleep(3)
            # 调用模拟器取访问组装好的URL
            self.driver.get(self.Request_url)
            time.sleep(3)
            self.driver.current_window_handle
            aa = self.driver.page_source
            response = Selector(text=aa)

            hexun_Analysis.Showrufenbu_Info(response, str(unit.Code))


