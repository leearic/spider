# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import DesiredCapabilities
from scrapy.selector import Selector
import time

from hr.utils.lagou.Save_2_DB import lagou_DB
from hr.utils.lagou.PageAnalysis import lagou_Analysis


class LgSpider(scrapy.Spider):
    name = "lgp"
    allowed_domains = ["lagou.com"]
    start_urls = ['http://www.lagou.com/']

    # 初始化，这里要调用无头浏览器
    def __init__(self):
        self.driver = webdriver.Chrome()
        # id,如果中间爬取失败,可以设置继续爬取值重新爬取数据,默认从0开始
        id = 2276
        self.units = lagou_DB.Search_Position_URL(id)

    def parse(self, response):
        # 从数据中拿取数据,组装 URL
        for unit in self.units:
            # 从数据库中拿取 URL
            print u"拉钩人才招聘网站 search id: " + str(unit.id)
            print "*" * 30

            self.driver.get(unit.url)


            self.driver.current_window_handle
            aa = self.driver.page_source
            response = Selector(text=aa)

            lagou_Analysis.Analysis_Position_Info(response, unit.searching_company)
            time.sleep(3)