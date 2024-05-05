from django.urls import path
from . import views
urlpatterns = [
    path('<str:project_name>/', views.project_details_page,name='project_details'),
    ]
