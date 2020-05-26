# -*- coding: utf-8 -*-
"""
Created on Tue May 26 13:54:00 2020

@author: Om
"""

import requests,json
import tkinter as tk
from tkinter import messagebox as mb
def weather_forecast():
    api_key = "d44125ad62ff58c1d546676f6f9cf07e"

    base_url="http://api.openweathermap.org/data/2.5/weather?"

    city_name = text.get()


    url= base_url+"appid="+api_key+"&q="+city_name

    response=requests.get(url)

    x=response.json()

    if x["cod"] != "404":
        y=x["main"]
        current_temperature = int(y["temp"]-273.15)
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        print(" Temperature (in celsius) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description)) 
        mb.showinfo("Today's weather forecast is"," Temperature (in celsius) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description) )
    else: 
        print(" City Not Found ")


root=tk.Tk()
L1=tk.Label(root,text="city name")
b1=tk.Button(root , text="submit", font = 30, width = 10, command=weather_forecast)

text= tk.Entry(root)
L1.grid(row=0,column=0)
text.grid(row=0,column=1)
b1.grid(row=1,column=1)

root.mainloop()