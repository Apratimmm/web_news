from django.shortcuts import render
from .newsapi import get_news

def actualhome(request):
    return render(request,'news/actualhomepage.html')

def home(request):
    category = request.GET.get('category', 'general')
    articles = get_news(category)
    return render(request, 'news/newspage.html', {'articles': articles})

