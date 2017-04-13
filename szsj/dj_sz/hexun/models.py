# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Companys(models.Model):
    Code = models.CharField(max_length=255, verbose_name=u"股票代码")
    Name = models.CharField(max_length=255, verbose_name=u"股票简称")
    ALl_Name = models.CharField(max_length=255, verbose_name=u"公司全称")
    History_Name = models.CharField(max_length=255, verbose_name=u"曾用名")


class base_Info(models.Model):

    company_code = models.CharField(max_length=255, verbose_name=u"公司股票代码")

    # 公司简介-基本信息

    name = models.CharField(max_length=255, verbose_name=u"公司名字")
    daima = models.CharField(max_length=255, verbose_name=u"股票代码")
    quancheng = models.CharField(max_length=255, verbose_name=u"公司全称")
    englishname = models.CharField(max_length=255, verbose_name=u"公司英文名称")
    cengyongming = models.CharField(max_length=255, verbose_name=u"曾用名")
    chengliriqi = models.CharField(max_length=255, verbose_name=u"成立日期")
    suoshuhangye = models.CharField(max_length=255, verbose_name=u"所属行业")
    suoshugannian = models.CharField(max_length=255, verbose_name=u"所属概念")
    suoshudiyu = models.CharField(max_length=255, verbose_name=u"所属地域")
    fadingdabiaoren = models.CharField(max_length=255, verbose_name=u"法定代表人")
    dulidongshi = models.CharField(max_length=255, verbose_name=u"独立董事")
    zixunfuwujigou = models.CharField(max_length=255, verbose_name=u"咨询服务机构")
    kuaijishiwusuo = models.CharField(max_length=255, verbose_name=u"会计师事务所")
    zhengquanshifudaibiao = models.CharField(max_length=255, verbose_name=u"证券事务代表")
    # 公司简介-证券信息
    faxingriqi = models.CharField(max_length=255, verbose_name=u"发行日期")
    shangshiriqi = models.CharField(max_length=255, verbose_name=u"上市日期")
    shangshijiaoyisuo = models.CharField(max_length=255, verbose_name=u"上市交易所")
    zhengquanleixing = models.CharField(max_length=255, verbose_name=u"证券类型")
    liutongguben = models.CharField(max_length=255, verbose_name=u"流通股本")
    zongguben = models.CharField(max_length=255, verbose_name=u"总股本")
    zhuchengxiaoshang = models.CharField(max_length=255, verbose_name=u"主承销商")
    faxingjia = models.CharField(max_length=255, verbose_name=u"发行价")
    shangshisourikaipanjia = models.CharField(max_length=255, verbose_name=u"上市首日开盘价")
    shangshishourizhangdiefu = models.CharField(max_length=255, verbose_name=u"上市首日涨跌幅")
    shangshishourihuanshoulv = models.CharField(max_length=255, verbose_name=u" 上市首日换手率")
    tebiechulihetuishi = models.CharField(max_length=255, verbose_name=u"特别处理和退市")
    faxingshiyinglv = models.CharField(max_length=255, verbose_name=u"发行市盈率")
    zuixinshiyinglv = models.CharField(max_length=255, verbose_name=u"最新市盈率")

    # 公司简介-工商信息
    zhuceziben = models.CharField(max_length=255, verbose_name=u"注册资本")
    zhucedizhi = models.CharField(max_length=255, verbose_name=u"注册地址")
    suodeisuilv = models.CharField(max_length=255, verbose_name=u"所得税率")
    bangongdizhi = models.CharField(max_length=255, verbose_name=u"办公地址")
    zhuyaochanpin = models.CharField(max_length=255, verbose_name=u"主要产品(业务)")

    # 公司简介-联系方式
    lianxidianhua = models.CharField(max_length=255, verbose_name=u"联系电话(董秘)")
    gongsichuanzhen = models.CharField(max_length=255, verbose_name=u"公司传真")
    dianziyouxiang = models.CharField(max_length=255, verbose_name=u"电子邮箱")
    gongsiwangzhi = models.CharField(max_length=255, verbose_name=u"公司网址")
    lianxiren = models.CharField(max_length=255, verbose_name=u"联系人")
    youzhengbianma = models.CharField(max_length=255, verbose_name=u"邮政编码")

    jingyingfanwei = models.CharField(max_length=999, verbose_name=u"经营范围")

    gongsijianjie = models.CharField(max_length=999, verbose_name=u"公司简介")


class Gaoguan_Info(models.Model):
    company_code = models.CharField(max_length=255, verbose_name=u"公司股票代码", default='-')
    # 高管-高管成员
    dongjiangao = models.CharField(max_length=255, verbose_name=u"董监高姓名", default='-')
    gaoguanzhiwu = models.CharField(max_length=255, verbose_name=u"高管职务", default='-')
    renzhiriqi = models.CharField(max_length=255, verbose_name=u"任职日期", default='-')
    lizhiriqi = models.CharField(max_length=255, verbose_name=u"离职日期", default='-')
    xueli = models.CharField(max_length=255, verbose_name=u"学历", default='-')
    nianxin = models.CharField(max_length=255, verbose_name=u"年薪(万元)", default='-')
    chiguzonge = models.CharField(max_length=255, verbose_name=u"持股总额(万元)", default='-')
    chigushuliang = models.CharField(max_length=255, verbose_name=u"持股数量(万股)", default='-')


class Dongshihui_Info(models.Model):
    company_code = models.CharField(max_length=255, verbose_name=u"公司股票代码", default='-')
    # 高管-董事会成员
    dongjiangao = models.CharField(max_length=255, verbose_name=u"董监高姓名", default='-')
    gaoguanzhiwu = models.CharField(max_length=255, verbose_name=u"高管职务", default='-')
    renzhiriqi = models.CharField(max_length=255, verbose_name=u"任职日期", default='-')
    lizhiriqi = models.CharField(max_length=255, verbose_name=u"离职日期", default='-')
    xueli = models.CharField(max_length=255, verbose_name=u"学历", default='-')
    nianxin = models.CharField(max_length=255, verbose_name=u"年薪(万元)", default='-')
    chiguzonge = models.CharField(max_length=255, verbose_name=u"持股总额(万元)", default='-')
    chigushuliang = models.CharField(max_length=255, verbose_name=u"持股数量(万股)", default='-')

class Jianshihui_Info(models.Model):
    company_code = models.CharField(max_length=255, verbose_name=u"公司股票代码", default='-')
    # 高管-监事会成员
    dongjiangao = models.CharField(max_length=255, verbose_name=u"董监高姓名", default='-')
    gaoguanzhiwu = models.CharField(max_length=255, verbose_name=u"高管职务", default='-')
    renzhiriqi = models.CharField(max_length=255, verbose_name=u"任职日期", default='-')
    lizhiriqi = models.CharField(max_length=255, verbose_name=u"离职日期", default='-')
    xueli = models.CharField(max_length=255, verbose_name=u"学历", default='-')
    nianxin = models.CharField(max_length=255, verbose_name=u"年薪(万元)", default='-')
    chiguzonge = models.CharField(max_length=255, verbose_name=u"持股总额(万元)", default='-')
    chigushuliang = models.CharField(max_length=255, verbose_name=u"持股数量(万股)", default='-')



class Fenhong_Info(models.Model):
    company_code = models.CharField(max_length=255, verbose_name=u"公司股票代码", default='-')
    # 分红、历年分红详表
    gonggaoshijian = models.CharField(max_length=255, verbose_name=u"公告时间", default='-')
    kuaijiniandu = models.CharField(max_length=255, verbose_name=u"会计年度", default='-')
    songgu = models.CharField(max_length=255, verbose_name=u"送股(股/10股)", default='-')
    paixi = models.CharField(max_length=255, verbose_name=u"派息(元/10股)", default='-')
    guquandengjiri = models.CharField(max_length=255, verbose_name=u"股权登记日", default='-')
    guquanchuxiri = models.CharField(max_length=255, verbose_name=u"除权除息日", default='-')
    honggushangshiri = models.CharField(max_length=255, verbose_name=u"红股上市日", default='-')
    shifoshisi = models.CharField(max_length=255, verbose_name=u"是否实施", default='-')
    xiangqing = models.CharField(max_length=255, verbose_name=u"分红详情", default='-')


class Fenhong_Zhuanzeng_Info(models.Model):
    company_code = models.CharField(max_length=255, verbose_name=u"公司股票代码", default='-')
    # 分红、转增股本
    gonggaoshijian = models.CharField(max_length=255, verbose_name=u"公告时间", default='-')
    zhuanzeng = models.CharField(max_length=255, verbose_name=u"转增(股/10股)", default='-')
    chuquanchuxiri = models.CharField(max_length=255, verbose_name=u"除权除息日", default='-')
    chuquandengjiri = models.CharField(max_length=255, verbose_name=u"除权登记日", default='-')
    zhuanzenggushangshiri = models.CharField(max_length=255, verbose_name=u"转增股上市日", default='-')
    tongqisonggu = models.CharField(max_length=255, verbose_name=u"同期送股(股/10股)", default='-')
    fanganjianjie = models.CharField(max_length=255, verbose_name=u"方案简介", default='-')
    shifoshisi = models.CharField(max_length=255, verbose_name=u"是否实施", default='-')
    xiangqing = models.CharField(max_length=255, verbose_name=u"分红详情", default='-')

class Fenhong_Peigu_Info(models.Model):
    company_code = models.CharField(max_length=255, verbose_name=u"公司股票代码", default='-')
    # 分红、配 股
    gonggaoshijian = models.CharField(max_length=255, verbose_name=u"公告时间", default='-')
    peigufangan = models.CharField(max_length=255, verbose_name=u"配股方案(股/10股)", default='-')
    peigujia = models.CharField(max_length=255, verbose_name=u"配股价(元)", default='-')
    jizhunguben = models.CharField(max_length=255, verbose_name=u"基准股本(万股)", default='-')
    chuquanri = models.CharField(max_length=255, verbose_name=u"除权日", default='-')
    guquandengjiri = models.CharField(max_length=255, verbose_name=u"股权登记日", default='-')
    jiaokuanqishiri = models.CharField(max_length=255, verbose_name=u"缴款起始日", default='-')
    jiaokuanzhongzhiri = models.CharField(max_length=255, verbose_name=u"缴款终止日", default='-')
    peigushangshiri = models.CharField(max_length=255, verbose_name=u"配股上市日", default='-')
    mujizijin = models.CharField(max_length=255, verbose_name=u"募集资金合计(元)", default='-')
    xiangqing = models.CharField(max_length=255, verbose_name=u"分红详情", default='-')

class Fenhong_Huigou_Info(models.Model):
    company_code = models.CharField(max_length=255, verbose_name=u"公司股票代码", default='-')
    # 分红、回 购
    gonggaoshijian = models.CharField(max_length=255, verbose_name=u"公告时间", default='-')
    huigouzanzonggubenbili = models.CharField(max_length=255, verbose_name=u"回购占总股本比例%", default='-')
    huigougushu = models.CharField(max_length=255, verbose_name=u"回购股数(股)", default='-')
    nihuigoujiage = models.CharField(max_length=255, verbose_name=u"拟回购价格(元)", default='-')
    gonggaoqianrigujia = models.CharField(max_length=255, verbose_name=u"公告前日股价(元)", default='-')
    goumaizuigaojia = models.CharField(max_length=255, verbose_name=u"购买最高价(元)", default='-')
    goumaizuidijia = models.CharField(max_length=255, verbose_name=u"购买最低价(元)", default='-')
    huigouzongjine = models.CharField(max_length=255, verbose_name=u"回购总金额(万元)", default='-')
    shifoshisi = models.CharField(max_length=255, verbose_name=u"是否实施", default='-')
    xiangqing = models.CharField(max_length=255, verbose_name=u"分红详情", default='-')






class Showrufenbu_Info(models.Model):
    company_code = models.CharField(max_length=255, verbose_name=u"公司股票代码", default='-')
    # 收入分布
    leibiemingcheng = models.CharField(max_length=255, verbose_name=u"类别名称", default='-')
    yinyeshouru = models.CharField(max_length=255, verbose_name=u"营业收入(万元)", default='-')
    zhanyinyeshourubili = models.CharField(max_length=255, verbose_name=u"占营业收入比例(%)", default='-')
    yinyechengben = models.CharField(max_length=255, verbose_name=u"营业成本(万元)", default='-')
    zhanchengbenbili = models.CharField(max_length=255, verbose_name=u"占成本比例", default='-')
    yingyelirun = models.CharField(max_length=255, verbose_name=u"营业利润(万元)", default='-')
    zhanlirunbili = models.CharField(max_length=255, verbose_name=u"占利润比例", default='-')
    maolilv = models.CharField(max_length=255, verbose_name=u"毛利率(%)", default='-')






























