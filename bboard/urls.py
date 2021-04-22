from django.urls import path
from .views import index, cur_time, by_rubric, BbCreateView

urlpatterns = [
    path('', index, name='index'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('cur_time/', cur_time),
    path('add/', BbCreateView.as_view(), name='add'),
]
