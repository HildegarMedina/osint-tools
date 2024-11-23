import tiktoken
from openai import OpenAI
from config.models_pricing import MODELS_PRICING
from dotenv import get_key

class ChatGPT:

    def __init__(self, model="gpt-4o-mini", max_tokens=3000):
        self.model = model
        self.max_tokens = max_tokens
        self.encoding = tiktoken.encoding_for_model(model)

    def calculate_cost(self, prompt):
        prompt_length = len(self.encoding.encode(prompt))
        response_length = self.max_tokens
        input_price = (prompt_length * MODELS_PRICING[self.model]['input']) / 1000
        output_price = (response_length * MODELS_PRICING[self.model]['output']) / 1000
        return input_price + output_price

    def completion(self, messages):
        try:
            openai = OpenAI(api_key=get_key('.env', 'OPENAI_API_KEY'))
            response = openai.chat.completions.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=0.7,
                messages=messages
            )
            message =  response.choices[0].message.content
            return message
        except Exception as e:
            print(e)
