from dotenv import set_key, get_key, load_dotenv

class Settings:
    
    def __init__(self) -> None:
        self.visibles = ['ipinfo_token', 'openai_api_key']

    def get_all(self):
        return { key: get_key('.env', key.upper()) for key in self.visibles}

    def update(self, settings):
        for key, value in settings.items():
            set_key('.env', key.upper(), value)
            load_dotenv()
        return True
