from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ueber-mich/', views.ueber_mich, name='ueber-mich'),
]