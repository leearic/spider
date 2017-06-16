# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from webapp.models import CarinfoModel, ImageInfoModel, TestingInfoModel

from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

import simplejson

def index(request, pages=1):
    cars = CarinfoModel.objects.all()
    paginator = Paginator(cars, 6)
    page = pages # pages #request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    alldata = {}
    carinfodata = []
    for car in contacts:
        cardata = {}
        cardata["name"] = car.name
        cardata["owner"] = car.owner
        cardata["address"] = car.car_address
        cardata["price"] = car.price
        cardata["image"] = car.image
        cardata["owner_say"] = car.owner_say
        carinfodata.append(cardata)

    alldata["carinfo"] = carinfodata
    alldata["currentpage"] = contacts.number
    # if contacts.has_previous:
    #     alldata["has_previous"] = "True"
    # else:
    #     alldata["has_previous"] = "False"
    #
    # if contacts.has_next:
    #     alldata["has_next"] = "True"
    # else:
    #     alldata["has_next"] = "False"
    alldata["page_count"] = len(contacts.paginator.page_range)

    responsedata = simplejson.dumps(alldata, ensure_ascii=False)

    return HttpResponse(responsedata, content_type="application/json; charset=utf8")


def detail(request, id):
    car = CarinfoModel.objects.get(id = id)
    test = TestingInfoModel.objects.get(id = id)
    images = ImageInfoModel.objects.get(id = id)
    data = {}
    data["carname"] = car.name
    data["price"] = car.price
    data["owner"] = car.owner
    data["module"] = car.module
    data["registed_time"] = car.registed_time
    data["mileage"] = car.mileage
    data["displacement"] = car.displacement
    data["car_address"] = car.car_address
    data["owner_say"] = car.owner_say
    data["color"] = test.color
    data["annual_time"] = test.annual_time
    data["delivery_time"] = test.delivery_time
    data["insurance_time"] = test.insurance_time
    data["address"] = test.address
    data["transfer_number"] = test.transfer_number
    data["invoice"] = test.invoice
    data["maintenance"] = test.maintenance
    data["accident_investigation"] = test.accident_investigation
    data["safety_detection"] = test.safety_detection
    data["appearance_detection"] = test.appearance_detection
    data["driving_test"] = test.driving_test
    data["img0"] = images.url0
    data["img1"] = images.url1
    data["img2"] = images.url2
    data["img3"] = images.url3
    data["img4"] = images.url4
    data["img5"] = images.url5
    data["img6"] = images.url6
    responsedata = simplejson.dumps(data, ensure_ascii=False)

    return HttpResponse(responsedata, content_type="application/json; charset=utf8")
    # return render_to_response('webapp/details.html', {"car": car, "images": images, "test":test})