from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_list, name='player_list'),
    path('player/new/', views.player_new, name='player_new'),
    path('player/view/<str:pk>/edit/', views.player_edit, name='player_edit'),
    path('player/view/<str:pk>/', views.player_detail, name='player_detail'),

    path('hitter/<int:pk>/add_position/', views.position_new, name='position_new'),
    path('card/<int:pk>/add_rolls/', views.build_card_results, name='build_card_results'),
]