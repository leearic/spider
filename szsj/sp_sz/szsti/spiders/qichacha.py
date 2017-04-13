# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import DesiredCapabilities
from scrapy.selector import Selector
import time
from szsti.utils.Save2DB import DjORM
from szsti.utils.PageAnaylist import qichachca


class SzSpider(scrapy.Spider):
    name = "qichacha"
    allowed_domains = ["qichacha.com"]
    start_urls = ['http://www.qichacha.com/user_login']

    # 初始化，这里要调用无头浏览器
    def __init__(self):
        self.driver = webdriver.Chrome()
        # 定义Number值,如果中间爬取失败,可以设置继续爬取值重新爬取数据,默认从0开始
        # Number = 1849
        Number = 1870

        self.units = DjORM.query(Number)

    def parse(self, response):

        self.driver.get(response.url)

        # 打开登录页面，这里需要手动输入验证码: 默操作时间是20秒
        print response.url

        self.driver.find_element_by_name("nameNormal").send_keys("13771691089")
        self.driver.find_element_by_name("pwdNormal").send_keys("liang152191")
        print u"你有20秒钟时间获取验证码并点击登录按钮...."
        time.sleep(20)

        #　随便查询一个试试看
        self.driver.find_element_by_id("searchkey").send_keys(u"百度")
        self.driver.find_element_by_id("V3_Search_bt").click()
        time.sleep(2)
        # 正式查询开始

        for unit in self.units:
            print "==========================="
            print "current search number:" + str(unit.id)
            print "==========================="
            self.driver.find_element_by_id("headerKey").clear()
            self.driver.find_element_by_id("headerKey").send_keys(unit.Unit_name)
            self.driver.find_element_by_css_selector(".btn.btn-primary.top-searchbtn.btn-icon.btn-top").click()
            searching = self.driver.current_window_handle
            time.sleep(6)
            try:
                self.driver.find_element_by_class_name("ma_h1").click()
                time.sleep(6)
                tabs = self.driver.window_handles
                for tab in tabs:
                    if tab != searching:
                        self.driver.switch_to_window(tab)
                        aa = self.driver.page_source
                        response = Selector(text=aa)

                        qichachca.BaseInfo(response, unit.Unit_name)

                        qichachca.Unit_Base_Shareholder_Info(response, unit.Unit_name)

                        qichachca.Unit_Base_Changed_Info(response, unit.Unit_name)

                        # 点击页面 进行二次查询
                        # self.driver.find_element_by_xpath('//*[@id="company-nav"]/ul/li[5]/a').click()
                        # self.driver.current_window_handle
                        # aa = self.driver.page_source
                        # response = Selector(text=aa)
                        # qichachca.Unit_annual_reports_Base_Info(response, unit.number)
                    else:
                        self.driver.close()
                time.sleep(2)
            except Exception as e:
                print str(e)
                pass
        self.driver.quit()
