# -*- coding: utf-8 -*-


from szsti.hexunutils.Save_2_DB import Hexun


class hexun_Analysis(object):

    @classmethod
    def BaseInfo(self, response, id):
        self.item = {}

        self.item["company_code"] = id
        # 公司简介-基本信息
        try:
            self.item["name"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[1]/table/tbody/tr[1]/td[2]/text()').extract()[0]
        except:
            self.item["name"] = '-'
        try:
            self.item[
            "daima"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[1]/table/tbody/tr[2]/td[2]/text()').extract()[0]
        except:
            self.item["daima"] = '-'
        try:
            self.item[
            "quancheng"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[1]/table/tbody/tr[3]/td[2]/text()').extract()[0]
        except:
            self.item["quancheng"] = '-'
        try:
            self.item[
            "Englishname"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[1]/table/tbody/tr[4]/td[2]/text()').extract()[0]
        except:
            self.item["Englishname"] = '-'
        try:
            self.item[
            "cengyongming"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[1]/table/tbody/tr[5]/td[2]/text()').extract()[0]
        except:
            self.item["cengyongming"] = '-'
        try:
            self.item[
            "chengliriqi"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[1]/table/tbody/tr[6]/td[2]/a/text()').extract()[0]
        except:
            self.item["chengliriqi"] = '-'
        try:
            self.item[
            "suoshuhangye"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[1]/table/tbody/tr[7]/td[2]/a/text()').extract()[0]
        except:
            self.item["suoshuhangye"] = '-'
        try:
            self.item[
            "suoshugannian"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[1]/table/tbody/tr[8]/td[2]/a/text()').extract()[0]
        except:
            self.item["suoshugannian"] = '-'
        try:
            self.item[
            "suoshudiyu"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[1]/table/tbody/tr[9]/td[2]/a/text()').extract()[0]
        except:
            self.item["suoshudiyu"] = '-'
        try:
            self.item[
            "fadingdabiaoren"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[1]/table/tbody/tr[10]/td[2]/text()').extract()[0]
        except:
            self.item["fadingdabiaoren"] = '-'
        try:
            self.item[
            "dulidongshi"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[1]/table/tbody/tr[11]/td[2]/text()').extract()[0]
        except:
            self.item["dulidongshi"] = '-'
        try:
            self.item[
            "zixunfuwujigou"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[1]/table/tbody/tr[12]/td[2]/text()').extract()[0]
        except:
            self.item["zixunfuwujigou"] = '-'
        try:
            self.item[
            "kuaijishiwusuo"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[1]/table/tbody/tr[13]/td[2]/text()').extract()[0]
        except:
            self.item["kuaijishiwusuo"] = '-'
        try:
            self.item[
            "zhengquanshifudaibiao"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[1]/table/tbody/tr[14]/td[2]/text()').extract()[0]
        # 公司简介-证券信息
        except:
            self.item["zhengquanshifudaibiao"] = '-'
        try:
            self.item[
            "faxingriqi"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[1]/table/tbody/tr[1]/td[2]/text()').extract()[0]
        except:
            self.item["faxingriqi"] = " - "

        try:
            self.item[
            "shangshiriqi"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[1]/table/tbody/tr[2]/td[2]/text()').extract()[0]
        except:
            self.item["shangshiriqi"] = '-'
        try:
            self.item[
            "shangshijiaoyisuo"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[1]/table/tbody/tr[3]/td[2]/a/text()').extract()[0]
        except:
            self.item["shangshijiaoyisuo"] = '-'
        try:
            self.item[
            "zhengquanleixing"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[1]/table/tbody/tr[4]/td[2]/text()').extract()[0]
        except:
            self.item["zhengquanleixing"] = '-'
        try:
            self.item[
            "liutongguben"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[1]/table/tbody/tr[5]/td[2]/a/text()').extract()[0]
        except:
            self.item["liutongguben"] = '-'
        try:
            self.item[
            "zongguben"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[1]/table/tbody/tr[6]/td[2]/a/text()').extract()[0]
        except:
            self.item["zongguben"] = '-'
        try:
            self.item[
            "zhuchengxiaoshang"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[1]/table/tbody/tr[7]/td[2]/a/text()').extract()[0]
        except:
            self.item["zhuchengxiaoshang"] = '-'
        try:
            self.item[
            "faxingjia"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[1]/table/tbody/tr[8]/td[2]/a/text()').extract()[0]
        except:
            self.item["faxingjia"] = '-'
        try:
            self.item[
            "shangshisourikaipanjia"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[1]/table/tbody/tr[9]/td[2]/a/text()').extract()[0]
        except:
            self.item["shangshisourikaipanjia"] = '-'
        try:
            self.item[
            "shangshishourizhangdiefu"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[1]/table/tbody/tr[10]/td[2]/text()').extract()[0]
        except:
            self.item["shangshishourizhangdiefu"] = '-'
        try:
            self.item[
            "shangshishourihuanshoulv"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[1]/table/tbody/tr[11]/td[2]/text()').extract()[0]
        except:
            self.item["shangshishourihuanshoulv"] = '-'
        try:
            self.item[
            "tebiechulihetuishi"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[1]/table/tbody/tr[12]/td[2]/text()').extract()[0]
        except:
            self.item["tebiechulihetuishi"] = '-'
        try:
            self.item[
            "faxingshiyinglv"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[1]/table/tbody/tr[13]/td[2]/text()').extract()[0]
        except:
            self.item["faxingshiyinglv"] = '-'
        try:
            self.item[
            "zuixinshiyinglv"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[1]/table/tbody/tr[14]/td[2]/a/text()').extract()[0]
        except:
            self.item["zuixinshiyinglv"] = '-'
        # 公司简介-工商信息
        try:
            self.item[
            "zhuceziben"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[2]/table/tbody/tr[1]/td[2]/a/text()').extract()[0]
        except:
            self.item["zhuceziben"] = '-'
        try:
            self.item[
            "zhucedizhi"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[2]/table/tbody/tr[2]/td[2]/text()').extract()[0]
        except:
            self.item["zhucedizhi"] = '-'
        try:
            self.item[
            "suodeisuilv"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[2]/table/tbody/tr[3]/td[2]/a/text()').extract()[0]
        except:
            self.item["suodeisuilv"] = '-'
        try:
            self.item[
            "bangongdizhi"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[2]/table/tbody/tr[4]/td[2]/text()').extract()[0]
        except:
            self.item["bangongdizhi"] = '-'
        try:
            self.item[
            "zhuyaochanpin"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[2]/table/tbody/tr[5]/td[2]/text()').extract()[0]

        # 公司简介-联系方式
        except:
            self.item["zhuyaochanpin"] = '-'
        try:
            self.item[
            "lianxidianhua"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[2]/table/tbody/tr[1]/td[2]/text()').extract()[0]
        except:
            self.item["lianxidianhua"] = '-'
        try:
            self.item[
            "gongsichuanzhen"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[2]/table/tbody/tr[2]/td[2]/text()').extract()[0]
        except:
            self.item["gongsichuanzhen"] = '-'
        try:
            self.item[
            "dianziyouxiang"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[2]/table/tbody/tr[3]/td[2]/a/text()').extract()[0]
        except:
            self.item["dianziyouxiang"] = '-'
        try:
            self.item[
            "gongsiwangzhi"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[2]/table/tbody/tr[4]/td[2]/a/text()').extract()[0]
        except:
            self.item["gongsiwangzhi"] = '-'
        try:
            self.item[
            "lianxiren"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[2]/table/tbody/tr[5]/td[2]/text()').extract()[0]
        except:
            self.item["jingyingfanwei"] = '-'
        try:
            self.item[
            "youzhengbianma"] = response.xpath('/html/body/div[5]/div[8]/div[2]/div[2]/table/tbody/tr[6]/td[2]/text()').extract()[0]
        except:
            self.item["lianxiren"] = '-'
        try:
            self.item["jingyingfanwei"] = response.xpath('/html/body/div[5]/div[8]/div[1]/div[3]/p/text()').extract()[0]
        except:
            self.item["jingyingfanwei"] = '-'
        try:
            self.item["gongsijianjie"]= response.xpath('/html/body/div[5]/div[8]/div[2]/div[3]/p/text()').extract()[0]
        except:
            self.item["gongsijianjie"] = '-'

        for i in self.item:
            try:
                self.item[i] = self.item[i].strip()

            except Exception:
                print "BaseInfo error"
                pass

        Hexun.Save_Base_Info(self.item)

        print "* BaseInfo *"

    @classmethod
    def Gaoguan_Info(self, response, id):
        self.item = {}
        self.item["company_code"] = id

        gaoguan_table = response.xpath('//*[@id="gkaTable"]/table/tbody/tr')
        for gaoguan in gaoguan_table:
            try:
                # 高管-监事会成员
                self.item["dongjiangao"] = gaoguan.xpath('td[1]/a/text()').extract()[0]
                self.item["gaoguanzhiwu"] = gaoguan.xpath('td[2]/text()').extract()[0]
                self.item["renzhiriqi"] = gaoguan.xpath('td[3]/text()').extract()[0]
                self.item["lizhiriqi"] =  gaoguan.xpath('td[4]/text()').extract()[0]
                self.item["xueli"] =  gaoguan.xpath('td[5]/text()').extract()[0]
                self.item["nianxin"] =  gaoguan.xpath('td[6]/text()').extract()[0]
                self.item["chiguzonge"] =  gaoguan.xpath('td[7]/text()').extract()[0]
                self.item["chigushuliang"] =  gaoguan.xpath('td[8]/text()').extract()[0]

                Hexun.Save_Gaoguan_Info(self.item)
                print u'高管保存成功'
            except:
                pass



    @classmethod
    def Dongshi_Info(self, response, id):
        self.item = {}
        self.item["company_code"] = id

        dongshi_table = response.xpath('//*[@id="gkbTable"]/table/tbody/tr')
        for dongshi in dongshi_table:
            try:
                # 高管-监事会成员
                self.item["dongjiangao"] = dongshi.xpath('td[1]/a/text()').extract()[0]
                self.item["gaoguanzhiwu"] = dongshi.xpath('td[2]/text()').extract()[0]
                self.item["renzhiriqi"] = dongshi.xpath('td[3]/text()').extract()[0]
                self.item["lizhiriqi"] =  dongshi.xpath('td[4]/text()').extract()[0]
                self.item["xueli"] =  dongshi.xpath('td[5]/text()').extract()[0]
                self.item["nianxin"] =  dongshi.xpath('td[6]/text()').extract()[0]
                self.item["chiguzonge"] =  dongshi.xpath('td[7]/text()').extract()[0]
                self.item["chigushuliang"] =  dongshi.xpath('td[8]/text()').extract()[0]

                Hexun.Save_Dongshihui_Info(self.item)
                print u'懂事保存成功'
            except:
                pass

    @classmethod
    def Jianshi_Info(self, response, id):
        self.item = {}
        self.item["company_code"] = id

        jianshi_table = response.xpath('//*[@id="gkcTable"]/table/tbody/tr')
        for jianshi in jianshi_table:
            try:
                # 高管-监事会成员
                self.item["dongjiangao"] = jianshi.xpath('td[1]/a/text()').extract()[0]
                self.item["gaoguanzhiwu"] = jianshi.xpath('td[2]/text()').extract()[0]
                self.item["renzhiriqi"] = jianshi.xpath('td[3]/text()').extract()[0]
                self.item["lizhiriqi"] = jianshi.xpath('td[4]/text()').extract()[0]
                self.item["xueli"] = jianshi.xpath('td[5]/text()').extract()[0]
                self.item["nianxin"] = jianshi.xpath('td[6]/text()').extract()[0]
                self.item["chiguzonge"] = jianshi.xpath('td[7]/text()').extract()[0]
                self.item["chigushuliang"] = jianshi.xpath('td[8]/text()').extract()[0]

                Hexun.Save_Jianshihui_Info(self.item)
                print u'监事保存成功'
            except:
                pass


    @classmethod
    def Fenhong_Info(self, response, id):
        self.item = {}
        self.item["company_code"] = id

        Fenhong_table = response.xpath('//*[@id="ldkplaTable"]/table/tbody/tr')

        for jianshi in Fenhong_table:
            try:
                # 高管-监事会成员
                self.item["gonggaoshijian"] = jianshi.xpath('td[1]/text()').extract()[0]
                self.item["kuaijiniandu"] = jianshi.xpath('td[2]/text()').extract()[0]
                self.item["songgu"] = jianshi.xpath('td[3]/text()').extract()[0]
                self.item["paixi"] = jianshi.xpath('td[4]/text()').extract()[0]
                self.item["guquandengjiri"] = jianshi.xpath('td[5]/text()').extract()[0]
                self.item["guquanchuxiri"] = jianshi.xpath('td[6]/text()').extract()[0]
                self.item["honggushangshiri"] = jianshi.xpath('td[7]/text()').extract()[0]
                self.item["shifoshisi"] = jianshi.xpath('td[8]/text()').extract()[0]
                self.item["xiangqing"] = jianshi.xpath('td[9]/a/@href').extract()[0]

                if self.item["gonggaoshijian"] == u"公告时间":
                    pass
                else:
                    Hexun.Save_Fenhong_Info(self.item)
                    print u"分红基本信息保存完毕..."
            except Exception as e:
                pass

    @classmethod
    def Fenhong_Zhuanzeng_Info(self, response, id):
        self.item = {}
        self.item["company_code"] = id
        Zhuanzeng_table = response.xpath('//*[@id="ldkplbTable"]/table/tbody/tr')
        for jianshi in Zhuanzeng_table:
            # 分红、转增股本
            try:
                self.item["gonggaoshijian"] = jianshi.xpath('td[1]/text()').extract()[0]
                self.item["zhuanzeng"] = jianshi.xpath('td[2]/text()').extract()[0]
                self.item["chuquanchuxiri"] = jianshi.xpath('td[3]/text()').extract()[0]
                self.item["chuquandengjiri"] = jianshi.xpath('td[4]/text()').extract()[0]
                #self.item["guquandengjiri"] = jianshi.xpath('td[5]/text()').extract()[0]
                self.item["zhuanzenggushangshiri"] = jianshi.xpath('td[5]/text()').extract()[0]
                self.item["tongqisonggu"] = jianshi.xpath('td[6]/text()').extract()[0]
                self.item["fanganjianjie"] = jianshi.xpath('td[7]/text()').extract()[0]
                self.item["shifoshisi"] = jianshi.xpath('td[8]/text()').extract()[0]
                self.item["xiangqing"] = jianshi.xpath('td[9]/a/@href').extract()[0]

                if self.item["gonggaoshijian"] == u"公告时间":
                    pass
                else:
                    Hexun.Save_Fenhong_Zhuanzeng_Info(self.item)
                    print u"分红-转增股本-信息保存完毕..."
            except:
                pass

    @classmethod
    def Fenhong_Peigu_Info(self, response, id):
        self.item = {}
        self.item["company_code"] = id

        jianshi_table = response.xpath('//*[@id="ldkplcTable"]/table/tbody/tr')
        for jianshi in jianshi_table:
            # 分红、配 股
            try:
                self.item["gonggaoshijian"] = jianshi.xpath('td[1]/text()').extract()[0]
                self.item["peigufangan"] = jianshi.xpath('td[2]/text()').extract()[0]
                self.item["peigujia"] = jianshi.xpath('td[3]/text()').extract()[0]
                self.item["jizhunguben"] = jianshi.xpath('td[4]/text()').extract()[0]
                self.item["chuquanri"] = jianshi.xpath('td[5]/text()').extract()[0]
                self.item["guquandengjiri"] = jianshi.xpath('td[6]/text()').extract()[0]
                self.item["jiaokuanqishiri"] = jianshi.xpath('td[7]/text()').extract()[0]
                self.item["jiaokuanzhongzhiri"] = jianshi.xpath('td[8]/text()').extract()[0]
                self.item["peigushangshiri"] = jianshi.xpath('td[9]/text()').extract()[0]
                self.item["mujizijin"] = jianshi.xpath('td[10]/text()').extract()[0]
                self.item["xiangqing"] = jianshi.xpath('td[11]/a/@href').extract()[0]

                if self.item["gonggaoshijian"] == u"公告时间":
                    pass
                else:
                    Hexun.Save_Fenhong_Peigu_Info(self.item)
                    print u"分红-配股-信息保存完毕..."
            except:
                pass


                #
    @classmethod
    def Fenhong_Huigou_Info(self, response, id):
        self.item = {}
        self.item["company_code"] = id

        jianshi_table = response.xpath('//*[@id="hklTable"]/table/tbody/tr')
        for jianshi in jianshi_table:
            # 分红、回购
            try:
                self.item["gonggaoshijian"] = jianshi.xpath('td[1]/text()').extract()[0]
                self.item["huigouzanzonggubenbili"] = jianshi.xpath('td[2]/text()').extract()[0]
                self.item["huigougushu"] = jianshi.xpath('td[3]/text()').extract()[0]
                self.item["nihuigoujiage"] = jianshi.xpath('td[4]/text()').extract()[0]
                self.item["gonggaoqianrigujia"] = jianshi.xpath('td[5]/text()').extract()[0]
                self.item["goumaizuigaojia"] = jianshi.xpath('td[6]/text()').extract()[0]
                self.item["goumaizuidijia"] = jianshi.xpath('td[7]/text()').extract()[0]
                self.item["huigouzongjine"] = jianshi.xpath('td[8]/text()').extract()[0]
                self.item["shifoshisi"] = jianshi.xpath('td[9]/text()').extract()[0]
                self.item["xiangqing"] = jianshi.xpath('td[10]/a/@href').extract()[0]

                if self.item["gonggaoshijian"] == u"公告时间":
                    pass
                else:
                    Hexun.Save_Fenhong_Peigu_Info(self.item)
                    print u"分红融资-回购-信息保存完毕..."
            except:
                pass




    @classmethod
    def Showrufenbu_Info(self, response, id):

        self.item = {}
        self.item["company_code"] = id

        jianshi_table = response.xpath('//*[@id="histDealTablea"]/table/tbody/tr')
        for jianshi in jianshi_table:


            # print jianshi.extract()
            # print "*" * 30

            # 收入分布
            try:
                self.item["leibiemingcheng"] = jianshi.xpath('td[2]/text()').extract()[0]
                self.item["yinyeshouru"] = jianshi.xpath('td[3]/text()').extract()[0]
                self.item["zhanyinyeshourubili"] = jianshi.xpath('td[4]/text()').extract()[0]
                self.item["yinyechengben"] = jianshi.xpath('td[5]/text()').extract()[0]
                self.item["zhanchengbenbili"] = jianshi.xpath('td[6]/text()').extract()[0]
                self.item["yingyelirun"] = jianshi.xpath('td[7]/text()').extract()[0]
                self.item["zhanlirunbili"] = jianshi.xpath('td[8]/text()').extract()[0]
                self.item["maolilv"] = jianshi.xpath('td[9]/text()').extract()[0]

                if self.item["leibiemingcheng"] == u"类别名称":
                    pass
                else:
                    Hexun.Showrufenbu_Info(self.item)
                    print u"收入分布-信息保存完毕..."
            except Exception as e:
                print "& "* 30
                print e
                print "& " * 30
                pass







