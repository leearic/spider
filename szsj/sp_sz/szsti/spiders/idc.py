# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from szsti.utils.Save2DB import DjORM

class SzSpider(scrapy.Spider):
    name = "idc"
    allowed_domains = ["dian.idcquan.com"]
    start_urls = ['http://dian.idcquan.com/item.php?act=list&catid=4']
    # start_urls = ['http://dian.idcquan.com/item.php?act=detail&id=1264']
    # start_urls = ["http://dian.idcquan.com/item.php?act=detail&id=1320"]
    # start_urls = ["http://dian.idcquan.com/item.php?act=detail&id=631"]


    def parse(self, response):

        baseurl = "http://dian.idcquan.com"
        indexs =  response.xpath('//*[@id="px_list2"]/dl/dd[1]/a/@href').extract()
        # 获取页面 详细信息,然后到一个解析方法去解析
        for index in indexs:
            url =  baseurl + index
            yield  Request(url=url, callback=self.parse_detail)

        # 获取分页
        pages = response.xpath('//*[@id="page"]/p/a/@href').extract()
        for page in pages:
            url = baseurl + page
            # print url
            yield  Request(url=url, callback=self.parse)

        pass


    def parse_detail(self, response):
    # def parse(self, response):
        item = {}
        # url
        item["url"] = response.url
        try:
            # name
            item["name"] = response.xpath('//*[@id="gongs_name"]/text()').extract()[0].strip()
            # company
            item["company"] = response.xpath('//p[@class="quanming"]/text()').extract()[0].strip() # //*[@id="erp_left"]/div[1]/div/div/p[3]
            # zone
            item["zone"] = response.xpath('//*[@id="erp_left"]/div[2]/div[1]/dl/dt/p[1]/span/text()').extract()[0].strip()
            # address
            item["address"] = response.xpath('//*[@id="erp_left"]/div[2]/div[1]/dl/dt/p[2]/span/text()').extract()[0].strip()
            # phone number
            item["phone_number"] = response.xpath('//*[@id="erp_left"]/div[2]/div[1]/dl/dt/p[3]/i/text()').extract()[0].strip()
            # website
            item["website"] = response.xpath('//*[@id="erp_left"]/div[2]/div[1]/dl/dt/p[4]/em/a/@href').extract()[0].strip()
            # main bussiness
            item["Main_business"] = response.xpath('//*[@id="erp_left"]/div[2]/div[1]/dl/dt/p[5]/span/text()').extract()[0].strip()
            # Satisfaction
            item["Satisfaction"] = response.xpath('//*[@id="erp_left"]/div[2]/div[1]/dl/dt/p[9]/text()').extract()[0].strip()


            # QQ
            try:
                qqoneline = response.xpath('//*[@id="erp_left"]/div[2]/div[1]/dl/dt/p[7]/a/@href').extract()[0].strip()
                item["qq"] = qqoneline.split("=")[2].split("&")[0]
            except Exception:
                item["qq"] = "null"

        except Exception:
            # name
            item["name"] = response.xpath('//table[@class="custom_field"]/tr[3]/td[2]/text()').extract()[0].strip()
            # company
            item["company"] = response.xpath('//table[@class="custom_field"]/tr[3]/td[2]/text()').extract()[0].strip()  # //*[@id="erp_left"]/div[1]/div/div/p[3]
            # zone
            try:
                item["zone"] = response.xpath('//table[@class="custom_field"]/tr[6]/td[2]/a[2]/text()').extract()[0].strip()
            except Exception:
                item["zone"] = response.xpath('//table[@class="custom_field"]/tr[5]/td[2]/a[2]/text()').extract()[0].strip()
            # # address
            try:
                item["address"] = response.xpath('//table[@class="custom_field"]/tr[7]/td[2]/text()').extract()[0].strip()
            except Exception:
                item["address"] = response.xpath('//table[@class="custom_field"]/tr[6]/td[2]/text()').extract()[0].strip()
            # phone number
            try:
                item["phone_number"] = response.xpath('//table[@class="custom_field"]/tr[9]/td[2]/text()').extract()[0].strip()
            except Exception:
                item["phone_number"] = response.xpath('//table[@class="custom_field"]/tr[8]/td[2]/text()').extract()[0].strip()
            # website
            try:
                item["website"] = response.xpath('//table[@class="custom_field"]/tr[11]/td[2]/a/@href').extract()[0].strip()
            except Exception:
                item["website"] = response.xpath('//table[@class="custom_field"]/tr[10]/td[2]/a/@href').extract()[0].strip()


            # main bussiness
            try:
                item["Main_business"] = response.xpath('//table[@class="custom_field"]/tr[8]/td[2]').extract()[0].strip()
            except Exception:
                item["Main_business"] = response.xpath('//table[@class="custom_field"]/tr[7]/td[2]').extract()[0].strip()

            # Satisfaction
            try:
                item["Satisfaction"] = response.xpath('//*[@id="subject_impress"]').extract()[0].strip()
            except Exception:
                item["Satisfaction"] = response.xpath('//*[@id="subject_impress"]').extract()[0].strip()

            # QQ
            try:
                qqoneline = response.xpath('//table[@class="custom_field"]/tr[10]/td[2]/a/@href').extract()[0].strip()
                item["qq"] = qqoneline.split("=")[2].split("&")[0]
            except Exception:
                item["qq"] = "null"


        print item["qq"]
        print  "*" * 30

        DjORM.save_IDC_Base_Info(item)