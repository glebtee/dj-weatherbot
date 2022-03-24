from itertools import chain
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
    url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&parse_mode=HTML&text={}'.format(botid, chatid, message)
    m = requests.post(url)

    print('globalchatID={}'.format(chatid))
    print(m.content)

# ask for weather update
def getWeather(units, city):
    city = city
    units = units
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'.format(city, units, weatherappid)

    response = requests.get(url)
    data = json.loads(response.text)

    print(data)

    return data

# index webpage
def index(request):
    city = "Helsinki"
    weather = getWeather("metric", "Helsinki")
    temp = weather['main']['temp']
    responsestr = '<h1>{}</h1><p>ilma meillä nyt: {}</p>'.format(city, temp)

    return HttpResponse(responsestr)

# tele webhook happens here
@require_POST
def bot(request):
    jsondata = request.body
    data = json.loads(jsondata)
    
    if data['message']:
        chatid = data['message']['chat']['id']
        message = data['message']['text']

        sendBotMessage(chatid, message)
        messageForAFriend(chatid)
    else:
        print(data)

    return HttpResponse(status=200)


def messageForAFriend(chatid):
    chatid = chatid
    message = "zzk49_bot дает в жопу"
    
    sendBotMessage(chatid, message)
    
    print("message sent to a friend")

    