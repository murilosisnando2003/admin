from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from vendas import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name="login"),
    path('home/',views.home, name='home'),
    path('logout/', views.my_logout, name="logout"),
    path('person/', views.persons_list, name="person"),
    path('list/', views.persons_list, name="person_list"),
    path('new/', views.persons_new, name="person_new"),
    path('update/<int:id>/', views.persons_update, name="persons_update"),
    path('delete/<int:id>/', views.persons_delete, name="persons_delete"),

]
