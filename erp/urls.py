from django.contrib import admin
from django.urls import path

from erp import views


urlpatterns = [

     path('', views.RemanufaturaView.as_view(), name='remanufatura'),
     path('editremanufatura/<int:pk>/', views.edit, name='editremanufatura'),
]