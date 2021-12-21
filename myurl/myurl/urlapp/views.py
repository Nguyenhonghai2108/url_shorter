from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import MyURL

# Create your views here.
def index(request):
    return HttpResponse('Xin chào, đây là hệ thống rút gọn link của chúng tôi')


def list_url(request):
    my_urls = MyURL.objects.all()
    template = '<a href="/urlapp/detail/{alias}/">/urlapp/{alias}</a> --> {url}<br/>'
    value = ''
    for my_url in my_urls:
        value += template.format(alias=my_url.alias, url=my_url.url)
    return HttpResponse(value)


def detail(request, alias):
    try:
        my_url = MyURL.objects.get(alias=alias)
    except MyURL.DoesNotExist:
        raise Http404('alias does not exist')
    return redirect(my_url.url)