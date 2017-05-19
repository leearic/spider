#!/usr/bin/env python
#coding:utf-8
"""
  Author:  'Aric'
  Purpose: u'Bossproxy的方法和函数'
  Created: '2015/7/13'
"""
from django.http import  HttpResponse
import hashlib
import baixihecom.settings as sts
import httplib,urllib
import  xml.etree.ElementTree as ET

class DO_proxy(object):
    @staticmethod
    def CheckSignature(request):
        token =  sts.TOKEN
        signature = request.GET.get("signature", '')
        timestamp = request.GET.get("timestamp", '')
        nonce = request.GET.get("nonce", '')
        echoStr = request.GET.get("echostr", '')
        tmp_str = hashlib.sha1(''.join(sorted([token, timestamp, nonce]))).hexdigest()
        if tmp_str == signature:
            return HttpResponse(echoStr)
        else:
            return HttpResponse((u"禁止访问".encode('gbk')))

    @staticmethod
    def Msg_Gateway(request):
        url = sts.MONSTER_URL
        host = sts.MONSTER_HOST
        fromUserName, toUserName, msgType, content = _Get_xml_data(request)
        content.encode('gbk')
        url = url+"?FromUser="+ fromUserName +"&toUserName="+toUserName+"&msgType="+msgType+"&content="+content
        conn = httplib.HTTPConnection(host)
        conn.request(method='GET', url=url)

        res = conn.getresponse()
        reply = res.read()
        return HttpResponse(reply)
def _Get_xml_data(req):
    xml_str = req.body
    myxml = ET.fromstring(xml_str)
    content = myxml.find('Content').text
    content = content.encode('utf-8')
    msgType = myxml.find('MsgType').text
    fromUserName = myxml.find('FromUserName').text
    toUserName = myxml.find('ToUserName').text
    createTime = myxml.find('CreateTime').text
    return  fromUserName, toUserName, msgType, content