from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('home-class/', views.HomeView.as_view(), name='home_class')
]