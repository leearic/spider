#!/usr/bin/env python
#coding:utf-8
"""
  Author:  'Aric'
  Purpose: ''
  Created: '2015/7/24'
"""
from qiushibaike import settings
import  MySQLdb

class  SQL_Conn():

    def __init__(self):
        try:
            self.connection =  MySQLdb.connect( host = settings.DB_HOST , user = settings.DB_USER, passwd = settings.DB_PASSWD, db = settings.DB_NAME, charset="utf8")
        except Exception, e:
            print  e

    def save(self, item):
        cursor = self.connection.cursor()

        sql = "insert into qiubai_qiushi (user_image, user_name, content, thumb, video_image, video, laugh, coments, played) values  (\'" + item["user_image"][0] + "\', \'" + item["user_name"] + "\', \'" + item["content"] + "\', \'" + item["thumb"][0] + "\', \'" + item["video_image"] + "\', \'" + item["video"]  + "\', \'" + item["laugh"]  + "\', \'" +  item["coments"]  + "\', \'" + item["played"] + "\')"
        try:
            cursor.execute(sql)
            self.connection.commit()
        except Exception, e:
            print e
        self.connection.rollback()
        print "insert into sql :" + item["user_name"]
        cursor.close()

    def test(self):
        cursor = self.connection.cursor()
        cursor.execute('select * from qiubai_qiushi')

    def __del__(self):
        self.connection.close()


if __name__ == '__main__':
    # print sys.path
    aa = SQL_Conn()
    aa.test()