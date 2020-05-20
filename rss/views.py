from django.shortcuts import render
import feedparser
import html
from operator import itemgetter
from htmlmin.decorators import minified_response


@minified_response
def index(request):
    if request.GET.get("url"):
        url = request.GET["url"]
        feeds = feedparser.parse(url)
        request.session['url'] = url
    else:
        feeds = None
        url = ""
    return render(request, 'rss/reader.html', {'feed' : feeds,'reload' : url})


@minified_response
def zorad_vzostupne(request):
    url = request.session['url']
    feed = feedparser.parse(url)
    entries = feed['entries']
    usporiadane = sorted(entries, key=itemgetter('published_parsed'), reverse=True)
    feed['entries'] = usporiadane
    return render(request, 'rss/reader.html', { 'feed' : feed,'reload' : url, })


@minified_response
def zorad_zostupne(request):
    url = request.session['url']
    feed = feedparser.parse(url)
    entries = feed['entries']
    usporiadane = sorted(entries, key=itemgetter('published_parsed'))
    feed['entries'] = usporiadane
    return render(request, 'rss/reader.html', { 'feed' : feed, 'reload' : url, })





