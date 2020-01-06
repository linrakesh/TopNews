from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    url = ('https://newsapi.org/v2/top-headlines?' 'country=us&' 'apiKey=2121032f088e4370affe13ca317f8d1a')
    response = requests.get(url)
    data = json.loads(response.text)
    for article in data['articles']:
        print(article['source']['name'])
        print(article['author'])
        print(article['title'])
        print(article['description'])
        print(article['url'])
        print(article['urlToImage'])
        print(article['publishedAt'])
        print(article['content'])
    
    return render(request,'newsapp/index.html',{'data':data})

