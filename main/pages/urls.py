from django.urls import path
#from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('', views.home_page,name='home'),
    path('about/', views.about_page,name='about'),
    path('services/', views.services_page,name='services'),
    path('projects/', views.projects_page,name='projects'),
    path('contact/', views.contact_page,name='contact'),
    path('documents/',views.documents_page,name='documents'),
    path('career/',views.career_page,name='career'),

     path('admin/proje/proje/<int:proje_id>/change/<int:image_id>', views.rotate_image, name='rotate_image'),
]