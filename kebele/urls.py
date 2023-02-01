from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    
    # resident management
    path('mr/', views.manage_resident, name="manage-resident"),
    path('add-resident/', views.add_resident, name="add-resident"),
    path('update-resident/<str:id>/', views.update_resident, name="update-resident"),
    path('view-resident/<str:id>/', views.view_resident, name="view-resident"),
         #address
    path('add-address/<str:id>/', views.add_address, name="add-address"),
    path('update-address/<str:id>/', views.update_address, name="update-address"),
         #house
    path('add-house/', views.add_house, name="add-house"),
    path('update-house/<str:id>/', views.update_house, name="update-house"),
    path('view-house/<str:id>/', views.view_house, name="view-house"),
         #family
    path('add-family/', views.add_family, name="add-family"),
    path('update-family/<str:id>/', views.update_family, name="update-family"),
    path('view-family/<str:id>/', views.view_family, name="view-family"),
         #id card
    path('add-idcard/', views.add_id_card, name="add-idcard"),
    path('update-idcard/<str:id>/', views.update_id_card, name="update-idcard"),
    path('view-idcard/<str:id>/', views.view_idcard, name="view-idcard"),
    
     # ? end of resident management
    
    
#     path('mvd', views.manage_vital_data, name="manage-vital-data"),
    
    #local business management
    path('mlb', views.manage_local_business, name="manage-local-business"),
    
    #local business
    path('add-local-business/', views.add_local_business, name="add-local-business"),
    path('update-local-business/<str:id>/', views.update_local_business, name="update-local-business"),
    path('delete-local-business/<str:id>/', views.delete_local_business, name="delete-local-business"),
    
    #local business owners
    path('add-lb-owner/', views.add_lb_owner, name="add-lb-owner"),
    path('update-lb-owner/<str:id>/', views.update_lb_owner, name="update-lb-owner"),
    path('delete-lb-owner/<str:id>/', views.delete_lb_owner, name="delete-lb-owner"),
        
    # managing kebele house
    path('mkh', views.manage_kebele_house, name="manage-kebele-house"),
    path('add-kebele-house/', views.add_kebele_house, name="add-kebele-house"),
    path('update-kebele-house/<str:id>/', views.update_kebele_house, name="update-kebele-house"),
    path('view-kh/<str:id>/', views.view_kebele_house, name="view-kh"),
    
        
     #managing kebele land
#     path('mkl', views.manage_kebele_land, name="manage-kebele-land"),
#     path('add-kebele-land/', views.add_kebele_land, name="add-kebele-land"),
#     path('update-kebele-land/<str:id>/', views.update_kebele_land, name="update-kebele-land"),


    
]