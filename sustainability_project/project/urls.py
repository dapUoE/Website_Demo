from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('home/', views.home, name='home'),
    path('navbar/', views.navbar, name='navbar'),
    path('base/', views.base, name='base'),
    path('profile/<str:username>', views.profile, name='profile')
    
]