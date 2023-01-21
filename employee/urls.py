from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginEmployee, name="login"),
    path('logout/', views.logoutEmployee, name="logout"),
    path('register/', views.registerEmployee, name="register"),
    path('account/', views.employee_profile, name="account"),
    path('update-profile/', views.editProfile, name="update-profile"),
    #employee management
    path('manage-employee/', views.manage_employee, name="manage-employee"),
    path('add-employee/', views.add_employee, name="add-employee"),
    path('update-employee/<str:id>/', views.update_employee, name="update-employee"),
    path('delete-employee/<str:id>/', views.delete_employee, name="delete-employee"),
    
    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.view_message, name="message"),
    path('create-message/<str:id>/', views.create_message, name="create-message"),
]

handler404 = "employee.views.page_not_found"