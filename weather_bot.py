import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore


def get_weather(city):
    """Fetches weather data for a given city."""
    api_key = '5ca5746f2d4dbbb3c54c3f6bdfb9a3e6'  # My API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data['cod'] != '404':
        main = weather_data['main']
        temperature = round(main['temp'] - 273.15, 2)  # Convert from Kelvin to Celsius
        description = weather_data['weather'][0]['description']
        return f"{city}\n{description}\n{temperature}°C"
    else:
        return "City not found."

# Example Usage (Run this script directly to test)
if __name__ == '__main__':
    city_name = input("Enter a city: ")
    weather_data = get_weather(city_name)
    print(weather_data)
