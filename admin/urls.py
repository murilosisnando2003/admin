from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from vendas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name="login"),
    path('home/',views.home, name='home'),
    path('logout/', views.my_logout, name="logout"),
]
