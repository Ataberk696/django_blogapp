from django.urls import path
from . import views
from .views import ajax_manage_users, ajax_manage_blogs, manage_users, manage_blogs

app_name = 'admin_panel'

urlpatterns = [
    path('update_status/', views.update_status, name='update_status'),
    path('users/', manage_users, name='manage_users'),
    path('blogs/', manage_blogs, name='manage_blogs'),
    path('ajax/manage-users/', ajax_manage_users, name='ajax_manage_users'),
    path('ajax/manage-blogs/', ajax_manage_blogs, name='ajax_manage_blogs'),

]
    # path('approve_user/<int:user_id>/', views.approve_user, name='approve_user'),
    # path('approve_blog/<int:blog_id>/', views.approve_blog, name='approve_blog'),
    # path('inactive_user/<int:user_id>/', views.inactive_user, name='inactive_user'),
    # path('inactive_blog/<int:blog_id>/', views.inactive_blog, name='inactive_blog'),
    # path('users/', views.manage_users, name='manage_users'),
    # path('blogs/', views.manage_blogs, name='manage_blogs'),
    # path('ajax-test/', views.ajax_test_view, name='ajax_test')
    # path('activate_user/', views.activate_user, name='activate_user'),
    # path('deactivate_user/', views.deactivate_user, name='deactivate_user'),
    # path('activate_blog/', views.activate_blog, name='activate_blog'),
    # path('deactivate_blog/', views.deactivate_blog, name='deactivate_blog'),