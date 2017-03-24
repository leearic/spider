# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import time

from baic.utils.RandomProxy import RadomProxyWebdriver
from baic.items import BaicRecordItem


class BJSpider(scrapy.Spider):
    # 北京
    name = "bjdetail"
    allowed_domains = ["gov.cn"]
    start_urls = (
        'http://qyxy.baic.gov.cn/dito/ditoAction!ycmlFrame.dhtml?clear=true',
    )
    # 初始化，这里要调用无头浏览器
    def __init__(self):

        self.driver   = RadomProxyWebdriver.getdriver()
        self.pageinfo = RadomProxyWebdriver.getdriver()

    def parse(self, response):
        # 1.获取网页源码，分析列表，获取列表长度
        urls = response.url
        self.driver.get(urls)
        time.sleep(2)
        aa = self.driver.page_source
        response = Selector(text=aa)

        try:
            next_page = response.xpath('/html/body/div/div/div[3]/div[1]/form/table/tbody/tr[12]/th/a[6]')
            if len(next_page) == 0:
                next_page = response.xpath('/html/body/div/div/div[3]/div[1]/form/table/tbody/tr[12]/th/a[10]')
        except Exception, e:
            print e
        # 这里添加一个计数器
        page_index = 0

        while next_page:
            # 如果页面是第一次加载，那就什么也不做
            if page_index == 0:
                pass
            else:
                self.driver.get(urls)
                self.driver.current_window_handle
                time.sleep(2)
            # 如果不是第一次加载，说明前面已经打开过了，这里按计数器的多少，点击下一页.
                for i in xrange(page_index):
                    try:
                        self.driver.find_element_by_link_text(">>").click()
                        self.driver.current_window_handle
                    except Exception as e:
                        print e
                    time.sleep(2)

            aa = self.driver.page_source
            response = Selector(text=aa)
            # 进入页面，找到link，获取list列表
            links = response.xpath('/html/body/div/div/div[3]/div[1]/form/table/tbody/tr').extract()

            # 获取到列表长度之后，可以根据长度来产生Xpath
            for i in range(2, len(links)):
                # 根据列表，获取各个公司的URL
                xpath = '/html/body/div/div/div[3]/div[1]/form/table/tbody/tr['+ str(i) +']/td[1]/a'
                self.driver.find_element_by_xpath(xpath).click()
                # time.sleep(2)
                self.driver.current_window_handle

                # 获取到不同的公司详情URL，接下来就可以分析网页源码，做数据提取，然后入库
                url = self.driver.current_url
                yield self.select_page_info(url)
                # 这里要回退，不然报错
                self.driver.back()
            try:
                next_page = response.xpath('/html/body/div/div/div[3]/div[1]/form/table/tbody/tr[12]/th/a[6]')
                if len(next_page) == 0:
                    next_page = response.xpath('/html/body/div/div/div[3]/div[1]/form/table/tbody/tr[12]/th/a[10]')
            except Exception as e:
                print e
            # time.sleep(2)
            page_index += 1

        self.driver.close()
        self.pageinfo.close()


    def select_page_info(self, pageinfo_url):
        # 获取到网页的URL，打开新链接， 获取网页源码
        self.pageinfo.get(pageinfo_url)
        time.sleep(15)
        self.pageinfo.current_window_handle
        page_info = self.pageinfo.page_source.encode('utf8')
        response = Selector(text=page_info)
        # 找到了网页源码，开始解析网页，获取需要的item.
        # 登记信息
        url = self.pageinfo.current_url
        city = u'北京'
        register_ID = response.xpath(
            '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[2]/td[1]/text()').extract()
        register_name = response.xpath(
            '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/text()').extract()
        type = response.xpath('/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[3]/td[1]/text()').extract()

        representative = response.xpath(
            '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/text()').extract()
        capital = response.xpath(
            '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[4]/td[1]/text()').extract()
        establishment = response.xpath(
            '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[4]/td[2]/text()').extract()
        lodgment = response.xpath(
            '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[5]/td/text()').extract()
        Operating_start = response.xpath(
            '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[6]/td[1]/text()').extract()
        Operating_end = response.xpath(
            '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[6]/td[2]/text()').extract()
        Business_scope = response.xpath(
            '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[7]/td/text()').extract()
        reg_authority = response.xpath(
            '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[8]/td[1]/text()').extract()
        Approved_date = response.xpath(
            '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[8]/td[2]/text()').extract()
        status = response.xpath(
            '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[9]/td[1]/text()').extract()

        if len(establishment) == 0:
            capital = ['nil']
            lodgment = response.xpath('/html/body/div[2]/div[2]/div/div[2]/table[1]/tbody/tr[4]/td/text()').extract()
            Operating_start = response.xpath(
                '/html/body/div[2]/div[2]/div/div[2]/table[1]/tbody/tr[5]/td[1]/text()').extract()
            Operating_end = response.xpath(
                '/html/body/div[2]/div[2]/div/div[2]/table[1]/tbody/tr[5]/td[2]/text()').extract()
            Business_scope = response.xpath(
                '/html/body/div[2]/div[2]/div/div[2]/table[1]/tbody/tr[6]/td/text()').extract()
            reg_authority = response.xpath(
                '/html/body/div[2]/div[2]/div/div[2]/table[1]/tbody/tr[7]/td[1]/text()').extract()
            Approved_date = response.xpath(
                '/html/body/div[2]/div[2]/div/div[2]/table[1]/tbody/tr[7]/td[2]/text()').extract()
            status = response.xpath('/html/body/div[2]/div[2]/div/div[2]/table[1]/tbody/tr[8]/td[2]/text()').extract()
            establishment = response.xpath(
                '/html/body/div[2]/div[2]/div/div[2]/table[1]/tbody/tr[8]/td[1]/text()').extract()
        #
        # 备案信息
        person_id = response.xpath('/html/body/form/table/tbody/tr[3]/td[1]/text()').extract()
        person_name = response.xpath('/html/body/form/table/tbody/tr[3]/td[2]/text()').extract()
        person_post = response.xpath('/html/body/form/table/tbody/tr[3]/td[3]/text()').extract()

        # 经营异常信息
        Abnormal_ID = response.xpath('/html/body/form/table/tbody/tr[3]/td[1]/text()').extract()
        Abnormal_reson = response.xpath('/html/body/form/table/tbody/tr[3]/td[2]/text()').extract()
        Abnormal_time = response.xpath('/html/body/form/table/tbody/tr[3]/td[3]/text()').extract()
        Abnormal_remove = response.xpath(
            '/html/body/form/table/tbody/tr[3]/td[5]/text()').extract()
        Abnormal_remove_date = response.xpath(
            '/html/body/form/table/tbody/tr[3]/td[6]/text()').extract()
        Abnormal_remove_auth = response.xpath(
            '/html/body/form/table/tbody/tr[3]/td[7]/text()').extract()

        #
        # baicinfos = []
        baicinfo = BaicRecordItem()
        baicinfo["url"] = [url]
        baicinfo["city"] = [city]
        try:
            baicinfo["register_ID"] = register_ID
            baicinfo["register_name"] = register_name
            baicinfo["type"] = type
            baicinfo["representative"] = representative
            baicinfo["capital"] = capital
            baicinfo["establishment"] = establishment
            baicinfo["lodgment"] = lodgment
            baicinfo["Operating_start"] = Operating_start
            baicinfo["Operating_end"] = Operating_end
            baicinfo["Business_scope"] = Business_scope
            baicinfo["reg_authority"] = reg_authority
            baicinfo["Approved_date"] = Approved_date
            baicinfo["status"] = status
            # 备案信息
            baicinfo["person_id"] = person_id
            baicinfo["person_name"] = person_name
            baicinfo["person_post"] = person_post

            # 经营异常信息
            baicinfo["Abnormal_ID"] = Abnormal_ID
            baicinfo["Abnormal_reson"] = Abnormal_reson
            baicinfo["Abnormal_time"] = Abnormal_time
            baicinfo["Abnormal_remove"] = Abnormal_remove
            baicinfo["Abnormal_remove_date"] = Abnormal_remove_date
            baicinfo["Abnormal_remove_auth"] = Abnormal_remove_auth

            for i in baicinfo:  # ['Abnormal_remove', 'Abnormal_remove_date']:
                if len(baicinfo[i]) == 0:
                    baicinfo[i] = ['nil']
                # print i +": " + baicinfo[i][0].strip()
            print register_name[0]
            print '*' * 10
            return baicinfo

        except Exception, e:
            print e
            pass
