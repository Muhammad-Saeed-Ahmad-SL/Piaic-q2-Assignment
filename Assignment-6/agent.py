import requests
from my_secrets import Secrets
from tools.weather_tool import WeatherTool
from tools.calculator_tool import CalculatorTool

secrets = Secrets()
tools = {
    "get_weather": WeatherTool(),
    "calculator": CalculatorTool()
}

def call_openrouter_api(prompt, history):
    headers = {
        "Authorization": f"Bearer {secrets.get_api_key()}",
        "Content-Type": "application/json"
    }

    messages = history + [{"role": "user", "content": prompt}]
    payload = {
        "model": secrets.get_api_model(),
        "messages": messages,
        "stream": False
    }

    response = requests.post(
        f"{secrets.get_api_base_url()}/chat/completions",
        headers=headers,
        json=payload
    )
    data = response.json()
    return data["choices"][0]["message"]["content"]
