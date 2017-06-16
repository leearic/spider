#!/usr/bin/env python
#coding:utf-8
"""
  Author:  'Aric'
  Purpose: '接受用户发来的消息，并且返回相应的信息'
  Created: '2015/7/14'
"""
# from tempates import templates as temp
import time
class Message_Session(object):
    def __init__(self, data):
        self.msgType = data["msgType"]
        self.content = data["content"]
        self.FromUser = data["FromUser"]
        self.ToUser = data["toUserName"]
        if self.msgType == "text":
            pass
        if self.msgType == "image":
            print "this is a image method"
        if self.msgType == "voice":
            print "this is a voice method"
        if self.msgType == "video":
            print "this is a video method"
        if self.msgType == "shortvideo":
            print "this is a shortvideo method"
        if self.msgType == "location":
            print "this is a location method"
        if self.msgType == "link":
            print "this is a link method"

    def Text_Msg_Response(self, content):
        text_info = '''<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[%s]]></MsgType>
                <Content><![CDATA[%s]]></Content>
                </xml>''' % (self.FromUser, self.ToUser, str(int(time.time())), self.msgType, content)
        return text_info
