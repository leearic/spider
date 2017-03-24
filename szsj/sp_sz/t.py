# -*- coding: utf-8 -*-


# from selenium import webdriver
# from scrapy.selector import Selector
#
#
# import  time
#
#
#
#
#
# driver = webdriver.Chrome()
# driver.get("http://www.qichacha.com/firm_d38086e115661b46f68c31070231d0ab.shtml")
#
# aa =  driver.page_source
# response = Selector(text=aa)
#
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








aa = "http://wpa.qq.com/msgrd?v=3&uin=3352118161&site=qq&menu=yes"
i = aa.split("=")[2].split("&")[0]

print i















