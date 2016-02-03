#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Sean
# @Date:   2016-01-20 00:56:10
# @Last Modified by:   Sean
# @Last Modified time: 2016-01-20 01:58:26
#每个视图函数至少要有一个参数，通常被叫作request。 这是一个触发这个视图、包含当前Web请求信息的对象，是类django.http.HttpRequest的一个实例。在这个示例中，我们虽然不用request做任何事情，然而它仍必须是这个视图的第一个参数。
#仅仅返回一个HttpResponse对象，这个对象包含了文本“Hello world”
from django.template.loader import get_template
from django.template import Template, Context
from django.http import Http404, HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")



'''
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
'''


def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)