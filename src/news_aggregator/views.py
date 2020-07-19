from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

# Create your views here.
urls = {
    'bbc': 'https://www.bbc.com/',
    'cgtn': 'https://www.cgtn.com/',
    'rt': 'https://www.rt.com/',
    'trt': 'https://www.trtworld.com/',
}
bbc = []
cgtn = []
rt = []
trt = []


def get_match(url, tag, klass):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    headings_classes = soup.find_all(tag, class_=klass)
    return headings_classes


def get_article_headings(url, tag, klass, lst, link=False):
    for headings in get_match(url, tag, klass):
        if link is True:
            _link = headings.find('a')
            if len(headings.text) > 5 and len(lst) < 5:
                if url in _link['href']:
                    lst.append({'content': headings.text, 'link': _link['href']})
                else:
                    lst.append({'content': headings.text, 'link': url + _link['href']})
        else:
            if len(headings.text) > 5 and len(lst) < 5:
                if url in headings['href']:
                    lst.append({'content': headings.text, 'link': headings['href']})
                else:
                    lst.append({'content': headings.text, 'link': url + headings['href']})


def home_view(request):
    # TRT
    get_article_headings(urls['trt'], 'div', 'news-article', trt, True)
    # RT
    get_article_headings(urls['rt'], 'a', 'main-promobox__link', rt)
    # CGTN
    get_article_headings(urls['cgtn'], 'div', 'cg-title', cgtn, True)
    # BBC
    get_article_headings(urls['bbc'], 'a', 'block-link__overlay-link', bbc)

    context = {
        'rt_news': rt,
        'cgtn_news': cgtn,
        'bbc_news': bbc,
        'trt_news': trt,
        # 'china_news': china_news,
    }
    return render(request, 'news_aggregator/home.html', context)
