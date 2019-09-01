from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('post/<post_id>/', views.view_post, name='post'),
]
