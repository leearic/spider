from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext
from cnirole.models import cosplay8dotcom
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger




def index(request, pages=1):
    cosplay8 = cosplay8dotcom.objects.all()
    paginator  = Paginator(cosplay8,40)
    page = pages #request.GET.get('page')
    try:
        contacts = paginator .page(page)
    except PageNotAnInteger:
        contacts = paginator .page(1)
    except EmptyPage:
        contacts = paginator .page(paginator.num_pages)
    return render_to_response('index.html', {'cosplay8': contacts})