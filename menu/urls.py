from django.urls import path
from . import views

urlpatterns = [
    path('home', views.welcome, name='welcome'),
    path('home-class/', views.HomeView.as_view(), name='home_class'),
    path('reservation', views.home)
]