import requests
from my_secrets import Secrets

class WeatherTool:
    name = "get_weather"
    description = "Get current weather for a given city."

    def run(self, city: str) -> str:
        key = Secrets().get_weather_api_key()
        url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}"
        try:
            response = requests.get(url)
            data = response.json()
            condition = data['current']['condition']['text']
            temp = data['current']['temp_c']
            return f"The weather in {city} is {condition} and {temp}°C."
        except Exception as e:
            return f"Failed to get weather: {str(e)}"
