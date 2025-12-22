
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_news_category(category):
    API_KEY = os.getenv('NEWSAPI_KEY')
    url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data['articles']

def search_news(query, from_date=None, to_date=None):
    API_KEY = os.getenv('NEWSAPI_KEY')
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}'
    if from_date:
        url += f'&from={from_date}'
    if to_date:
        url += f'&to={to_date}'
    response = requests.get(url)
    data = response.json()
    return data.get('articles', [])
