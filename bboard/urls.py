from django.urls import path
from .views import index, cur_time

urlpatterns = [
    path('', index),
    path('cur_time/', cur_time),
]