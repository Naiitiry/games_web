from django.urls import path
from .views import landing_page_games

urlpatterns = [
    path('',landing_page_games,name="landing_page_games"),
    
]
