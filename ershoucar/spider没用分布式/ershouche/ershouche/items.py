# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarItem(scrapy.Item):
    # 商品名称
    name = scrapy.Field()
    # 购买网址
    url = scrapy.Field()


#class CarinfoItem(scrapy.Item):
    # 车主
    owner = scrapy.Field()
    # # 车主职业
    # occupation = scrapy.Field()
    # 车主地址
    # owner_address = scrapy.Field()
    # # 换车理由
    # reason = scrapy.Field()
    # 汽车型号
    module = scrapy.Field()
    # 汽车价格
    price = scrapy.Field()
    # 汽车上牌时间
    registed_time = scrapy.Field()
    # 行程
    mileage = scrapy.Field()
    # 排量
    displacement = scrapy.Field()
    # 汽车所在地
    car_address = scrapy.Field()
    # 车主说明
    owner_say = scrapy.Field()

#class TestingInfoItem(scrapy.Item):
    # 车身颜色
    color = scrapy.Field()
    # 年检时间
    annual_time = scrapy.Field()
    # 交强险时间
    delivery_time = scrapy.Field()
    # 商业保险到期时间
    insurance_time = scrapy.Field()
    # 归属地
    address = scrapy.Field()
    # 过户次数
    transfer_number = scrapy.Field()
    # 购车发票
    invoice = scrapy.Field()
    # 4s 保养
    maintenance = scrapy.Field()
    # 事故排查
    accident_investigation = scrapy.Field()
    # 安全检测
    safety_detection = scrapy.Field()
    # 外观检测
    appearance_detection = scrapy.Field()
    # 驾驶检测
    driving_test = scrapy.Field()
    # 检测结果
    # result = scrapy.Field()

#class ImageInfoItem(scrapy.Item):
    # " 汽车展示图片,这里放几个就行了,没全部放进来"
    url0 = scrapy.Field()
    url1 = scrapy.Field()
    url2 = scrapy.Field()
    url3 = scrapy.Field()
    url4 = scrapy.Field()
    url5 = scrapy.Field()
    url6 = scrapy.Field()
    url7 = scrapy.Field()
class BaseInfoItem(scrapy.Item):

    # 基础信息太多,Demo没必要把所有数据都爬下来 ....
    pass





















