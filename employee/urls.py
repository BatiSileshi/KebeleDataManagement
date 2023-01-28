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
    path('sent-message/<str:pk>/', views.view_sent_message, name="sent-message"),
    path('create-message/', views.create_message_all, name="create-message-all"),
]

handler404 = "employee.views.page_not_found"