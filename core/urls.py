from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recommend/', views.recommend, name='recommend'),
    path('filter/', views.filter_search, name='filter_search'),
    path('last-read/', views.last_read_search, name='last_read_search'),

]
