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
    name = "gao"
    allowed_domains = ["qichacha.com"]
    start_urls = ['http://www.qichacha.com/user_login']

    # 初始化，这里要调用无头浏览器
    def __init__(self):
        self.driver = webdriver.Chrome()
        # 定义Number值,如果中间爬取失败,可以设置继续爬取值重新爬取数据,默认从0开始
        # Number = 2053
        # self.units = DjORM.query_itjuzi(Number)

        self.units = [u"洗衣机", u"玻璃瓶", u"玻璃容器", u"化妆品瓶", u"玻璃瓶涂装"]


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

            self.driver.find_element_by_id("headerKey").clear()
            self.driver.find_element_by_id("headerKey").send_keys(unit)
            self.driver.find_element_by_css_selector(".btn.btn-primary.top-searchbtn.btn-icon.btn-top").click()
            index = 1
            time.sleep(3)
            try:
                while self.driver.find_element_by_link_text(">"):
                    print "================"
                    print "current index: " + str(index)
                    print "current search category: " + unit
                    print "================"
                    try:
                        self.driver.current_window_handle
                        aa = self.driver.page_source
                        response = Selector(text=aa)
                        qichachca.Miss_Gao_Info(response, unit)

                        index = index + 1

                        self.driver.find_element_by_xpath('//*[@id="ajaxlist"]/div[3]/ul/li[8]/input').clear()
                        self.driver.find_element_by_xpath('//*[@id="ajaxlist"]/div[3]/ul/li[8]/input').send_keys(index)

                    except:

                        try:
                            self.driver.find_element_by_xpath('//*[@id="ajaxlist"]/div[3]/ul/li[10]/input').clear()
                            self.driver.find_element_by_xpath('//*[@id="ajaxlist"]/div[3]/ul/li[10]/input').send_keys(index)
                        except:
                            self.driver.find_element_by_xpath('//*[@id="ajaxlist"]/div[3]/ul/li[9]/input').clear()
                            self.driver.find_element_by_xpath('//*[@id="ajaxlist"]/div[3]/ul/li[9]/input').send_keys(index)


                    self.driver.find_element_by_id("jumpPage").click()
                    print "next page clicked ...."
                    time.sleep(3)
            except:
                pass
        self.driver.quit()
