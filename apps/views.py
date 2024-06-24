from django.shortcuts import render
from django.http import HttpResponse

def inicial(request):
    return render(request, 'folha/home.html')

def calculadoras(request):
    return render(request, 'folha/calculadoras.html')

def horaExtra(request):
    return render(request, 'folha/calculadoras/horaExtra.html')