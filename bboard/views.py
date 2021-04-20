from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import datetime
from .models import Bb


# Create your views here.

def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))


def cur_time(request):
    return HttpResponse(f'Cur time is {datetime.datetime.now()}')
