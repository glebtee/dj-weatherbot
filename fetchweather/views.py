from django.shortcuts import render
from django.http import HttpResponse
import requests, json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

appid = "ed71a4ff62e0d8b0edffad31710b4085"
botid = "382694174:AAHZeoMmAJQ6C5oLQfoNax11deTbSC2gKvA"

message = ""
globalChatID = ""
city = ""
temp = ""

def botMessage(chatid, message):
    url = 'https://api.telegram.org/bot' + botid + '/sendMessage?chat_id=' + chatid + '&parse_mode=HTML&text=' + message
    m = requests.post(url)

    print("globalchatID = " + str(chatid))
    print(m.content)

def getWeather(units, city):
    city = city
    units = units
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}".format(city, units, appid)

    response = requests.get(url)
    data = json.loads(response.text)

    return data

def botWeatherMessage(chatid, city):
    weather = getWeather("metric", "Helsinki")
    city = city
    temp = str(weather["main"]["temp"])

    message = "Temp in " + city + " is ... " + str(temp)
    chatid = chatid
    
    botMessage(chatid, message)

def index(request):
    weather = getWeather("metric", "Helsinki")
    city = weather["name"]
    temp = str(weather["main"]["temp"])

    message = "page refreshed"
    
    botMessage(globalChatID, message)

    return HttpResponse("<h1>" + city + "</h1>" + "ilma meillä nyt: " + temp)

@require_POST
def bot(request):
    city = "Helsinki"
    jsondata = request.body
    data = json.loads(jsondata)

    print(data)
    
    chatid = str(data['message']['chat']['id'])
    weather = getWeather("metric", city)
    print(weather)
    
    botWeatherMessage(chatid, city)

    return HttpResponse(status=200)