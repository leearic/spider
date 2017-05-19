from hr.utils.lagou.Save_2_DB import lagou_DB

class lagou_Analysis(object):

    @classmethod
    def Analysis_Position_Info(self, response, searching_company):

        self.item = {}
        try:
            self.item["searching_company"] = [searching_company]

            self.item["searched_company"] = response.xpath('//*[@id="job_company"]/dt/a/div/h2/text()').extract()
            self.item["bumen"] = response.xpath('/html/body/div[3]/div/div[1]/div/div[1]/text()').extract()
            self.item["zhiwei"] =response.xpath("/html/body/div[3]/div/div[1]/div/span/text()").extract()

            self.item["yaoqiu"] = response.xpath('/html/body/div[3]/div/div[1]/dd/p[1]').extract()
            self.item["fabushijian"] = response.xpath('/html/body/div[3]/div/div[1]/dd/p[2]/text()').extract()
            self.item["zhiweiyouhuo"] = response.xpath('//*[@id="job_detail"]/dd[1]/p/text()').extract()
            self.item["zhiweimiaoshu"] = response.xpath('//*[@id="job_detail"]/dd[2]/div').extract()
            self.item["gongzuodidian"] = response.xpath('//*[@id="job_detail"]/dd[3]/div[1]').extract()

            self.item["fabuzhe"] = response.xpath('//*[@id="job_detail"]/dd[4]/div/div[1]/a/span[1]/text()').extract()

            for i in self.item:
                self.item[i] = self.item[i][0].strip()

            lagou_DB.Save_Position_Info(self.item)
            print "Save Position Info ok...."
        except:
            pass