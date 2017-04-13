#-*- coding: utf-8 -*-


import sys, os
from szsti.settings import djpath
if djpath not in sys.path:
    sys.path.append(djpath)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_sz.settings")
django.setup()
from hightech.models import HightechInfo, Unit_Base_Info, Unit_Base_Info_Shareholder_Info, Unit_Base_Info_Changed_Info, Unit_annual_reports_Base_Info, Unit_annual_reports_Website_Info, Unit_annual_Promoters_and_reports_investment_Info, IDC_Base_Info, Itjuzi_Company_Info, Gao_Company_Info

class DjORM(object):

    #--------------------------------------------------------------
    #   以下数据来自： szsti.gov.cn
    #--------------------------------------------------------------

    @classmethod
    def save_hightechInfo(self, item):
        # 企业信息  szsti.gov.cn
        hightechInfo = HightechInfo()
        try:
            hightechInfo.number = item['number']  #private key
            hightechInfo.KeyID = item['KeyID']
            hightechInfo.Unit_name = item['Unit_name']
            hightechInfo.address = item['address']
            hightechInfo.Subordinate_Domain = item['Subordinate_Domain']
            hightechInfo.type = item['type']

            hightechInfo.save()

        except Exception:
            # 这有报错信息，将这个URL留下来以后单独处理
            print  "error================"
            pass

        # --------------------------------------------------------------
        #   以下数据来自： http://dian.idcquan.com
        # --------------------------------------------------------------
    @classmethod
    def save_IDC_Base_Info(self, item):
        idc_Base_Info = IDC_Base_Info()
        try:
           idc_Base_Info.url = item['url']
           idc_Base_Info.name = item['name']
           idc_Base_Info.company = item['company']
           idc_Base_Info.zone = item['zone']
           idc_Base_Info.address = item['address']
           idc_Base_Info.phone_number = item['phone_number']
           idc_Base_Info.website = item['website']
           idc_Base_Info.Main_business = item['Main_business']
           idc_Base_Info.Satisfaction = item['Satisfaction']

           idc_Base_Info.QQ = item['qq']

           idc_Base_Info.save()

        except Exception as e:
            # print e
            print  "...save IDC Base INFO Error ..."
            # print "___________________________________"
            pass




    #--------------------------------------------------------------
    #   以下数据来自： qichachca.com
    #--------------------------------------------------------------
    @classmethod
    def save_Unit_Base_Info(self, item):
        # 企业基础信息
        unit_Base_Info = Unit_Base_Info()
        try:
            # 企业详细信息-1
            unit_Base_Info.searching_name = item['searching_name']
            unit_Base_Info.searched_name = item['searched_name']



            unit_Base_Info.phone_nunber = item['phone_nunber']
            # unit_Base_Info.email = item['email']
            # unit_Base_Info.website = item['website']
            # unit_Base_Info.address = item['address']
            # 　企业工商信息
            unit_Base_Info.code = item['code']
            unit_Base_Info.Registration_number = item['Registration_number']
            unit_Base_Info.Organization_code = item['Organization_code']
            unit_Base_Info.Operating_state = item['Operating_state']
            unit_Base_Info.Legal_representative = item['Legal_representative']
            unit_Base_Info.registered_capital = item['registered_capital']
            unit_Base_Info.Company_type = item['Company_type']
            unit_Base_Info.date_of_establishment = item['date_of_establishment']
            unit_Base_Info.Operating_period = item['Operating_period']
            unit_Base_Info.registration_authority = item['registration_authority']
            unit_Base_Info.Date_of_issue = item['Date_of_issue']
            unit_Base_Info.company_size = item['company_size']
            unit_Base_Info.Subordinate_industry = item['Subordinate_industry']
            unit_Base_Info.English_name = item['English_name']
            unit_Base_Info.Name_used_Before = item['Name_used_Before']
            unit_Base_Info.Enterprise_address = item['Enterprise_address']
            unit_Base_Info.Business_scope = item['Business_scope']

            unit_Base_Info.save()

        except Exception:
            # 这有报错信息，将这个URL留下来以后单独处理
            print  "error================"
            pass


    @classmethod
    def save_Unit_Base_Info_Shareholder_Info(self, item):
        # 股东信息
        unit_Base_Info_Shareholder_Info = Unit_Base_Info_Shareholder_Info()
        try:
            unit_Base_Info_Shareholder_Info.searching_name = item['searching_name']
            unit_Base_Info_Shareholder_Info.searched_name = item['searched_name']



            unit_Base_Info_Shareholder_Info.Shareholder = item['Shareholder']
            unit_Base_Info_Shareholder_Info.Shareholding_ratio = item['Shareholding_ratio']
            unit_Base_Info_Shareholder_Info.Subscribed_capital_contribution = item['Subscribed_capital_contribution']
            unit_Base_Info_Shareholder_Info.Subscription_Date = item['Subscription_Date']
            unit_Base_Info_Shareholder_Info.Shareholder_type = item['Shareholder_type']
            unit_Base_Info_Shareholder_Info.save()

        except Exception:
            # 这有报错信息，将这个URL留下来以后单独处理
            print  "error================"
            pass

    @classmethod
    def save_Unit_Base_Info_Changed_Info(self, item):
        # 变更信息
        unit_Base_Info_Changed_Info = Unit_Base_Info_Changed_Info()
        try:
            unit_Base_Info_Changed_Info.searching_name = item['searching_name']
            unit_Base_Info_Changed_Info.searched_name = item['searched_name']

            unit_Base_Info_Changed_Info.Change_date = item['Change_date']
            unit_Base_Info_Changed_Info.Change_item = item['Change_item']
            unit_Base_Info_Changed_Info.Before_change = item['Before_change']
            unit_Base_Info_Changed_Info.After_change = item['After_change']
            unit_Base_Info_Changed_Info.save()

        except Exception:
            # 这有报错信息，将这个URL留下来以后单独处理
            print  "error================"
            pass

    @classmethod
    def save_Unit_annual_reports_Base_Info(self, item):
        # 企业年报-企业基本信息
        unit_annual_reports_Base_Info = Unit_annual_reports_Base_Info()
        try:
            unit_annual_reports_Base_Info.searching_name = item['searching_name']
            unit_annual_reports_Base_Info.searched_name = item['searched_name']

            unit_annual_reports_Base_Info.Registration_number = item['Registration_number']
            unit_annual_reports_Base_Info.Business_state = item['Business_state']
            unit_annual_reports_Base_Info.Enterprise_telephone = item['Enterprise_telephone']
            unit_annual_reports_Base_Info.Email = item['Email']
            unit_annual_reports_Base_Info.Postcode = item['Postcode']
            unit_annual_reports_Base_Info.number_of_people_engaged = item['number_of_people_engaged']
            unit_annual_reports_Base_Info.residence = item['residence']
            unit_annual_reports_Base_Info.transfer_of_shareholder_equity = item['transfer_of_shareholder_equity']
            unit_annual_reports_Base_Info.investment_Info = item['investment_Info']
            unit_annual_reports_Base_Info.save()

        except Exception:
            # 这有报错信息，将这个URL留下来以后单独处理
            print  "error================"
            pass

    @classmethod
    def save_Unit_annual_reports_Website_Info(self, item):
        # 企业年报-网站或网店信息
        unit_annual_reports_Website_Info = Unit_annual_reports_Website_Info()
        try:
            unit_annual_reports_Website_Info.searching_name = item['searching_name']
            unit_annual_reports_Website_Info.searched_name = item['searched_name']
            unit_annual_reports_Website_Info.Web_Type = item['Web_Type']
            unit_annual_reports_Website_Info.Web_Name = item['Web_Name']
            unit_annual_reports_Website_Info.Web_Site = item['Web_Site']
            unit_annual_reports_Website_Info.save()

        except Exception:
            # 这有报错信息，将这个URL留下来以后单独处理
            print  "error================"
            pass


    @classmethod
    def save_Unit_annual_Promoters_and_reports_investment_Info(self, item):
        # 企业年报-发起人及出资信息
        unit_annual_Promoters_and_reports_investment_Info = Unit_annual_Promoters_and_reports_investment_Info()
        try:
            unit_annual_Promoters_and_reports_investment_Info.searching_name = item['searching_name']
            unit_annual_Promoters_and_reports_investment_Info.searched_name = item['searched_name']



            unit_annual_Promoters_and_reports_investment_Info.Sponsor =item['Sponsor']
            unit_annual_Promoters_and_reports_investment_Info.Subscribed_capital_contribution = item['Subscribed_capital_contribution']
            unit_annual_Promoters_and_reports_investment_Info.Time_of_subscription =item['Time_of_subscription']
            unit_annual_Promoters_and_reports_investment_Info.Subscribed_capital_contribution = item['Subscribed_capital_contribution']
            unit_annual_Promoters_and_reports_investment_Info.Paid_in_capital_contribution = item['Paid_in_capital_contribution']
            unit_annual_Promoters_and_reports_investment_Info.Investment_time = item['Investment_time']
            unit_annual_Promoters_and_reports_investment_Info. Investment_method = item['Investment_method']

            unit_annual_Promoters_and_reports_investment_Info.save()

        except Exception:
            # 这有报错信息，将这个URL留下来以后单独处理
            print  "error================"
            pass



    @classmethod
    def save_info_For_Miss_Gao(self, item):
        # 企业年报-发起人及出资信息
        gao_Company_Info = Gao_Company_Info()
        try:
            gao_Company_Info.phone_nunber = item["phone_nunber"]
            gao_Company_Info.Enterprise_address = item["Enterprise_address"]
            gao_Company_Info.company_name = item["company_name"]
            gao_Company_Info.Legal_representative = item["Legal_representative"]
            gao_Company_Info.Business_scope = item["Business_scope"]
            gao_Company_Info.status = item["status"]
            gao_Company_Info.category = item["category"]

            gao_Company_Info.save()


        except Exception:
            # 这有报错信息，将这个URL留下来以后单独处理
            print  " = save info error ="
            pass

















    @classmethod
    def query(self, Number):
        if Number == 0:
            aa = HightechInfo.objects.all()
            # print "ID == 0"

        else:
            aa = HightechInfo.objects.filter(id__gte=Number)
            # print "ID != 0"
        return aa

    @classmethod
    def query_itjuzi(self, Number):
        if Number == 0:
            aa = Itjuzi_Company_Info.objects.all()
            # print "ID == 0"

        else:
            aa = Itjuzi_Company_Info.objects.filter(id__lte=Number)
            # print "ID != 0"
        return aa
