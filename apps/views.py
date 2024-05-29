from django.shortcuts import render
from django.http import HttpResponse

def inicial(request):
    return render(request, 'folha/home.html')

# Create your views here.
