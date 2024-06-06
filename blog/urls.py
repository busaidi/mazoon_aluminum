from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:category_slug>/<slug:slug>', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.category, name='category_detail'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('post/create/', views.post_create, name='post_create'),
]

