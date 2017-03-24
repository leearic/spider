# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from scrapy.selector import Selector
import time
from szsti.utils.Save2DB import DjORM

class SzSpider(scrapy.Spider):
    name = "unit"
    allowed_domains = ["szsti.gov.cn"]
    start_urls = ['http://www.szsti.gov.cn/services/hightech/']

    # #
    # allowed_domains = ["*"]
    # start_urls = ['http://172.16.201.249']

    # 初始化，这里要调用无头浏览器
    def __init__(self):

        # capabilities = DesiredCapabilities.PHANTOMJS.copy()
        # capabilities['phantomjs.page.settings.userAgent'] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0"
        # capabilities = DesiredCapabilities.FIREFOX.copy()
        # # capabilities['general.useragent.override'] = user_agent_string
        self.driver = webdriver.Remote(command_executor='http://172.16.201.250:8080/wd/hub',
                                       desired_capabilities = {
                                                'browserName': "Firefox",
                                                'takeScreenshot': False,
                                                "version": "5.1",
                                                "platform": "Linux",
                                                "javascriptEnabled": True,
                                                # "marionette": False,

                                                'phantomjs.page.settings.userAgent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0",
                                            },
                                          )

    def parse(self, response):
        print response.url
        # pass
        self.driver.get(response.url)
        time.sleep(2)
        item = {}
        index = 371
        self.driver.find_element_by_id("PagerControl_input").clear()
        self.driver.find_element_by_id("PagerControl_input").send_keys('371')
        self.driver.find_element_by_id("PagerControl_btn").click()
        self.driver.current_window_handle

        try:
            while(self.driver.find_element_by_link_text(u"下一页")):

                self.driver.current_window_handle
                aa = self.driver.page_source
                response = Selector(text=aa)
                tbody = response.xpath('//table[@id="data_list_container"]/tbody/tr')



                for body in tbody:
                    try:
                        number = body.xpath('td[1]/text()').extract()[0].strip()
                        KeyID =  body.xpath('td[2]/text()').extract()[0].strip()
                        Unit_name =  body.xpath('td[3]/text()').extract()[0].strip()
                        address =  body.xpath('td[4]/text()').extract()[0].strip()
                        Subordinate_Domain =  body.xpath('td[5]/text()').extract()[0].strip()
                        type = body.xpath('td[6]/text()').extract()[0].strip()
                        item["number"]              = number
                        item["KeyID"]               = KeyID
                        item["Unit_name"]           = Unit_name
                        item["address"]             = address
                        item["Subordinate_Domain"]  = Subordinate_Domain
                        item["type"]                = type
                        print item["Unit_name"]
                        # DjORM.save(item)
                        print  number + "   Saved ..... "
                    except Exception:
                        print "tbody Error. ignor .... "
                        pass
                        # print "     error   "
                self.driver.find_element_by_link_text(u"下一页").click()
                print "clicked next page ....   "
                index = index + 1
                print "current page: " + str(index)
                time.sleep(15)
            self.driver.close()
        except Exception as e:
            print "do while error ....  " + str(e)
            pass


        time.sleep(2)
        self.driver.quit()