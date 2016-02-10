#!/usr/bin/env python

from django.http import Http404, HttpResponse

def hello(request):
    return HttpResponse("Hello world")

