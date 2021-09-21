from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_list, name='player_list'),
    path('player/new/', views.player_new, name='player_new'),
    path('player/<str:pk>/edit/', views.player_edit, name='player_edit'),
    path('player/<str:pk>/', views.player_detail, name='player_detail'),
]