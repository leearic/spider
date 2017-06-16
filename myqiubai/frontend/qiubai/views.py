from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext
from qiubai.models import QiuShi
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

def qiushi(request, pages=1):
    Qius = QiuShi.objects.all()
    paginator  = Paginator(Qius, 5)
    page = pages #request.GET.get('page')
    try:
        contacts = paginator .page(page)
    except PageNotAnInteger:
        contacts = paginator .page(1)
    except EmptyPage:
        contacts = paginator .page(paginator.num_pages)
    return render_to_response('index.html',{'qiubais':contacts})




    # return  render('index.html', {'qiubais':Qius}, context_instance=RequestContext(request))