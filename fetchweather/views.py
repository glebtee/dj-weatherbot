from django.shortcuts import render
from django.http import HttpResponse
import requests, json

appid = "ed71a4ff62e0d8b0edffad31710b4085"

def getWeather(units, city):
    city = city
    units = units
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}".format(city, units, appid)

    response = requests.get(url)
    data = json.loads(response.text)

    return data

def index(request):
    weather = getWeather("metric", "Helsinki")
    city = weather["name"]
    temp = str(weather["main"]["temp"])
    return HttpResponse("<h1>" + city + "</h1>" + "ilma: " + temp)
