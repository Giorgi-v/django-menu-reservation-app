from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to Little Lemon")

class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to Little Lemon")

def home(request):
    form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    
    return render(request, 'index.html', {'form' : form })