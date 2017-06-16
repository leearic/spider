# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class HightechInfo(models.Model):
    # 企业信息
    number  = models.IntegerField(verbose_name=u"序号")  # 这个做主键
    KeyID = models.CharField(max_length=255, verbose_name=u"证书编号")
    Unit_name   = models.CharField(max_length=255, verbose_name=u"单位名称")
    address = models.CharField(max_length=255, verbose_name=u"地址")
    Subordinate_Domain = models.CharField(max_length=255, verbose_name=u"所属领域")
    type = models.CharField(max_length=255, verbose_name=u"高企类别")




class IDC_Base_Info(models.Model):
    # 企业信息
    url  = models.CharField(max_length=255, verbose_name=u"爬取网址")
    name  = models.CharField(max_length=255, verbose_name=u"IDC名字")
    company = models.CharField(max_length=255, verbose_name=u"公司名字")
    zone   = models.CharField(max_length=255, verbose_name=u"地区")
    address = models.CharField(max_length=255, verbose_name=u"公司地址")
    phone_number = models.CharField(max_length=255, verbose_name=u"联系电话")
    website = models.CharField(max_length=255, verbose_name=u"网址")
    Main_business = models.CharField(max_length=1024, verbose_name=u"主营业务")
    Satisfaction = models.CharField(max_length=1024, verbose_name=u"满意度")
    QQ = models.CharField(max_length=255, verbose_name=u"qq", default="null")








class Unit_Base_Info(models.Model):
    # 企业详细信息-1

    searched_name  = models.CharField(max_length=255, verbose_name=u"查询到的名字", default='-')
    searching_name = models.CharField(max_length=255, verbose_name=u"需要查询的名字", default='-')

    phone_nunber = models.CharField(max_length=255, verbose_name=u"电话号码")
    # email   = models.CharField(max_length=255, verbose_name=u"邮箱")
    # website = models.CharField(max_length=255, verbose_name=u"网址")
    # address = models.CharField(max_length=255, verbose_name=u"地址")
    #　企业工商信息
    code = models.CharField(max_length=255, verbose_name=u"统一社会信用代码")
    Registration_number = models.CharField(max_length=255, verbose_name=u"注册号")
    Organization_code = models.CharField(max_length=255, verbose_name=u"组织机构代码")
    Operating_state = models.CharField(max_length=255, verbose_name=u"经营状态")
    Legal_representative = models.CharField(max_length=255, verbose_name=u"法定代表人")
    registered_capital = models.CharField(max_length=255, verbose_name=u"注册资本")
    Company_type = models.CharField(max_length=255, verbose_name=u"公司类型")
    date_of_establishment = models.CharField(max_length=255, verbose_name=u"成立日期")
    Operating_period = models.CharField(max_length=255, verbose_name=u"营业期限")
    registration_authority = models.CharField(max_length=255, verbose_name=u"登记机关")
    Date_of_issue = models.CharField(max_length=255, verbose_name=u"发照日期")
    company_size = models.CharField(max_length=255, verbose_name=u"公司规模")
    Subordinate_industry = models.CharField(max_length=255, verbose_name=u"所属行业")
    English_name = models.CharField(max_length=255, verbose_name=u"英文名")
    Name_used_Before = models.CharField(max_length=255, verbose_name=u"曾用名")
    Enterprise_address = models.CharField(max_length=255, verbose_name=u"企业地址")
    Business_scope = models.CharField(max_length=255, verbose_name=u"经营范围")


class Unit_Base_Info_Shareholder_Info(models.Model):
    # 股东信息
    searched_name  = models.CharField(max_length=255, verbose_name=u"查询到的名字", default='-')
    searching_name = models.CharField(max_length=255, verbose_name=u"需要查询的名字", default='-')
    Shareholder  = models.CharField(max_length=255, verbose_name=u"股东")
    Shareholding_ratio = models.CharField(max_length=255, verbose_name=u"持股比例")
    Subscribed_capital_contribution   = models.CharField(max_length=255, verbose_name=u"认缴出资额")
    Subscription_Date = models.CharField(max_length=255, verbose_name=u"认缴出资日期")
    Shareholder_type = models.CharField(max_length=255, verbose_name=u"股东类型")


class Unit_Base_Info_Changed_Info(models.Model):
    # 变更信息
    searched_name  = models.CharField(max_length=255, verbose_name=u"查询到的名字", default='-')
    searching_name = models.CharField(max_length=255, verbose_name=u"需要查询的名字", default='-')
    Change_date = models.CharField(max_length=255, verbose_name=u"变更日期")
    Change_item  = models.CharField(max_length=255, verbose_name=u"变更项目")
    Before_change = models.CharField(max_length=255, verbose_name=u"变更前")
    After_change   = models.CharField(max_length=255, verbose_name=u"变更后")

class Unit_annual_reports_Base_Info(models.Model):
    # 企业年报-企业基本信息
    searched_name  = models.CharField(max_length=255, verbose_name=u"查询到的名字", default='-')
    searching_name = models.CharField(max_length=255, verbose_name=u"需要查询的名字", default='-')
    Registration_number = models.CharField(max_length=255, verbose_name=u"注册号")
    Business_state = models.CharField(max_length=255, verbose_name=u"企业经营状态")
    Enterprise_telephone  = models.CharField(max_length=255, verbose_name=u"企业联系电话")
    Email = models.CharField(max_length=255, verbose_name=u"电子邮箱")
    Postcode   = models.CharField(max_length=255, verbose_name=u"邮政编码")
    number_of_people_engaged = models.CharField(max_length=255, verbose_name=u"从业人数")
    residence = models.CharField(max_length=255, verbose_name=u"住所")
    transfer_of_shareholder_equity  = models.CharField(max_length=255, verbose_name=u"有限责任公司本年度是否发生股东股权转让")
    investment_Info = models.CharField(max_length=255, verbose_name=u"企业是否有投资信息或购买其他公司股权")


class Unit_annual_reports_Website_Info(models.Model):
    # 企业年报-网站或网店信息
    searched_name  = models.CharField(max_length=255, verbose_name=u"查询到的名字", default='-')
    searching_name = models.CharField(max_length=255, verbose_name=u"需要查询的名字", default='-')

    Web_Type = models.CharField(max_length=255, verbose_name=u"类型")
    Web_Name = models.CharField(max_length=255, verbose_name=u"名称")
    Web_Site  = models.CharField(max_length=255, verbose_name=u"网址")


class Unit_annual_Promoters_and_reports_investment_Info(models.Model):
    # 企业年报-发起人及出资信息
    searched_name  = models.CharField(max_length=255, verbose_name=u"查询到的名字", default='-')
    searching_name = models.CharField(max_length=255, verbose_name=u"需要查询的名字", default='-')
    Sponsor = models.CharField(max_length=255, verbose_name=u"发起人")
    Subscribed_capital_contribution = models.CharField(max_length=255, verbose_name=u"认缴出资额（万元）")
    Time_of_subscription  = models.CharField(max_length=255, verbose_name=u"认缴出资时间")
    Subscribed_capital_contribution = models.CharField(max_length=255, verbose_name=u"认缴出资方式")
    Paid_in_capital_contribution   = models.CharField(max_length=255, verbose_name=u"实缴出资额（万元）")
    Investment_time = models.CharField(max_length=255, verbose_name=u"出资时间")
    Investment_method = models.CharField(max_length=255, verbose_name=u"出资方式")





class Itjuzi_Company_Info(models.Model):
    # 企业年报-发起人及出资信息
    company_allname = models.CharField(max_length=999, verbose_name=u"企业全名")
    company_name = models.CharField(max_length=999, verbose_name=u"企业名")



class Gao_Company_Info(models.Model):
    # 企业年报-发起人及出资信息
    phone_nunber = models.CharField(max_length=255, verbose_name=u"电话号码")
    Enterprise_address = models.CharField(max_length=255, verbose_name=u"企业地址")
    company_name = models.CharField(max_length=999, verbose_name=u"企业全名")
    Legal_representative = models.CharField(max_length=255, verbose_name=u"法定代表人")
    Business_scope = models.CharField(max_length=255, verbose_name=u"经营范围")
    status  =  models.CharField(max_length=255, verbose_name=u"状态")
    category = models.CharField(max_length=255, verbose_name=u"分类")

















