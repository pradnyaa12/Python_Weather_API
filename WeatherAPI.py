import requests
import os
from datetime import datetime 


#stored secret information in windows environment varibales 

user_api=os.environ['weather_data_API']
latitude=input("Enter the latitude : ")
longitude=input("Enter the longitude : ")

#this is from https://openweathermap.org website 
#api-current weather data
#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
#lat, lon	required	Geographical coordinates (latitude, longitude). If you need the geocoder to automatic convert city names and zip-codes to geo coordinates and the other way around, please use our Geocoding API.


api_key="https://api.openweathermap.org/data/2.5/weather?lat="+latitude+"&lon="+longitude+"&appid="+user_api

api_link=requests.get(api_key)
api_data=api_link.json()

print("api data :",api_data)

if api_data['cod']==404:
    print("Invalid city:{},Please check your latitude or longitude".format(latitude))
else:
    temp_city=((api_data['main']['temp'])-273.15)
    weather_desc=api_data['weather'][0]['description']
    humidity=api_data['main']['humidity']
    wind_speed=api_data['wind']['speed']
    date_time=datetime.now().strftime("%d %b %y | %I:%M:%S %p")
    
    print("weather stats for-{} || {}".format(latitude.upper(),date_time))
    print("current temperature is:{:.2f} deg c".format(temp_city))
    print("current weather desc: ",weather_desc)
    print("current Humidity:",humidity,'%')
    print("current wind speed: ",wind_speed,'kmph')
    
    
    
#create account on OpenWeatherMap.org 
#create API key 
#select Current Weather Data
# copy the api call : https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
#create api request from python
