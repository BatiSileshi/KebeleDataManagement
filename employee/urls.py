from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginEmployee, name="login"),
    path('logout/', views.logoutEmployee, name="logout"),
    path('register/', views.registerEmployee, name="register"),
    #employee management
    path('manage-employee/', views.manage_employee, name="manage-employee"),
    path('add-employee/', views.add_employee, name="add-employee"),
    path('update-employee/<str:id>/', views.update_employee, name="update-employee"),
    path('delete-employee/<str:id>/', views.delete_employee, name="delete-employee"),
]
