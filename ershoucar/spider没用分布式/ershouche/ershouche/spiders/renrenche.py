# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from ershouche import settings
from ershouche.utils import iscrawled as cr
from ershouche.items import CarItem



class ExampleSpider(scrapy.Spider):
    name = "renrenche"
    allowed_domains = ["renrenche.com"]
    start_urls = (
        'http://www.renrenche.com/cn/ershouche/',
    )

    def parse(self, response):
        sel = Selector(response)
        # 获取车辆信息的页面，并且用splash来解析
        ItemUrls = sel.xpath('//li[@class="span6 list-item"]/a/@href').extract()
        for url in ItemUrls:
            url = settings.BaseUrl + url
            yield Request(url=url, callback=self.parse_car,
                                     meta={
                                         'splash': {
                                                'endpoint' : "render.html",
                                                'args': {
                                                        'wait': 0.8,
                                                    },
                                                },
                                         'url': url
                                         }
                                     )
        # 获取分页信息
        pages = sel.xpath('//ul[@class="pagination"]/li/a/@href').extract()
        for page in pages:
            page = settings.BaseUrl + page
            if "javascript" in page:
                pass
            else:
                # pass
                yield Request(url=page, callback=self.parse)

    def parse_car(self, response):
        sel = Selector(response)
        """ CarItem """
        # 汽车型号
        name = sel.xpath('//div[@class="title"]/text()').extract()
        # 购买网址
        url = response.meta['url']
        """CarinfoItem"""
        # 车主
        owner = sel.xpath('//div[@class="text-block bottom-left"]/h3/text()').extract()
        # 汽车型号
        module =  name
        # 汽车价格
        price = sel.xpath('//p[@class="box-price"]/text()').extract()
        # 汽车上牌时间 [0] 上牌时间 [1] 是行程
        registed_time_and_mileage = sel.xpath('//ul[@class="row-fluid list-unstyled box-list-primary"]/li[@class="span7"]/p/strong/text()').extract()
        # 汽车信息. [0] 是排量   [1] 是地区
        displacement_and_car_address = sel.xpath('//ul[@class="row-fluid list-unstyled box-list-primary"]/li[@class="span5"]/p/strong/text()').extract()
        # 车主说明
        owner_say = sel.xpath('//div[@class="text-block bottom-left"]/p/text()').extract()
        """ TestingInfoItem """
        # 车身颜色
        color = sel.xpath('//div[@class="span23 offset1"]/table/tbody/tr[1]/td[2]/text()').extract()
        # 年检时间
        annual_time =sel.xpath('//div[@class="span23 offset1"]/table/tbody/tr[1]/td[4]/text()').extract()
        #  交强险时间
        delivery_time =sel.xpath('//div[@class="span23 offset1"]/table/tbody/tr[1]/td[6]/text()').extract()
        # 商业保险到期时间
        insurance_time =sel.xpath('//div[@class="span23 offset1"]/table/tbody/tr[1]/td[8]/text()').extract()
        # 归属地
        address = sel.xpath('//div[@class="span23 offset1"]/table/tbody/tr[2]/td[2]/text()').extract()
        # 过户次数
        transfer_number = sel.xpath('//div[@class="span23 offset1"]/table/tbody/tr[2]/td[4]/text()').extract()
        # 购车发票
        invoice = sel.xpath('//div[@class="span23 offset1"]/table/tbody/tr[2]/td[6]/text()').extract()
        # 4s 保养
        maintenance = sel.xpath('//div[@class="span23 offset1"]/table/tbody/tr[2]/td[8]/text()').extract()
        # 事故排查
        accident_investigation = sel.xpath('//div[@class="row-fluid title"][1]/p[@class="span19"]/text()').extract()
        # 安全检测
        safety_detection = sel.xpath('//div[@class="row-fluid title"][2]/p[@class="span19"]/text()').extract()
        # 外观检测
        appearance_detection = sel.xpath('//div[@class="row-fluid title"][@id="detail_blemish_inspect"]/p[@class="span19"]/text()').extract()
        # 驾驶检测
        driving_test = sel.xpath('//div[@class="row-fluid title"][4]/p[@class="span19"]/text()').extract()
        # 检测结果
        # result =
        """ ImageInfoModel """
        urls = sel.xpath('//div[@class="container detail-gallery"]/div/div/div/div/img/@data-src').extract()


        try:
            ifcrawl = cr.iscrawled()
        except Exception, e:
            print e


        if ifcrawl.IsCrawled(url):
            items = []
            item = CarItem()

            item["name"] = name
            item["url"] = [url]
            if len(owner) != 0:
                item["owner"] = owner
            else:
                item["owner"] = ["unknown"]
            item["module"] = module
            item["price"] = price

            if len(registed_time_and_mileage) != 0:
                item["registed_time"] = [registed_time_and_mileage[0]]
            else:
                item["registed_time"] = ["unknown"]
            if len(registed_time_and_mileage) != 0:
                item["mileage"] = [registed_time_and_mileage[1]]
            else:
                item["mileage"] = ["unknown"]

            if len(displacement_and_car_address) != 0:
                item["displacement"] = [displacement_and_car_address[0]]
            else:
                item["displacement"] = ["unknown"]
            if len(registed_time_and_mileage) != 0:
                item["car_address"] = [displacement_and_car_address[1]]
            else:
                item["car_address"] = ["unknown"]
            if len(owner) != 0:
                item["owner_say"] = owner_say
            else:
                item["owner_say"] = ["unknown"]
            item["color"] = color
            item["annual_time"] = annual_time
            item["delivery_time"] = delivery_time
            item["insurance_time"] =insurance_time
            item["address"] = address
            item["transfer_number"] =transfer_number
            item["transfer_number"] = transfer_number
            item["invoice"] =invoice
            item["maintenance"]  = maintenance
            item["accident_investigation"] = accident_investigation
            item["safety_detection"] = safety_detection
            item["appearance_detection"] = appearance_detection
            item["driving_test"] = driving_test

            item["url0"] = [urls[0]]
            item["url1"] = [urls[1]]
            item["url2"] = [urls[2]]
            item["url3"] = [urls[3]]
            item["url4"] = [urls[4]]
            item["url5"] = [urls[5]]
            item["url6"] = [urls[6]]
            item["url7"] = [urls[7]]

            items.append(item)
            print item["url0"]

            return  items
        else:
            print url + "  have crawled !!"


