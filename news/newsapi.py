
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_news(category):
    API_KEY = os.getenv('NEWSAPI_KEY')
    url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data['articles']
