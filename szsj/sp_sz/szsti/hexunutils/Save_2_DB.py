# -*- coding: utf-8 -*-
import sys, os
from szsti.settings import djpath
if djpath not in sys.path:
    sys.path.append(djpath)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_sz.settings")
django.setup()

from hexun.models import Companys, base_Info, Gaoguan_Info, Dongshihui_Info,  Jianshihui_Info, Fenhong_Info, Fenhong_Zhuanzeng_Info, Fenhong_Peigu_Info, Fenhong_Huigou_Info, Showrufenbu_Info


class Hexun(object):

    @classmethod
    def Save_Base_Info(self, item):
        base_info = base_Info()
        # 公司简介-基本信息
        base_info.company_code = item["company_code"]
        base_info.name = item["name"]
        base_info.daima = item["daima"]
        base_info.quancheng = item["quancheng"]
        base_info.englishname = item["Englishname"]
        base_info.cengyongming = item["cengyongming"]
        base_info.chengliriqi = item["chengliriqi"]
        base_info.suoshuhangye = item["suoshuhangye"]
        base_info.suoshugannian = item["suoshugannian"]
        base_info.suoshudiyu = item["suoshudiyu"]
        base_info.fadingdabiaoren = item["fadingdabiaoren"]
        base_info.dulidongshi = item["dulidongshi"]
        base_info.zixunfuwujigou = item["zixunfuwujigou"]
        base_info.kuaijishiwusuo = item["kuaijishiwusuo"]
        base_info.zhengquanshifudaibiao = item["zhengquanshifudaibiao"]
        # 公司简介-证券信息
        base_info.faxingriqi = item["faxingriqi"]
        base_info.shangshiriqi = item["shangshiriqi"]
        base_info.shangshijiaoyisuo = item["shangshijiaoyisuo"]
        base_info.zhengquanleixing = item["zhengquanleixing"]
        base_info.liutongguben = item["liutongguben"]
        base_info.zongguben = item["zongguben"]
        base_info.zhuchengxiaoshang = item["zhuchengxiaoshang"]
        base_info.faxingjia = item["faxingjia"]
        base_info.shangshisourikaipanjia = item["shangshisourikaipanjia"]
        base_info.shangshishourizhangdiefu = item["shangshishourizhangdiefu"]
        base_info.shangshishourihuanshoulv = item["shangshishourihuanshoulv"]
        base_info.tebiechulihetuishi = item["tebiechulihetuishi"]
        base_info.faxingshiyinglv = item["faxingshiyinglv"]
        base_info.zuixinshiyinglv = item["zuixinshiyinglv"]

        # 公司简介-工商信息
        base_info.zhuceziben = item["zhuceziben"]
        base_info.zhucedizhi = item["zhucedizhi"]
        base_info.suodeisuilv = item["suodeisuilv"]
        base_info.bangongdizhi = item["bangongdizhi"]
        base_info.zhuyaochanpin = item["zhuyaochanpin"]

        # 公司简介-联系方式
        base_info.lianxidianhua = item["lianxidianhua"]
        base_info.gongsichuanzhen = item["gongsichuanzhen"]
        base_info.dianziyouxiang = item["dianziyouxiang"]
        base_info.gongsiwangzhi = item["gongsiwangzhi"]
        base_info.lianxiren = item["lianxiren"]
        base_info.youzhengbianma = item["youzhengbianma"]

        base_info.jingyingfanwei = item["jingyingfanwei"]

        base_info.gongsijianjie = item["gongsijianjie"]

        base_info.save()

    @classmethod
    def Save_Gaoguan_Info(self,  item):
        gaoguan_Info = Gaoguan_Info()

        gaoguan_Info.company_code = item["company_code"]
        # 高管-高管成员
        gaoguan_Info.dongjiangao = item["dongjiangao"]
        gaoguan_Info.gaoguanzhiwu = item["gaoguanzhiwu"]
        gaoguan_Info.renzhiriqi = item["renzhiriqi"]
        gaoguan_Info.lizhiriqi = item["lizhiriqi"]
        gaoguan_Info.xueli = item["xueli"]
        gaoguan_Info.nianxin = item["nianxin"]
        gaoguan_Info.chiguzonge = item["chiguzonge"]
        gaoguan_Info.chigushuliang = item["chigushuliang"]


        gaoguan_Info.save()

    @classmethod
    def Save_Dongshihui_Info(self,  item):
        dongshihui_Info = Dongshihui_Info()

        dongshihui_Info.company_code = item["company_code"]
        # 高管-高管成员
        dongshihui_Info.dongjiangao = item["dongjiangao"]
        dongshihui_Info.gaoguanzhiwu = item["gaoguanzhiwu"]
        dongshihui_Info.renzhiriqi = item["renzhiriqi"]
        dongshihui_Info.lizhiriqi = item["lizhiriqi"]
        dongshihui_Info.xueli = item["xueli"]
        dongshihui_Info.nianxin = item["nianxin"]
        dongshihui_Info.chiguzonge = item["chiguzonge"]
        dongshihui_Info.chigushuliang = item["chigushuliang"]

        dongshihui_Info.save()

    @classmethod
    def Save_Jianshihui_Info(self,  item):
        jianshihui_Info = Jianshihui_Info()

        jianshihui_Info.company_code = item["company_code"]
        # 高管-监事
        jianshihui_Info.dongjiangao = item["dongjiangao"]
        jianshihui_Info.gaoguanzhiwu = item["gaoguanzhiwu"]
        jianshihui_Info.renzhiriqi = item["renzhiriqi"]
        jianshihui_Info.lizhiriqi = item["lizhiriqi"]
        jianshihui_Info.xueli = item["xueli"]
        jianshihui_Info.nianxin = item["nianxin"]
        jianshihui_Info.chiguzonge = item["chiguzonge"]
        jianshihui_Info.chigushuliang = item["chigushuliang"]

        jianshihui_Info.save()



    @classmethod
    def Save_Fenhong_Info(self,  item):
        fenhong_Info = Fenhong_Info()

        fenhong_Info.company_code = item["company_code"]
        # 分红、历年分红详表
        fenhong_Info.gonggaoshijian = item["gonggaoshijian"]
        fenhong_Info.kuaijiniandu = item["kuaijiniandu"]
        fenhong_Info.songgu = item["songgu"]
        fenhong_Info.paixi = item["paixi"]
        fenhong_Info.guquandengjiri = item["guquandengjiri"]
        fenhong_Info.guquanchuxiri = item["guquanchuxiri"]
        fenhong_Info.honggushangshiri = item["honggushangshiri"]
        fenhong_Info.shifoshisi = item["shifoshisi"]
        fenhong_Info.xiangqing = item["xiangqing"]
        fenhong_Info.save()

    @classmethod
    def Save_Fenhong_Zhuanzeng_Info(self,  item):
        fenhong_Zhuanzeng_Info = Fenhong_Zhuanzeng_Info()

        fenhong_Zhuanzeng_Info.company_code = item["company_code"]
        # 分红、转增股本
        fenhong_Zhuanzeng_Info.gonggaoshijian = item["gonggaoshijian"]
        fenhong_Zhuanzeng_Info.zhuanzeng = item["zhuanzeng"]
        fenhong_Zhuanzeng_Info.chuquanchuxiri = item["chuquanchuxiri"]
        fenhong_Zhuanzeng_Info.chuquandengjiri = item["chuquandengjiri"]
        fenhong_Zhuanzeng_Info.zhuanzenggushangshiri = item["zhuanzenggushangshiri"]
        fenhong_Zhuanzeng_Info.tongqisonggu = item["tongqisonggu"]
        fenhong_Zhuanzeng_Info.fanganjianjie = item["fanganjianjie"]
        fenhong_Zhuanzeng_Info.shifoshisi = item["shifoshisi"]
        fenhong_Zhuanzeng_Info.xiangqing = item["xiangqing"]

        fenhong_Zhuanzeng_Info.save()

    @classmethod
    def Save_Fenhong_Peigu_Info(self,  item):
        fenhong_Peigu_Info = Fenhong_Peigu_Info()

        fenhong_Peigu_Info.company_code = item["company_code"]
        # 分红、配 股
        fenhong_Peigu_Info.gonggaoshijian = item["gonggaoshijian"]
        fenhong_Peigu_Info.peigufangan = item["peigufangan"]
        fenhong_Peigu_Info.peigujia = item["peigujia"]
        fenhong_Peigu_Info.jizhunguben = item["jizhunguben"]
        fenhong_Peigu_Info.chuquanri = item["chuquanri"]
        fenhong_Peigu_Info.guquandengjiri = item["guquandengjiri"]
        fenhong_Peigu_Info.jiaokuanqishiri = item["jiaokuanqishiri"]
        fenhong_Peigu_Info.jiaokuanzhongzhiri = item["jiaokuanzhongzhiri"]
        fenhong_Peigu_Info.peigushangshiri = item["peigushangshiri"]
        fenhong_Peigu_Info.mujizijin = item["mujizijin"]
        fenhong_Peigu_Info.xiangqing = item["xiangqing"]
        fenhong_Peigu_Info.save()

    @classmethod
    def Save_Fenhong_Huigou_Info(self,  item):
        fenhong_Huigou_Info = Fenhong_Huigou_Info()

        fenhong_Huigou_Info.company_code = item["company_code"]
        # 分红、回 购
        fenhong_Huigou_Info.gonggaoshijian = item["gonggaoshijian"]
        fenhong_Huigou_Info.huigouzanzonggubenbili = item["huigouzanzonggubenbili"]
        fenhong_Huigou_Info.huigougushu = item["huigougushu"]
        fenhong_Huigou_Info.nihuigoujiage = item["nihuigoujiage"]
        fenhong_Huigou_Info.gonggaoqianrigujia = item["gonggaoqianrigujia"]
        fenhong_Huigou_Info.goumaizuigaojia = item["goumaizuigaojia"]
        fenhong_Huigou_Info.goumaizuidijia = item["goumaizuidijia"]
        fenhong_Huigou_Info.huigouzongjine = item["huigouzongjine"]
        fenhong_Huigou_Info.shifoshisi = item["shifoshisi"]
        fenhong_Huigou_Info.xiangqing = item["xiangqing"]
        fenhong_Huigou_Info.save()

    @classmethod
    def Showrufenbu_Info(self, item):
        showrufenbu_Info = Showrufenbu_Info()
        showrufenbu_Info.company_code = item["company_code"]
        # 收入分布
        showrufenbu_Info.leibiemingcheng = item["leibiemingcheng"]
        showrufenbu_Info.yinyeshouru = item["yinyeshouru"]
        showrufenbu_Info.zhanyinyeshourubili = item["zhanyinyeshourubili"]
        showrufenbu_Info.yinyechengben = item["yinyechengben"]
        showrufenbu_Info.zhanchengbenbili = item["zhanchengbenbili"]
        showrufenbu_Info.yingyelirun = item["yingyelirun"]
        showrufenbu_Info.zhanlirunbili = item["zhanlirunbili"]
        showrufenbu_Info.maolilv =item["maolilv"]

        showrufenbu_Info.save()



    @classmethod
    def Search_ID(self, id):

        if id == 0:
            aa = Companys.objects.all()
            # print "ID == 0"
        else:
            aa = Companys.objects.filter(id__gte=id)
            print "ID != 0"
        return aa



