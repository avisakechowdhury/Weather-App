from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):

    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=df53d7c0e1b87d827627a8d884e18660').read()

        json_data = json.loads(res)
        data = {
            "country_code" : str(json_data['sys']['country']),
            "coordinate" : str(json_data['coord']['lat']) + ' ' +
            str(json_data['coord']['lon']),
            "temp" : str(json_data['main']['temp']) +'k',
            "pressure" : str(json_data['main']['pressure']),
            "humidity" : str(json_data['main']['humidity']),
        }
    else:
        data = {}
        city = ''
    return render(request, 'index.html', {'city':city.capitalize(), 'data':data})