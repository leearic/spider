#coding:utf-8
# from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
from  utils import Boss_Proxy

bp = Boss_Proxy.DO_proxy

@csrf_exempt
def  interface(request):
    if request.method == 'GET':
        response = HttpResponse(bp.CheckSignature(request), content_type="text/plain")
        return response
    if request.method == 'POST':
        response = HttpResponse(bp.Msg_Gateway(request), content_type="application/xml")
        return response
    else:
       return  HttpResponse(u"禁止访问")