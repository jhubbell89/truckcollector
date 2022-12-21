from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trucks/', views.trucks_index, name='index'),
    path('trucks/<int:truck_id>/', views.trucks_detail, name='detail'),
]