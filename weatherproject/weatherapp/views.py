from django.shortcuts import render,redirect
import requests
import datetime
# Create your views here.
def home(request):
    if 'city' in request .POST:
        city = request.POST['city']
    else:
        city = 'indore'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=1787ac1358a851089898c332b5ce1837'
    PARAMS = {'units': 'metric'}

    data = request.get(url,PARAMS).json()

    description = data['weather'][0]['description']
    icon = data['weather'] [0] ['icon']
    temp = data['main']['temp']


    day = datetime.date.today()
    return render(request,'weatherapp/index.html',{'description':description,'icon':icon,'temp':temp,'day':day})