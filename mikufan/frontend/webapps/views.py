from django.shortcuts import render_to_response

# Create your views here.
from .models import Coser, Images
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger





def index(request, pages=1):
    cosers = Coser.objects.order_by('-id')
    paginator = Paginator(cosers, 8)
    page = pages
    try:
        coser = paginator.page(page)
    except PageNotAnInteger:
        coser = paginator.page(1)
    except EmptyPage:
        coser = paginator.page(paginator.num_pages)



    topcoser = Coser.objects.filter(istop = 1)

    return render_to_response('webapps/index.html', {"coser": coser, 'TopCoser': topcoser})


def detail(request, id):
    image = Images.objects.filter(coser_id=id)
    mycoser = Coser.objects.get(id=id)


    cosers = Coser.objects.order_by('-id')[:18]
    # paginator = Paginator(cosers, 18)
    # # page = 1
    # try:
    #     coser = paginator.page(1)
    # except PageNotAnInteger:
    #     coser = paginator.page(1)
    # except EmptyPage:
    #     coser = paginator.page(paginator.num_pages)

    return render_to_response('webapps/detail.html', {"coser": cosers, "images": image, "Coser":mycoser})