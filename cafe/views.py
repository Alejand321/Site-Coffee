from django.shortcuts import render
from django.http import HttpResponse 
from .models import Cafe

def home(request):
    cafe = Cafe.objects.all()
    return render(request, 'inicio.html', {'cafe': cafe})

