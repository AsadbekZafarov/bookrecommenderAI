from django.urls import path
from . import views

urlpatterns = [
    path('login_page/', views.login, name='login_page'),
    path('', views.recommend, name='recommend'),
    path('filter/', views.filter_search, name='filter_search'),
    path('last-read/', views.by_ai, name='by_ai'),

]
