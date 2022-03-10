from django.shortcuts import render
from django.http import HttpResponse
import requests, json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

weatherappid = "ed71a4ff62e0d8b0edffad31710b4085"
botid = "382694174:AAHZeoMmAJQ6C5oLQfoNax11deTbSC2gKvA"

message = ""
chatid = ""
city = ""
temp = ""

# send bot message
def sendBotMessage(chatid, message):
    url = 'https://api.telegram.org/bot' + botid + '/sendMessage?chat_id=' + chatid + '&parse_mode=HTML&text=' + message
    m = requests.post(url)

    print("globalchatID = " + str(chatid))
    print(m.content)

# ask for weather update
def getWeather(units, city):
    city = city
    units = units
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}".format(city, units, weatherappid)

    response = requests.get(url)
    data = json.loads(response.text)

    print(data)

    return data

# send telegram a weather update
def sendWeatherBotMessage(chatid, city):
    city = city
    weather = getWeather("metric", city)
    temp = str(weather["main"]["temp"])

    message = "Temp in " + city + " is ... " + str(temp)
    chatid = chatid
    
    sendBotMessage(chatid, message)

# index webpage
def index(request):
    city = "Helsinki"
    weather = getWeather("metric", "Helsinki")
    temp = str(weather["main"]["temp"])
    message = "page refreshed"
    chatid = "201222234"
    
    sendBotMessage(chatid, message)
    sendWeatherBotMessage(chatid, city)

    return HttpResponse("<h1>" + city + "</h1>" + "ilma meillä nyt: " + temp)

# tele webhook happens here
@require_POST
def bot(request):
    jsondata = request.body
    data = json.loads(jsondata)
    
    print(data)
    
    return HttpResponse(status=200)