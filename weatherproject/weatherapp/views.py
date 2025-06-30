from django.shortcuts import render
import requests
import datetime
from django.contrib import messages

def home(request):
    if request.method == 'POST' and 'city' in request.POST:
        city = request.POST.get('city')
    else:
        city = 'Indore'

    # Weather API
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=''
    PARAMS = {'units': 'metric'}

    # Google Custom Search API (Image)
    API_KEY = ''
    SEARCH_ENGINE_ID = ''
    query = city + " 1920x1080"
    image_url = None  # Fallback

    try:
        search_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&searchType=image&imgSize=xlarge"
        image_data = requests.get(search_url).json()
        search_items = image_data.get("items")
        if search_items and len(search_items) > 0:
            image_url = search_items[0]["link"]
    except Exception as e:
        print("Image fetch failed:", e)

    # Handle Weather Data
    try:
        data = requests.get(weather_url, params=PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city.title(),
            'exception_occurred': False,
            'image_url': image_url
        })

    except KeyError:
        exception_occurred = True
        messages.error(request, 'Entered data is not available to API')
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': day,
            'city': 'Indore',
            'exception_occurred': exception_occurred,
            'image_url': image_url
        })
