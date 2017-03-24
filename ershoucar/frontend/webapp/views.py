from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from .models import CarinfoModel, ImageInfoModel, TestingInfoModel
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

def index(request, pages=1):
    cars = CarinfoModel.objects.all()
    paginator  = Paginator(cars, 6)
    page = pages # pages #request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('webapp/index.html', {"cars": contacts})

def detail(request, id):
    car = CarinfoModel.objects.get(id = id)
    test = TestingInfoModel.objects.get(id = id)
    images = ImageInfoModel.objects.get(id = id)
    return render_to_response('webapp/details.html', {"car": car, "images": images, "test":test})
