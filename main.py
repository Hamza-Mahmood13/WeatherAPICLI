import requests


def main():
    while True:

        city = input("Enter a city: ").strip()

        if not city:
            print("City nane cannot be empty")
            continue
        
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
            continue
        
        data = response.json()

        results = data.get("results")
        if not results:
            print("City not found")
            continue
        
        location = results[0]
        name = location.get("name")
        country = location.get("country")
        latitude = location.get("latitude")
        longitude = location.get("longitude")

        
        print("Location found: ")
        print("City:", name)
        print("Country", country)
        print("Latitude", latitude)
        print("Longitude", longitude)

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
            continue
        
        weather_data = weather_response.json()
        current = weather_data.get("current_weather")

        if not current:
            print("Data not found")
            continue
        
        temperature = current.get("temperature")
        weather_code = current.get("weathercode")

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
        description = "Unknown conditions"

        for codes, text in WEATHER_CODE.items():
            if weather_code in codes:
                description = text
                break
        #description = WEATHER_CODE.get(weather_code, "Unknown conditions")

        print("current weather")
        print(f"location: {name}, {country}")
        print(f"Temperature: {temperature}")
        print(f"Conditions: {description}")

        again = input("\nSearch again? (y/n): ").strip().lower()

        if again != "y":
            print("Goodbye")
            break

if __name__ == "__main__":
    main()