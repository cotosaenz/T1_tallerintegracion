from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_season>/breaking_bad_season/', views.bb_season, name='bb_season'),
    path('<int:id_season>/better_call_saul_season/', views.bcs_season, name='bcs_season'),
    path('<int:id_episode>/episode/', views.episode, name='episode'),
    path('<str:character>/character', views.character, name='character'),
    path('searching_character/', views.search, name='search'),
]