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
    # path('list/', views.persons_list, name="person_list"),
    path('new/', views.persons_new, name="person_new"),
    path('update/<int:id>/', views.persons_update, name="persons_update"),
    # path('delete/<int:id>/', views.persons_delete, name="persons_delete"),
    path('classificacao/', views.classificacao, name='fiscal_classificacao'),
    path('edit-classificacao/<int:id>/', views.edit_classificao, name='edit_classificacao_pk'),

    path('list/', views.IndexView.as_view(), name='index'),
    path('list/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('post/', views.postview, name='post'),
    path('delete/<int:pk>/', views.delete, name='delete'),

]
