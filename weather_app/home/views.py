from multiprocessing import context
from django.shortcuts import render
import requests
import datetime


def home(request):
    now_date = datetime.datetime.now().strftime('%B, %d')
    print(now_date)
    city = request.GET.get('city', 'Minsk')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a1b18de1ce1b2ce2fefc6315113d58ee'
    data = requests.get(url).json()
    payload = {
        'city': data['name'], 
        'weather': data['weather'][0]['main'],
        'icon': data['weather'][0]['icon'],
        'temperature': round(data['main']['temp'] - 273),
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
        'description': data['weather'][0]['description'],
        }
    context = {'data': payload, 'now_date' : now_date}
    print(context)
    

    return render(request, 'home.html', context)