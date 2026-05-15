from django.urls import path
from . import views     

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('saveprofile/', views.save_profile, name='save-profile'),
    path('dashboard/<int:id>/', views.resume, name='resume'),
]