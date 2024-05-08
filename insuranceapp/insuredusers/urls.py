from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('edit-profil/<int:user_id>', views.update_view, name='update-profile'),
    path('delete-profil/<int:user_id>', views.delete_view, name='delete-profile'),
]