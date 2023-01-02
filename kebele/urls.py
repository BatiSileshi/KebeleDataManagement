from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    
    path('mr/', views.manage_resident, name="manage-resident"),
    path('add-resident/', views.add_resident, name="add-resident"),
    
    
    path('mvd', views.manage_vital_data, name="manage-vital-data"),
    path('mlb', views.manage_local_business, name="manage-local-business"),
    path('mkl', views.manage_kebele_land, name="manage-kebele-land"),
    path('mkl', views.manage_kebele_house, name="manage-kebele-house"),

    
]