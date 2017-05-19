# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.http import Request
from fang_with_js.items import FangItem

from scrapy.selector import Selector
class ASpider(scrapy.Spider):
    name = "a"
    allowed_domains = ["anjuke.com"]
    start_urls = (
        'http://www.anjuke.com/sy-city.html',
    )

    def __init__(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:8080/wd/hub', desired_capabilities={
            'takeScreenshot': False,
            'javascriptEnabled': True,

        })

    def parse(self, response):
        # 从全国地区获取到每一个地区的二级域名
        self.driver.get(response.url)
        aa = self.driver.page_source
        # print aa
        body = Selector(text=aa)
        #
        urls =  body.xpath('//div[@class="cities_boxer"]/div/dl/dd/a/@href').extract()
        zones =  body.xpath('//div[@class="cities_boxer"]/div/dl/dd/a/text()').extract()
        for i in xrange(len(urls)):
            url = urls[i]+'/sale/'
            # print url
            yield Request(url=url, callback=self.get_zone_house_info, meta={'zone': zones[0], 'url': url})

    def get_zone_house_info(self, response):
        zone =  response.meta['zone']
        url = response.meta['url']

        self.driver.get(response.url)
        aa = self.driver.page_source
        # print aa
        body = Selector(text=aa)


        urls = body.xpath('//div[@class="sale-left"]/ul/li/div[@class="house-details"]/div/a/@href').extract()
        for i in urls:
            yield  Request(url=i, callback=self.get_house_detail_info, meta={'zone': zone})

        pages = body.xpath('//div[@class="multi-page"]/a/@href').extract()
        for page in pages:

            yield  Request(url=page, callback=self.get_zone_house_info, meta={'zone': zone, 'url': url})
        pass

    def get_house_detail_info(self, response):
        # 区域
        zone =  response.meta['zone']
        # URL
        url =  response.url
        self.driver.get(response.url)
        aa = self.driver.page_source
        # print aa
        body = Selector(text=aa)

        # 商品图片
        image = body.xpath('//div[@class="picCon"]/ul/li[1]/a/img/@src').extract()
        # 售价
        saleprice = body.xpath('//div[@class="box prop-info-box"]/div[1]/div[@class="litem fl"]/dl[1]/dd/strong/span/text()').extract()
        # 首付
        shoufu = body.xpath('//div[@class="box prop-info-box"]/div[1]/div[@class="litem fl"]/dl[2]/dd/text()').extract()
        # 月供 *
        monthpay = body.xpath('//div[@class="box prop-info-box"]/div[1]/div[@class="litem fl"]/dl[3]/dd/text()').extract()
        # 单价
        unit_price = body.xpath('//div[@class="box prop-info-box"]/div[1]/div[@class="litem fl"]/dl[4]/dd/text()').extract()
        # 所在小区 *
        quarters = body.xpath('//div[@class="box prop-info-box"]/div[1]/div[@class="litem fl"]/dl[5]/dd/text()').extract()
        # 位置 *
        position = body.xpath('//div[@class="box prop-info-box"]/div[1]/div[@class="litem fl"]/dl[6]/dd/a/text()').extract()

        # 房型
        apartment = body.xpath('//div[@class="box prop-info-box"]/div[1]/div[@class="ritem fr"]/dl[1]/dd/text()').extract()
        # 面积
        area = body.xpath('//div[@class="box prop-info-box"]/div[1]/div[@class="ritem fr"]/dl[2]/dd/text()').extract()
        # 朝向
        orientation = body.xpath('//div[@class="box prop-info-box"]/div[1]/div[@class="ritem fr"]/dl[3]/dd/text()').extract()
        # 楼层
        floor = body.xpath('//div[@class="box prop-info-box"]/div[1]/div[@class="ritem fr"]/dl[4]/dd/text()').extract()
        # 装修 *
        renovation = body.xpath('//div[@class="box prop-info-box"]/div[1]/div[@class="ritem fr"]/dl[5]/dd/text()').extract()
        # 类型 *
        type = body.xpath('//div[@class="box prop-info-box"]/div[1]/div[@class="ritem fr"]/dl[6]/dd/text()').extract()

        details = body.xpath('//div[@class="box prop-info-box"]/div[@class="pro_detail"]/div[@class="pro_main cf"]/div[@class="pro_con wb"]').extract()

        if len(monthpay) == 0:
            monthpay = ['nil']
        if len(quarters) == 0:
            quarters = ['nil']
        if len(position) == 0:
            position = ['nil']
        if len(type) == 0:
            type = ['nil']
        if len(renovation) == 0:
            renovation = ['nil']

        anjuitems = []
        anjuitem = FangItem()
        print "*"*40
        #
        anjuitem["zone"] = zone
        anjuitem["url"] = url
        anjuitem["image"] = image[0]

        anjuitem["saleprice"] = saleprice[0]
        anjuitem["shoufu"] = shoufu[0]
        anjuitem["monthpay"] = monthpay[0]
        anjuitem["unit_price"] = unit_price[0]
        anjuitem["quarters"] = quarters[0]
        anjuitem["position"] =  position[0]
        anjuitem["apartment"] = apartment[0]
        anjuitem["area"] = area[0]
        anjuitem["orientation"] = orientation[0]
        anjuitem["floor"] = floor[0]
        anjuitem["renovation"] = renovation[0]
        anjuitem["type"] = type[0]
        anjuitem["details"] = details[0]
        anjuitems.append(anjuitem)
        # time.sleep(2)

        return anjuitems