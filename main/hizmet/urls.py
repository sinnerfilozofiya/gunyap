from django.urls import path
from . import views
urlpatterns = [
    path('<str:service_name>/', views.service_detail_page,name='service_detail'),
    ]
