from django.urls import path
#from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('', views.home_page,name='home'),
    path('about/', views.about_page,name='about'),
    path('services/', views.services_page,name='services'),
    path('projects/', views.projects_page,name='projects'),
    path('contact/', views.contact_page,name='contact'),
   
    
]