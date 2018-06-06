import requests
import json

#API key
apikey = "512bc3309fda0712b7aef47ef930c3e5"

#cities
cities = ["Tokyo,JP","London,UK","New York,US"]

#API format
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

#convert K -> C
k2c = lambda k : k - 273.15

for name in cities:
    url = api.format(city=name, key=apikey)
    r = requests.get(url)

    data = json.loads(r.text)
    #print(data)
    #print
    print("+ city = ", data["name"])
    print("| weather = ", data["weather"][0]["description"])
    print("| max temp = ", k2c(data["main"]["temp_max"]))
    print("| min temp = ", k2c(data["main"]["temp_min"]))
    print("| humidity = ", data["main"]["humidity"])
    print("")