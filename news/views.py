from django.shortcuts import render
from .newsapi import get_news_category, search_news

def initalhome(request):
    return render(request,'news/actualhomepage.html')

def home(request):
    category = request.GET.get('category', 'general')
    articles = get_news_category(category)
    return render(request, 'news/newspage.html', {'articles': articles})

def search(request):
    query = request.GET.get('q', '')
    from_date = request.GET.get('from', '')
    to_date = request.GET.get('to', '')
    
    if query:
        articles = search_news(query, from_date, to_date)
    else:
        articles = []

    context = {
        'articles': articles, 
        'query': query,
        'from_date': from_date,
        'to_date': to_date
    }
    return render(request, 'news/search_results.html', context)

