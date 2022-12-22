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
    path('trucks/<int:truck_id>/assoc_mo/<int:mod_id>/', views.assoc_mod, name='assoc_mod'),
    path('mods/', views.ModList.as_view(), name='mods_index'),
    path('mods/<int:pk>/', views.ModDetail.as_view(), name='mods_detail'),
    path('mods/create/', views.ModCreate.as_view(), name='mods_create'),
    path('mods/<int:pk>/update/', views.ModUpdate.as_view(), name='mods_update'),
    path('mods/<int:pk>/delete/', views.ModDelete.as_view(), name='mods_delete'),
]