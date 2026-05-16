from django.urls import path
from . import views     

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('saveprofile/', views.save_profile, name='save-profile'),
    path('dashboard/<int:id>/', views.resume, name='resume'),
    path('download/<int:id>/', views.download_resume, name='download_resume'),
    path('edit/<int:id>/', views.edit_resume, name='edit-resume'),
    path('delete/<int:id>/', views.delete_resume, name='delete-resume'),
]