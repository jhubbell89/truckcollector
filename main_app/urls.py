from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trucks/', views.trucks_index, name='index'),
    path('trucks/<int:truck_id>/', views.trucks_detail, name='detail'),
    path('trucks/create', views.TruckCreate.as_view(), name='trucks_create'),
    path('trucks/<int:pk>/update/', views.TruckUpdate.as_view(), name='trucks_update'),
    path('trucks/<int:pk>/delete/', views.TruckDelete.as_view(), name='trucks_delete'),  
    path('trucks/<int:truck_id>/add_service/', views.add_service, name='add_service'),

]