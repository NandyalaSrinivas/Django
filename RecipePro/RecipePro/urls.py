from django.contrib import admin
from django.urls import path
from app_recipe import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('create/', views.create, name = 'creat'),
    path('<int : id>/details', views.details, name = 'details'),
    path('<int : id>/delete', views.delete, name = 'delete')
]
