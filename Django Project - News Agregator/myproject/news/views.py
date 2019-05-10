from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request, source = "new-scientist"):


  url = 'https://newsapi.org/v1/articles?source={}'.format(source)
  url += '&sortBy=top&apiKey=d754b116d9fe46c2ad4d4e33b23e0f52'

  page = urllib.request.urlopen(url)
  string = page.read().decode()
  data = json.loads(string)
  sources = ['ars-technica', 'bbc-news', 'hacker-news', 'national-geographic', 'new-scientist', 'techradar']
  current_site = source
  context = {'newsapi': data, 'sources_key' : sources, 'selected_site': current_site}
  return render(request, 'news/index.html', context)