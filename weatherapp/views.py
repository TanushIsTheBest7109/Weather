from django.shortcuts import render, HttpResponse
import requests
def home(request):
    temp = f" {0} "
    wind_speed = f" {0}"
    city = "City"
    humidity = 0
    feels_like = 0
    if request.method == "POST":

        city = request.POST.get('city')
        api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
        response = requests.get(api_url, headers={'X-Api-Key': 'oM1cYB4XhrVlyZz3ieZ6ag==mmHLtW2EbcbmLftD'})
        if response.status_code == requests.codes.ok:
            print(type(response.json()))
            temp = f" {response.json()['temp']}"
            wind_speed = f" {response.json()['wind_speed']}"
            humidity = f" {response.json()['humidity']}"
            feels_like = f" {response.json()['feels_like']}"

        else:
            return HttpResponse("Error")


    weather = {
        'temp': temp,
        'wind_speed': wind_speed,
        'city':city,
        'humidity': humidity,
        'feels_like': feels_like
    }



    return render(request, "base.html", weather)