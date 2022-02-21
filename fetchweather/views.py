from django.shortcuts import render
from django.http import HttpResponse
import requests, json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

appid = "ed71a4ff62e0d8b0edffad31710b4085"
botid = "382694174:AAHZeoMmAJQ6C5oLQfoNax11deTbSC2gKvA"
message = ""
chatID = ""

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
    return HttpResponse("<h1>" + city + "</h1>" + "ilma njyttes: " + temp)

@require_POST
def bot(request):
    jsondata = request.body

    data = json.loads(jsondata)
    message = data['message']
    chatID = message['chat']

    return HttpResponse(chatID + ' ' + message)