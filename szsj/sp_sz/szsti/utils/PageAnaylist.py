# -*- coding: utf-8 -*-


from szsti.utils.Save2DB import DjORM


class qichachca(object):

    @classmethod
    def BaseInfo(self, response, number):
        self.item = {}
        self.item["searching_name"] = number
        self.item['searched_name'] = \
        response.xpath('//*[@id="company-top"]/div/div[1]/span[2]/span/span[1]/text()').extract()[0].strip()
        self.item["phone_nunber"] = response.xpath('//*[@id="company-top"]/div/div[1]/span[2]/small[1]/text()').extract()[0]
        self.item["code"] = response.xpath('//*[@id="Cominfo"]/table/tbody/tr[1]/td[2]/text()').extract()[0]

        self.item["Registration_number"] = response.xpath('//*[@id="Cominfo"]/table/tbody/tr[1]/td[4]/text()').extract()[0]


        self.item["Organization_code"] =  response.xpath('//*[@id="Cominfo"]/table/tbody/tr[2]/td[2]/text()').extract()[0]
        self.item["Operating_state"] = response.xpath('//*[@id="Cominfo"]/table/tbody/tr[2]/td[4]/text()').extract()[0]
        self.item["Legal_representative"] = response.xpath('//*[@id="Cominfo"]/table/tbody/tr[3]/td[2]/text()').extract()[0]
        self.item["registered_capital"] = response.xpath('//*[@id="Cominfo"]/table/tbody/tr[3]/td[4]/text()').extract()[0]
        self.item["Company_type"] = response.xpath('//*[@id="Cominfo"]/table/tbody/tr[4]/td[2]/text()').extract()[0]
        self.item["date_of_establishment"] = response.xpath('//*[@id="Cominfo"]/table/tbody/tr[4]/td[4]/text()').extract()[0]
        self.item["Operating_period"] = response.xpath('//*[@id="Cominfo"]/table/tbody/tr[5]/td[2]/text()').extract()[0]
        self.item["registration_authority"] = response.xpath('//*[@id="Cominfo"]/table/tbody/tr[5]/td[4]/text()').extract()[0]
        self.item["Date_of_issue"] = response.xpath('//*[@id="Cominfo"]/table/tbody/tr[6]/td[2]/text()').extract()[0]
        self.item["company_size"] = response.xpath('//*[@id="Cominfo"]/table/tbody/tr[6]/td[4]/text()').extract()[0]
        self.item["Subordinate_industry"] = response.xpath('//*[@id="Cominfo"]/table/tbody/tr[7]/td[2]/text()').extract()[0]
        self.item["English_name"] = response.xpath('//*[@id="Cominfo"]/table/tbody/tr[7]/td[4]/text()').extract()[0]
        self.item["Name_used_Before"] = response.xpath('//*[@id="Cominfo"]/table/tbody/tr[8]/td[2]/text()').extract()[0]
        self.item["Enterprise_address"] = response.xpath('//*[@id="Cominfo"]/table/tbody/tr[9]/td[2]/text()').extract()[0]
        self.item["Business_scope"] = response.xpath('//*[@id="Cominfo"]/table/tbody/tr[10]/td[2]/text()').extract()[0]


        for i in self.item:
            try:
                self.item[i] = self.item[i].strip()

            except Exception:
                print "BaseInfo error"
                pass

        DjORM.save_Unit_Base_Info(self.item)

        print "* BaseInfo *"



    @classmethod
    def  Unit_Base_Shareholder_Info(self, response, number):
        # 股东信息
        self.item = {}
        self.item["searching_name"] = number
        self.item['searched_name'] = \
        response.xpath('//*[@id="company-top"]/div/div[1]/span[2]/span/span[1]/text()').extract()[0].strip()
        tbody = response.xpath('//*[@id="Sockinfo"]/table/tbody/tr')

        for i in tbody:
            # print i.extract()
            try:
                self.item["Shareholder"]                     = i.xpath('td[1]/a[1]/text()').extract()[0]
                self.item["Shareholding_ratio"]              = i.xpath('td[2]/text()').extract()[0].strip()
                self.item["Subscribed_capital_contribution"] = i.xpath('td[3]/text()').extract()[0].strip()
                self.item["Subscription_Date"]               = i.xpath('td[4]/text()').extract()[0].strip()
                self.item["Shareholder_type"]                = i.xpath('td[5]/text()').extract()[0].strip()
            except Exception:
                print "Unit_Base_Shareholder_Info error"
                pass
        DjORM.save_Unit_Base_Info_Shareholder_Info(self.item)
        print "* Unit_Base_Shareholder_Info *"


    @classmethod
    def  Unit_Base_Changed_Info(self, response, number):
            # 变更信息
        self.item = {}
        self.item["searching_name"] = number

        self.item['searched_name'] = response.xpath('//*[@id="company-top"]/div/div[1]/span[2]/span/span[1]/text()').extract()[0].strip()
        tbody = response.xpath('//*[@id="Changelist"]/table/tbody/tr')

        for i in tbody:
            # print i.extract()
            try:
                self.item["Unit_id"] =  i.xpath('td[1]/text()').extract()[0]
                self.item["Change_date"] = i.xpath('td[2]/text()').extract()[0].strip()
                self.item["Change_item"] = i.xpath('td[3]/text()').extract()[0].strip()
                self.item["Before_change"] = i.xpath('td[4]/div/text()').extract()[0].strip()
                self.item["After_change"] = i.xpath('td[5]/div/text()').extract()[0].strip()
            except Exception as e:
                # print e
                print "Unit_Base_Changed_Info error "
                pass
        DjORM.save_Unit_Base_Info_Changed_Info(self.item)
        print "* Unit_Base_Changed_Info *"

    @classmethod
    def  Unit_annual_reports_Base_Info(self, response, number):
        # 企业年报-企业基本信息

        print u"Unit_annual_reports_Base_Info"
        self.item = {}
        self.item["searching_name"] = number

        self.item["Registration_number"] = response.xpath('//*[@id=u"2015年度报告"]/table[1]/tbody/tr[1]/td[2]/text()').extract()[0]
        self.item["Business_state"] = response.xpath('//*[@id=u"2015年度报告"]/table[1]/tbody/tr[1]/td[4]/text()').extract()[0]
        self.item["Enterprise_telephone"]  = response.xpath('//*[@id=u"2015年度报告"]/table[1]/tbody/tr[2]/td[2]/text()').extract()[0]
        self.item["Email"] = response.xpath('//*[@id=u"2015年度报告"]/table[1]/tbody/tr[2]/td[4]/a/text()').extract()[0]
        self.item["Postcode"]   = response.xpath('//*[@id=u"2015年度报告"]/table[1]/tbody/tr[3]/td[2]/text()').extract()[0]
        self.item["number_of_people_engaged"] = response.xpath('//*[@id="2015年度报告"]/table[1]/tbody/tr[3]/td[4]/text()').extract()[0]
        self.item["residence"] = response.xpath('//*[@id=u"2015年度报告"]/table[1]/tbody/tr[4]/td[2]/text()').extract()[0]
        self.item["transfer_of_shareholder_equity"]  = response.xpath('//*[@id=u"2015年度报告"]/table[1]/tbody/tr[5]/td[2]/text()').extract()[0]
        self.item["investment_Info"] = response.xpath('//*[@id=u"2015年度报告"]/table[1]/tbody/tr[5]/td[4]/text()').extract()[0]


        for i in self.item:
            try:
                self.item[i] = self.item[i].strip()

            except Exception:
                pass
        print "*" * 30


    @classmethod
    def  Miss_Gao_Info(self, response, category):
        # Miss Gao

        print "Miss Gao Info saving ．．．．"
        self.item = {}
        self.item["category"] = category


        tbody = response.xpath('//*[@id="searchlist"]/table/tbody/tr')


        for i in tbody:
            # print i.extract()
            # print "%" * 10
            try:
                allinfo =  i.xpath("td[2]").extract()[0]
                # print "================"
                # print  "category: " + category
                # print "================"

                try:
                    self.item["phone_nunber"] = allinfo.split("<br>")[2].strip()
                    print "phone_number" + allinfo.split("<br>")[2].strip()
                except:
                    self.item["phone_nunber"] = "-"

                try:
                    self.item["Enterprise_address"] = allinfo.split("<br>")[3].split("</td>")[0].strip()
                    print "Enterprise_address" + allinfo.split("<br>")[3].split("</td>")[0].strip()
                except:
                    self.item["Enterprise_address"] = "-"

                try:
                    self.item["company_name"] = i.xpath("td[2]/a/text()").extract()[0].strip()
                    print "company_name" + i.xpath("td[2]/a/text()").extract()[0].strip()
                except:
                    self.item["company_name"] = "-"

                try:
                    self.item["Legal_representative"] = allinfo.split("<br>")[1].strip()
                    print "Legal_representative: " + allinfo.split("<br>")[1].strip()
                except:
                    self.item["Legal_representative"] = "-"

                self.item["Business_scope"] = category

                try:
                    self.item["status"] = i.xpath('td/span[@class="ma_cbt_green m-l-xs"]/text()').extract()[0].strip()
                    print "status: " + i.xpath('td/span[@class="ma_cbt_green m-l-xs"]/text()').extract()[0].strip()
                except:
                    self.item["status"] = "-"

                self.item["category"] = category

                DjORM.save_info_For_Miss_Gao(self.item)

                # print "***" * 9
            except:
                print "---- page analysis  error -----"
                pass
