
from django.contrib import admin
from django.urls import path
from Hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('service/', views.service,name='services'),
    path('starter/', views.starter,name='starter'),
]
