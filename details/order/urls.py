from django.contrib import admin
from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.insert),
    path('show',views.show)
]

