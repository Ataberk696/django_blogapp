from django.urls import path
from . import views

urlpatterns = [
    path('blogs/<slug:slug>/comments/', views.comments_view, name='comments'),
    path("", views.index, name='home'),
    path("index", views.index),
    path("blogs", views.blog, name='blogs'),
    path('blogs/<slug:slug>/', views.blog_details, name='blog_details'),
    path('add/', views.add_blog, name='add_blog'),
    path('load-filtered-blogs/', views.load_filtered_blogs, name='load_filtered_blogs'),
    # path('load-more-blogs/', views.load_more_blogs, name='load_more_blogs'),
    # path('filter-blogs/', views.filter_blogs, name='filter_blogs'),
]
