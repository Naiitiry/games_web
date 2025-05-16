from django.shortcuts import render
#from django.http import JsonResponse
from django.conf import settings
import requests
import math


API_KEY = settings.RAWG_API

def landing_page_games(request):
    category = request.GET.get("ordering","metacritic")
    platform_query = request.GET.get("platforms","")
    search_query = request.GET.get("search","")
    exclude_additions = request.GET.get("exclude_additions", "")
    page = int(request.GET.get("page",1))
    next_page = page + 1

    base_url = "https://api.rawg.io/api/games"
    message_error =""
    games = []
    platforms = []
    additions = []

    params={
        "key":API_KEY,
        "page":page,
        "ordering":f'{category}'
    }


    if search_query:
        params["search"] = search_query
    if platform_query:
        params["platforms"] = platform_query
    if exclude_additions:
        params["exclude_additions"] = exclude_additions
    
    # Try para los bucles de la lista de los juegos, con sus atributos
    try:
        response = requests.get(base_url,params=params)
        data = response.json()
        count = data.get("count", 0)
        games = data.get("results",[])
        page_size = len(games)
        total_pages = math.ceil(count/page_size) if page_size else 1
        has_next = page<total_pages
        # Ver por consola que devuelve la variable.
        # print(games)
    except Exception as e:
        games = []
        message_error=f"Algo salió mal: {str(e)}"
        has_next = False

    # Try para el bucle con las plataformas
    try:
        platforms_response = requests.get(f"https://api.rawg.io/api/platforms?key={API_KEY}")
        platforms_response.raise_for_status()
        platforms_data = platforms_response.json()
        platforms = platforms_data.get("results", [])
    except Exception as e:
        platforms = []
        message_error=f"Algo salió mal: {str(e)}"


    context = {
        "games": games,
        "message_error": message_error,
        "has_next": has_next,
        "next_page": next_page,
        "category": category,
        "platform": platform_query,
        "search_query": search_query,
        "platforms":platforms,
        "exclude_additions":exclude_additions
    }
    template = "games/partials/_game_list.html" if request.headers.get("HX-Request") else "games/landing.html"
    
    return render(request,template,context)

def game_detail(request,game_id):
    game_detail_url = f'https://api.rawg.io/api/games/{game_id}?key={API_KEY}'
    error_message = ""

    try:
        game_detail_response = requests.get(game_detail_url)
        game_detail_response.raise_for_status()
        game_data = game_detail_response.json()
    except Exception as e:
        game_data = []
        error_message = f"Error a obtener los datos del juego, {str(e)}"

    return render(request,'games/games_detail.html',{"game":game_data,
                                                     "error_message":error_message,})