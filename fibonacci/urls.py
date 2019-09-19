from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('fib', views.get_fib, name='result'),
    path('index', views.index)
]