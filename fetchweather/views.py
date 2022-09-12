import os, requests, json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.conf import settings

weatherappid = os.environ['WEATHER_ID']
botid = os.environ['BOT_ID']
message = ""
chatid = ""
city = ""
temp = ""

# send bot message
def sendBotMessage(chatid, message):
    """ takes chat id and message string as parameters, sends message to telegram bot
    """
    try:
     url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&parse_mode=HTML&text={}'.format(botid, chatid, message)
     m = requests.post(url)
    except:
        print('*** cant send messages now')

# get weather update
def getWeather(units, city):
    """takes temperature units and city name as parameters, sends request to openweather app,
    returns data
    """
    city = city
    units = units
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'.format(city, units, weatherappid)

    response = requests.get(url)
    data = json.loads(response.text)

    print(url)

    return data
# get cat url
def getCatURL():
    """ returns random cat picture from cat api
    """
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    data = json.loads(response.text)

    print(data)

    return data[0]['url']

# index webpage
def index(request):
    """ returns an index page with city air temperature
    """
    city = "Helsinki"
    weather = getWeather("metric", "Helsinki")

    try:
        temp = weather['main']['temp']
        responsestr = '<h1>{}</h1><p>ilmat meillä nyt: {}</p>'.format(city, temp)
    except:
        responsestr = '<p>Säätä ei pysty hakee lols</p>'

    return HttpResponse(responsestr)

# path to city webpage
def city(request, cityname):
    """ returns an index page with city air temperature
    """
    weather = getWeather("metric", cityname)

    try:
        temp = weather['main']['temp']
        responsestr = '<h1>{}</h1><p>ilmat meillä nyt: {}</p>'.format(cityname, temp)
    except:
        responsestr = '<p>Säätä ei pysty hakee lols</p>'

    return HttpResponse(responsestr)

# REMEMBER set webook in tele: 
# curl -F "url=https://weatherboat.azurewebsites.net/bot/" https://api.telegram.org/bot{botid}/setWebhook
@require_POST
def bot(request):
    """ telegram webhook happens here, returns bot messages, 
        must remember to set webhook after initial app deployment
    """
    jsondata = request.body
    data = json.loads(jsondata)

    print(data)

    if 'message' in data:
        chatid = data['message']['chat']['id']
        message = data['message']['text']

        try:
            temp = getWeather('metric', message)['main']['temp']
            sendBotMessage(chatid, 'Its {} degrees in {}'.format(temp, message))

        except:
            sendBotMessage(chatid, "nope")
            sendBotMessage(chatid, getCatURL())

    else:
        print("----traffic other than messages---------->")
        print(data)

    return HttpResponse(status = 200)