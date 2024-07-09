from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/threads/', views.thread_list, name='thread_list'),
    path('threads/<int:thread_id>/posts/', views.post_list, name='post_list'),
    path('threads/<int:thread_id>/posts/<int:post_id>/', views.post_detail, name='post_detail'),
]
