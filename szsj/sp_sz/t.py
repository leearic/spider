# -*- coding: utf-8 -*-
#! /usr/bin/env python




from selenium import webdriver
from scrapy.selector import Selector


import  time





driver = webdriver.Firefox()
driver.get("http://www.qichacha.com/firm_d38086e115661b46f68c31070231d0ab.shtml")

aa =  driver.page_source

print aa

driver.close()



# response = Selector(text=aa)
# #
#
#
# tbody = response.xpath('//*[@id="Changelist"]/table/tbody/tr')
#
#
# for i in tbody:
#     # print i.extract()
#     try:
#         print i.xpath('td[1]/text()').extract()[0]
#         print i.xpath('td[2]/text()').extract()[0].strip()
#         print i.xpath('td[3]/text()').extract()[0].strip()
#         print i.xpath('td[4]/div/text()').extract()[0].strip()
#         print i.xpath('td[5]/div/text()').extract()[0].strip()
#     except Exception:
#         print "error"
#         pass
#
#     print "*" * 30
#
#












