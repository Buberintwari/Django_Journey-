from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from datetime import datetime


# Create your views here.


# the index() will handle all the app's logic
def index(request):
    API_KEY = '315049b1192ee0f8150acdab3aa16c2c'
    city_weather_update = {}

    if request.method == 'POST':
        city_name = request.POST.get('city', '').strip()
        if city_name:  # Vérifie que la ville n'est pas vide
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
            
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()  # Lève une erreur en cas de mauvais statut HTTP
                data = response.json()
                
                if data.get("cod") != 200:  # Vérifie si la requête a réussi
                    raise ValueError(data.get("message", "Invalid response from API"))

                # Récupération et formatage des données
                current_time = datetime.now().strftime("%A, %B %d %Y, %H:%M:%S %p")
                
                city_weather_update = {
                    'city': city_name,
                    'description': data['weather'][0]['description'].capitalize(),
                    'icon': data['weather'][0]['icon'],
                    'temperature': f"Temperature: {data['main']['temp']} °C",
                    'country_code': data['sys']['country'],
                    'wind': f"Wind: {data['wind']['speed']} m/s",
                    'humidity': f"Humidity: {data['main']['humidity']}%",
                    'time': current_time
                }


            except requests.exceptions.RequestException as e:
                city_weather_update = {'error': "Problème de connexion avec l'API. Réessayez plus tard."}
            except (KeyError, ValueError) as e:
                 city_weather_update = {'error': "Ville introuvable ! Vérifiez l'orthographe et réessayez."}


    context = {'city_weather_update': city_weather_update}
    return render(request, 'weatherupdates/home.html', context)