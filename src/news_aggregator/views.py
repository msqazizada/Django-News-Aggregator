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


# BBC
for headings in get_match(urls['bbc'], 'a', 'block-link__overlay-link'):
    if len(headings.text) > 5 and len(bbc) < 5:
        if urls['bbc'] in headings['href']:
            bbc.append({'content': headings.text,
                        'link': headings['href']})
        else:
            bbc.append({'content': headings.text,
                        'link': urls['bbc'] + headings['href']})


# CGTN
for headings in get_match(urls['cgtn'], 'div', 'cg-title'):
    link = headings.find('a')
    if len(headings.text) > 5 and len(cgtn) < 5:
        if urls['cgtn'] in link['href']:
            cgtn.append({'content': headings.text,
                         'link': link['href']})
        else:
            cgtn.append({'content': headings.text,
                         'link': urls['cgtn'] + link['href']})


# RT
for headings in get_match(urls['rt'], 'a', 'main-promobox__link'):
    if len(headings.text) > 5 and len(rt) < 5:
        if urls['rt'] in headings['href']:
            rt.append({'content': headings.text,
                       'link': headings['href']})
        else:
            rt.append({'content': headings.text,
                       'link': urls['rt'] + headings['href']})


# TRT
for headings in get_match(urls['trt'], 'div', 'news-article'):
    link = headings.find('a')
    if len(headings.text) > 5 and len(trt) < 5:
        if urls['trt'] in link['href']:
            trt.append({'content': headings.text,
                        'link': link['href']})
        else:
            trt.append({'content': headings.text,
                        'link': urls['trt'] + link['href']})


def home_view(request):
    context = {
        'rt_news': rt,
        'cgtn_news': cgtn,
        'bbc_news': bbc,
        'trt_news': trt,
        # 'china_news': china_news,
    }
    return render(request, 'news_aggregator/home.html', context)
