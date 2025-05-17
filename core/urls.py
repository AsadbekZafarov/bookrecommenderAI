from django.urls import path
from . import views
from templates.accounts.views import register
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('', views.home, name='home'),
    path('best_sellers/', views.best_sellers, name='best_sellers'),
    
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('recommend/', views.recommend, name='recommend'),
    # path('filter/', views.filter_search, name='filter_search'),
    path('by_ai/', views.by_ai, name='by_ai'),
    # path('login_page/country/', views.country_books, name='country'),

]
