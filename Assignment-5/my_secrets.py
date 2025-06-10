import os
from dotenv import load_dotenv

load_dotenv()

class Secrets:
    def __init__(self):
        self.api_key = os.getenv("LITELLM_API_KEY")
        self.model = os.getenv("LITELLM_MODEL")

    def get_api_key(self):
        return self.api_key

    def get_model(self):
        return self.model
