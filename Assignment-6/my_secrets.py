import os
from dotenv import load_dotenv

load_dotenv()

class Secrets:
    def __init__(self):
        self.api_key = os.getenv("OPEN_ROUTER_API_KEY")
        self.api_base_url = os.getenv("OPEN_ROUTER_BASE_URL")
        self.model = os.getenv("ROUTER_MODEL")
        self.weather_api_key = os.getenv("WEATHER_API_KEY")

    def get_api_key(self):
        return self.api_key

    def get_api_base_url(self):
        return self.api_base_url

    def get_api_model(self):
        return self.model

    def get_weather_api_key(self):
        return self.weather_api_key
