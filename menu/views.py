from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Little Lemon")

class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to Little Lemon")