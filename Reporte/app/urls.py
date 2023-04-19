from django.contrib import admin
from django.urls import path, include

from .views import home, pdf

urlpatterns = [
    path('', home, name='home'),
    path('pdf', pdf, name='pdf'),
]