from django.shortcuts import render

# Create your views here.

# importing api
from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.


def index(request):

    newsapi = NewsApiClient(api_key='e22533c663ea49449addbaeb281be918')
    top = newsapi.get_top_headlines(sources='techcrunch')

    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'news/index.html', context={"mylist": mylist})
