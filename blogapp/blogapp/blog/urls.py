from django.urls import path
from . import views

urlpatterns = [
    # path('ajax-test/', views.ajax_test_view, name='ajax_test'),
    path('blogs/<slug:slug>/comments/', views.comments_view, name='comments'),
    path("", views.index, name='home'),
    path("index", views.index),
    path("blogs", views.blog, name='blogs'),
    path("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),
    path("blogs/<slug:slug>", views.blog_details , name='blog_details'),
    path('add/', views.add_blog, name='add_blog'),
]
