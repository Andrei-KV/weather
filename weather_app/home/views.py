import requests
from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    city = request.GET.get("city", "Minsk")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a1b18de1ce1b2ce2fefc6315113d58ee"
    # Task: add try/except for lost requests, new html
    response = requests.get(url)
    # Task: add new html with fail-text, new input attempt
    if response.status_code != 200:
        return HttpResponse("OK")
    data = response.json()
    payload = {
        "city": data["name"],
        "weather": data["weather"][0]["main"],
        "icon": data["weather"][0]["icon"],
        "temperature": round(data["main"]["temp"] - 273),
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "description": data["weather"][0]["description"],
    }
    context = {"data": payload}

    return render(request, "home.html", context)
