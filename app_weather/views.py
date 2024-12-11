from datetime import datetime
import json
import requests


from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def my_view(request):
    if request.method == "GET":
        params = {'key': '12ddc253d89342b587a51819240412', 'q': '59.93,30.31'}
        url = f'https://api.weatherapi.com/v1/current.json'
        response = requests.get(url, params=params)
        # print(response.text)
        data = response.json()
        time_ = datetime.fromisoformat(data['current']['last_updated']).time()
        date_ = '.'.join(list(reversed(str(datetime.fromisoformat(data['current']['last_updated']).date()).split('-'))))
        print(json.dumps(data, indent=4))
        s = f'Город: {data["location"]["name"]}\n' \
            f'Страна: {data["location"]["country"]}\n' \
            f'Температура: {data["current"]["temp_c"]} град\n' \
            f'Ветер: {data["current"]["wind_kph"]} км/ч\n' \
            f'Ощущается: {data["current"]["feelslike_c"]} град\n' \
            f'Время обновления:{time_} {date_}'
        print(s)
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})


