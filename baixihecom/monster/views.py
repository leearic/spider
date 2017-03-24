#encoding: UTF-8
from django.shortcuts import render
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

# Create your views here.
from django.http import HttpResponse
from utils import Do_Monster
def gateway(request):
    if request.method == "POST":
        return HttpResponse(u"这里是monster的测试.默认拒绝访问哦".encode('gbk'), content_type="text/plain")
    if request.method == "GET":
        try:
            data = request.GET
            content = data["content"].encode('utf-8')
            response = Do_Monster.Message_Session(data)
            res = response.Text_Msg_Response(content)
            print res
            return HttpResponse(res, content_type="application/xml")
        except Exception as e:
            print e
            return HttpResponse(u"这里是monster的测试.默认拒绝访问哦".encode('gbk'), content_type="text/plain")
    else:
        return HttpResponse('false')