from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('fib', views.result, name='result'),
    path('index', views.index)
]