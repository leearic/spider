# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from django.shortcuts import render_to_response
from django.http.response import  HttpResponseRedirect
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import recommen

def index(request):
    return render_to_response('index.html')


def details(request):
    wd = request.GET.get('wd')
    pages = request.GET.get('pages')
    product = models.ProductDetail
    if pages == '' or pages == None:
        pages = 1
    if wd == '' or wd == None:
        pass
        return HttpResponseRedirect('/')
    else:
        res_product = product.objects.filter(Q(name__contains = wd))

        rcm = recommen.Recommen()
        rcmd = rcm.GetRandomProduct(res_product.count())


        paginator = Paginator(res_product, 10)
        page = pages
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        return render_to_response('details.html', {'products': products, "count":  res_product.count(), "keyword": wd, "rcm": rcmd})
