from django.urls import path
#from django.contrib.auth.views import LoginView
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home_page,name='home'),
    path('kullanici/', views.login_page,name='login'),
    path('profile/', views.profile_page,name='profile'),
    path('customer/', views.list_page, name='customer'),  
    path('filter_file/', views.filter_file, name='filter_file'),  
    path('about/', views.about_page,name='about'),
    path('services/', views.services_page,name='services'),
    path('projects/', views.projects_page,name='projects'),
    path('documents/', views.deneme_page,name='documents'),
    path('contact/', views.contact_page,name='contact'),
    #path('documents/',views.documents_page,name='documents'),
    path('career/',views.career_page,name='career'),
    path('/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('admin/proje/proje/<int:proje_id>/change/<int:image_id>', views.rotate_image, name='rotate_image'),
]