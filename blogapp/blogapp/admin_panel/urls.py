from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('users/', views.manage_users, name='manage_users'),
    path('blogs/', views.manage_blogs, name='manage_blogs'),
    path('approve_user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('approve_blog/<int:blog_id>/', views.approve_blog, name='approve_blog'),
    path('inactive_user/<int:user_id>/', views.inactive_user, name='inactive_user'),
    path('inactive_blog/<int:blog_id>/', views.inactive_blog, name='inactive_blog'),
]
