#!/usr/bin/env python
# coding: utf-8

# In[12]:


import requests 

from datetime import datetime

current = datetime.now() 

api_key='bfc323db64c9224acdc8c1d72df4dd3d'

location = input("Enter your city name") 
 
api_link="http://api.openweathermap.org/data/2.5/weather?q="+str(location)+"&appid="+api_key 

link = requests.get(api_link) 
data = link.json() 

 
temp_in_C = (data['main']['temp']-273.15)  

descr = data['weather'][0]['description'] 

humid = data['main']['humidity'] 

wind_spd = data['wind']['speed'] 

cloud_per = data['clouds']['all'] 

print("***************************************************************") 

print("Weather report for {} at {} is: ".format(location.upper(),current)) 

print("***************************************************************") 


print("Description of Weather: "+ descr)

print("Temperature in Celsius: "+str(temp_in_C)) 

print("Humidity is: "+ str(humid)+"%") 

print("Wind Speed is: "+ str(wind_spd)) 

print("Cloud Availability is: "+str(cloud_per)+"%")

print()

weather_data = open("weather_info.txt","a")
weather_data.write("\nWeather report for {} at {} is: ".format(location.upper(),current)+"\n")
weather_data.write("Description of Weather: "+ descr+"\n")
weather_data.write("Temperature in Celsius: "+str(temp_in_C)+"\n") 
weather_data.write("Humidity is: "+ str(humid)+"%"+"\n")
weather_data.write("Wind Speed is: "+ str(wind_spd)+"\n") 
weather_data.write("Cloud Availability is: "+str(cloud_per)+"%"+"\n")
weather_data.close()
weather_data = open("weather_info.txt","r")
weather_data.close()


# In[9]:





# In[ ]:




