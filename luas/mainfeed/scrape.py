from bs4 import BeautifulSoup
from django.shortcuts import redirect
from .models import Headline
import requests

def scrape():
    #news.kompas.com popular scrapper
    source = requests.get('https://news.kompas.com').text

    soup = BeautifulSoup(source, 'lxml')

    trending = soup.find('div', class_='most__wrap clearfix')
    article = trending.find_all('div', class_='most__list clearfix')

    for i in range(len(article)):
            temp = article[i].a.text
            title = temp.split('\n')

            if Headline.objects.filter(title=title[1]).exists():
                    break
            else:
                    #save it to database
                    new_headline = Headline()
                    new_headline.title = title[1]
                    new_headline.read = title[2]
                    new_headline.url = article[i].a['href']
                    new_headline.source = "Kompas"
                    new_headline.genre = "News"
                    new_headline.save()

    #DetikNews rss
    source = requests.get('http://rss.detik.com/index.php/detikcom_nasional').text

    soup = BeautifulSoup(source, 'xml')

    article = soup.find_all('item')

    for i in range(len(article)):
            title = article[i].title.text
            link = article[i].link.text
            
            if Headline.objects.filter(title=title).exists():
                    break
            else:
                    new_headline = Headline()
                    new_headline.title = title
                    new_headline.url = link
                    new_headline.source = "DetikNews"
                    new_headline.genre = "News"
                    new_headline.save()

    #DetikFinance rss, url not fixed yet
    source = requests.get('http://rss.detik.com/index.php/finance').text

    soup = BeautifulSoup(source, 'xml')

    article = soup.find_all('item')

    for i in range(len(article)):
            title = article[i].title.text
            link = article[i].link.text
            
            if Headline.objects.filter(title=title).exists():
                    break
            else:
                    new_headline = Headline()
                    new_headline.title = title
                    new_headline.url = link
                    new_headline.source = "DetikFinance"
                    new_headline.genre = "Finance"
                    new_headline.save()

    #liputan6 News popular scraper
    source = requests.get('https://www.liputan6.com/news/indeks/terpopuler').text

    soup = BeautifulSoup(source, 'lxml')

    trending = soup.find('div', class_='articles--list articles--list_rows')
    article = trending.find_all('article', class_='articles--rows--item')

    for i in range(10):
            temp = article[i].a

            if Headline.objects.filter(title=temp['title']).exists():
                    break
            else:
                    #save it to database
                    new_headline = Headline()
                    new_headline.title = temp['title']
                    new_headline.url = temp['href']
                    new_headline.source = "Liputan6"
                    new_headline.genre = "News"
                    new_headline.save()

    # #tempo News popular scraper
    # source = requests.get('https://nasional.tempo.co').text

    # soup = BeautifulSoup(source, 'lxml')

    # trending = soup.find('div', class_='tab-content-slide selected')
    # article = trending.find_all('div', class_='wrapper clearfix')

    # for i in range(len(article)):
    #         temp = article[i]

    #         if Headline.objects.filter(title=title[1]).exists():
    #                 break
    #         else:
    #                 #save it to database
    #                 new_headline = Headline()
    #                 new_headline.title = temp.h2.text
    #                 new_headline.url = temp.a['href']
    #                 new_headline.source = "Tempo"
    #                 new_headline.genre = "News"
    #                 new_headline.save()
