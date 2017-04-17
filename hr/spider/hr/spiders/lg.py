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
    name = "lg"
    allowed_domains = ["lagou.com"]
    start_urls = ['http://www.lagou.com/']

    # 初始化，这里要调用无头浏览器
    def __init__(self):
        self.driver = webdriver.Chrome()
        # id,如果中间爬取失败,可以设置继续爬取值重新爬取数据,默认从0开始
        id = 0
        self.units = lagou_DB.Search_ID(id)
        self.item = {}

    def parse(self, response):

        # 打开网站
        self.driver.get(response.url)

        print u"你有5秒钟来选择地区, 推荐地区-全国"
        time.sleep(5)



        self.driver.find_element_by_class_name("search_input").clear()
        time.sleep(2)
        self.driver.find_element_by_class_name("search_input").send_keys(u'百度')
        time.sleep(2)
        self.driver.find_element_by_id("search_button").click()

        time.sleep(2)
        # 从数据中拿取数据,组装 URL
        for unit in self.units:
            print u"拉钩人才招聘网站 search id: " + str(unit.id)
            print "*" * 30

            self.driver.current_window_handle

            self.driver.find_element_by_id('keyword').clear()
            self.driver.find_element_by_id('keyword').send_keys(unit.searching_company)
            self.driver.find_element_by_id('submit').click()
            time.sleep(2)
            self.driver.find_element_by_id('tab_pos').click()
            time.sleep(2)

            self.driver.current_window_handle

            aa = self.driver.page_source
            response = Selector(text=aa)

            try:
                # 如果有相关工作岗位, 立即保存起来
                self.get_postion_url(response, unit.searching_company)

                # 如果有第二页相关工作岗位,立即点击第二页,然后继续保存下来
                try:
                    self.driver.find_element_by_css_selector('#s_position_list>div.item_con_pager>div>span.pager_next.pager_next_disabled')
                    self.aa = False
                except:
                    self.aa = True


                while self.aa:

                    self.driver.find_element_by_class_name('pager_next').click()
                    time.sleep(2)

                    self.driver.current_window_handle
                    aa = self.driver.page_source
                    response = Selector(text=aa)
                    self.get_postion_url(response, unit.searching_company)
                    try:
                        self.driver.find_element_by_css_selector('#s_position_list>div.item_con_pager>div>span.pager_next.pager_next_disabled')
                        self.aa = False
                    except:
                        self.aa = True

            except:
                print "error occours ... No such postion"

            # lagou_Analysis.Analysis_Position_Info(response, unit.searching_company)



    def get_postion_url(self, response, searching_company):

        postion_table = response.xpath('//*[@id="s_position_list"]/ul/li')
        for postion in postion_table:
            self.item["url"] =  postion.xpath('div/div/div/a[@class="position_link"]/@href').extract()[0]
            self.item["searching_company"] = searching_company
            lagou_DB.Save_Position_URL(self.item)

        print searching_company + u"： 职位保存完毕"

