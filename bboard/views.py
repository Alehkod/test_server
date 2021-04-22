from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Rubric
import datetime
from .models import Bb
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import BbForm


# Create your views here.

def index(request):
    bbs = Bb.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs})


def cur_time(request):
    return HttpResponse(f'Cur time is {datetime.datetime.now()}')


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
