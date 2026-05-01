import requests

WEATHER_CODE = {
    (0,): "Clear sky",
    (1,2,3): "Mainly clear",
    (45, 48): "Fog",
    (51, 53, 55): "Drizzle",
    (56, 57): "Freezing drizzle",
    (61, 63, 65): "Rain",
    (66, 67): "Freezing rain",
    (71, 73, 75): "Snow fall",
}

def describe_weather(weather_code):
    for codes, text in WEATHER_CODE.items():
        if weather_code in codes:
            return text
    return "Unknown conditions"

def get_location(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city,
        "count": 1
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Network error:", e)
        return None
        
    data = response.json()

    results = data.get("results")
    if not results:
        print("City not found")
        return None
        
    return results[0]

def get_weather(latitude, longitude):
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    try:
        weather_response = requests.get(weather_url, params=weather_params, timeout=10)
        weather_response.raise_for_status()
    except requests.RequestException as j:
        print("Network error", j)
        return None
        
    weather_data = weather_response.json()
    current = weather_data.get("current_weather")

    if not current:
        print("Data not found")
        return None
    
    return current

def main():
    while True:

        city = input("Enter a city: ").strip()

        if not city:
            print("City name cannot be empty")
            continue
        
        location = get_location(city)

        if location is None:
            continue
        
        name = location.get("name")
        country = location.get("country")
        latitude = location.get("latitude")
        longitude = location.get("longitude")

        current_weather = get_weather(latitude, longitude)

        if current_weather is None:
            continue

        temperature = current_weather.get("temperature")
        weather_code = current_weather.get("weathercode")
        description = describe_weather(weather_code)
        wind_speed = current_weather.get("windspeed")

        print("Current weather: ")
        print(f"Location: {name}, {country}")
        print(f"Temperature: {temperature}°C")
        print(f"Conditions: {description}")
        print(f"Wind speed: {wind_speed} km/h")

        again = input("\nSearch again? (y/n): ").strip().lower()

        if again != "y":
            print("Goodbye")
            break

if __name__ == "__main__":
    main()