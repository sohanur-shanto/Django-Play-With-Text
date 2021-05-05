from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('playwithtext/', views.index, name = 'index'),
    path('analyzing/', views.analyzing, name = 'analyzing'),
    path('contact/', views.contact, name = 'Contact'),
    path('aboutme/', views.aboutme, name = 'AboutMe'),

]
