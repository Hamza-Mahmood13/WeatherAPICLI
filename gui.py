import tkinter as tk
from main import get_location, get_weather, describe_weather

def show_weather():
    city = city_entry.get().strip()

    if not city:
        result_label.config(text="City name cannot be empty")
        return
    
    result_label.config(text="Loading weather data...")
    root.update()
    
    location = get_location(city)

    if location is None:
        result_label.config(text="City not found")
        return
    
    name = location.get("name")
    country = location.get("country")
    latitude = location.get("latitude")
    longitude = location.get("longitude")

    current_weather = get_weather(latitude, longitude)

    if current_weather is None:
        result_label.config("Weather data not found")
        return
    
    temperature = current_weather.get("temperature")
    weather_code = current_weather.get("weathercode")
    description = describe_weather(weather_code)
    wind_speed = current_weather.get("windspeed")

    result_label.config(
        text=f"Location: {name}, {country}\n"
            f"Temperature: {temperature}°C\n"
            f"Conditions: {description}\n"
            f"Wind Speed: {wind_speed} km/h"
    )

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

title_label = tk.Label(root, text="Weather App", font=("Arial", 16))
title_label.pack(pady=15)

instruction_label = tk.Label(root, text="Enter a city name to get the current weather:", font=("Arial", 10))
instruction_label.pack(pady=5)

city_entry = tk.Entry(root, width=30, font=("Arial", 11))
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Get Weather", command=show_weather, width=18)
search_button.pack(pady=10)

result_label = tk.Label(root, text="Weather results will appear here.", font=("Arial", 11), justify="left")
result_label.pack(pady=15)

root.bind("<Return>", lambda event: show_weather())

root.mainloop()