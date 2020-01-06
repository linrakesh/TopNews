from django.shortcuts import render
import requests
import json

# Create your views here.


def index(request):
    url = ('https://newsapi.org/v2/top-headlines?' 'country=in&' 'apiKey=2121032f088e4370affe13ca317f8d1a')
    response = requests.get(url)
    data = json.loads(response.text)
    name = []
    author = []
    title = []
    desc = []
    url = []
    img = []
    pubat = []
    content = []
    for article in data['articles']:
        name.append(article['source']['name'])
        author.append(article['author'])
        title.append(article['title'])
        desc.append(article['description'])
        url.append(article['url'])
        img.append(article['urlToImage'])
        pubat.append(article['publishedAt'])
        content.append(article['content'])
        # print(article['source']['name'])
        # print(article['author'])
        # print(article['title'])
        # print(article['description'])
        # print(article['url'])
        # print(article['urlToImage'])
        # print(article['publishedAt'])
        # print(article['content'])
        post = zip(name, author, title, desc, url, img, pubat, content)
    return render(request, 'newsapp/index.html', {'data': post})
