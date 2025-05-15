from django.shortcuts import render
#from django.http import JsonResponse
from django.conf import settings
import requests
import math


API_KEY = settings.RAWG_API

def landing_page_games(request):
    category = request.GET.get("ordering","metacritic")
    search_query = request.GET.get("search","")
    page = int(request.GET.get("page",1))
    next_page = page + 1

    base_url = "https://api.rawg.io/api/games"
    message_error =""
    games = []


    if search_query:
        url = f'https://api.rawg.io/api/games?key={API_KEY}&search={search_query}&page={page}'
    else:
        url = f'{base_url}?key={API_KEY}&ordering={category}&page={page}'
    try:
        response = requests.get(url)
        data = response.json()
        count = data.get("count", 0)
        games = data.get("results",[])
        page_size = len(games)
        total_pages = math.ceil(count/page_size) if page_size else 1
        has_next = page<total_pages
        # Ver por consola que devuelve la variable.
        #print(games)
    except Exception as e:
        games = []
        message_error=f"Algo salió mal: {str(e)}"
        has_next = False

    if request.headers.get("HX-Request"):
        return render(request,"games/partials/_game_list.html",{"games":games,
                                                "message_error":message_error,
                                                "has_next":has_next,
                                                "count":count,
                                                "next_page":next_page,
                                                "category":category
                                                }) 
    
    return render(request,"games/landing.html",{"games":games,
                                                "message_error":message_error,
                                                "has_next":has_next,
                                                "count":count,
                                                "next_page":next_page,
                                                "category":category
                                                })

def game_detail(request,game_id):
    game_detail_url = f'https://api.rawg.io/api/games/{game_id}?key={API_KEY}'
    pass