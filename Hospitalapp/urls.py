
from django.contrib import admin
from django.urls import path
from Hospitalapp import views

urlpatterns = [

    path('', views.index,name='home'),
    path('service/', views.service,name='services'),
    path('starter/', views.starter,name='starter'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('departmets/', views.departments,name='departments'),
    path('doctors/', views.doctors,name='doctors'),
    path('contact/', views.contact,name='contact'),
    path('appointment/', views.appointment,name='appointment'),
    path('show/', views.show,name='show'),
    path('delete/<int:id>', views.delete),
]
