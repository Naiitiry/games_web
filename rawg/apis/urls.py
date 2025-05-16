from django.urls import path
from .views import landing_page_games,game_detail

urlpatterns = [
    path('',landing_page_games,name="landing_page_games"),
    path('game_detail/<int:game_id>',game_detail,name="game_detail"),
    
]
