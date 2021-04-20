from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import datetime
from .models import Bb


# Create your views here.

def index(request):
    bbs = Bb.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs})


def cur_time(request):
    return HttpResponse(f'Cur time is {datetime.datetime.now()}')
