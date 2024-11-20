from dotenv import set_key
import os

class Settings:
    
    def __init__(self) -> None:
        self.visibles = ['ipinfo_token']

    def get_all(self):
        return { k.lower(): v for k, v in os.environ.items() if k.lower() in self.visibles }

    def update(self, settings):
        for key, value in settings.items():
            set_key('.env', key.upper(), value)
        return True
