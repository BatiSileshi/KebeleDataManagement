from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginEmployee, name="login"),
    path('logout/', views.logoutEmployee, name="logout"),
    path('register/', views.registerEmployee, name="register"),

    
]
