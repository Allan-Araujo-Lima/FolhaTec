from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicial, name='home'),
    path('calculadoras', views.calculadoras, name='calculadoras'),
    path('calculadoras/hora-extra', views.horaExtra, name='hora-extra')
]