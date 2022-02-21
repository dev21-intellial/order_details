from django.contrib import admin
from order import views
from django.urls import path,include

urlpatterns = [
    path('',views.insert,name='insert'),
    path('show',views.show,name='show'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update')
]

