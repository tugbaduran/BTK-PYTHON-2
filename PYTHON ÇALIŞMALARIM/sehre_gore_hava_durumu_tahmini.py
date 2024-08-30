import requests
import json

location= input("Şehir arayınız= ")
endpoint= "https://www.metaweather.com/api/location/search/?query={}".format(location)
response= requests.get(endpoint)

def filter_cities(response):
  cities=list(filter(lambda x: x.get("location_type")=="City", response))
  return cities
  
def forecast(woeid):
  endpoint_forcasting ="https://www.metaweather.com/api/location/{}/".format(woeid)
  response= requests.get(endpoint_forcasting)
  response_to_json= json.loads(response.content)
  consolidated_weather= response_to_json.get("consolidated_weather")
  return consolidated_weather


if response.status_code == 200:
  convert_to_dict= json.loads(response.content)
  cities = filter_cities(convert_to_dict)


  for id, city in enumerate(cities):
    print("{} - {}".format(id, city.get("title")))

  city_id= int(input("Şehir Seç= "))
  city = cities[city_id]
  city_woeid= city.get("woeid")
  
  forcasting_result= forecast(city_woeid)

  for weather in forcasting_result:
    print(weather.get("applicable_date"), weather.get("weather_state_name"))
