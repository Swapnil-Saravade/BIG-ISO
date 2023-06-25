#from django.contrib import admin
from django.urls import path,include
from auth_system import views
urlpatterns = [
    path('home/',views.homepage,name="homepage"),
    path('',views.register,name="registerpage"),
    path('login/',views.login,name="login"),
    path('logout/', views.logout_view, name='logout'),
]
