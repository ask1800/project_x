from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from bs4 import BeautifulSoup
import requests
from .models import Headline


#test comment
def scrape(request):
        #kompas.com trending news web scrapper
        source = requests.get('https://www.kompas.com').text

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
                        new_headline.save()

        #detiknews.com rss trending
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
                        new_headline.source = "Detik"
                        new_headline.save()

        return redirect('/')
        
class ObjectFeeds(ListView):
	model = Headline
	context_object_name = 'headlines'
	template_name = 'mainfeed/home.html'
	

# class HeadlineDetailView(DetailView):
#         model = Headline
#         context_object_name = 'headline'
#         template_name = 'mainfeed/home_detail.html'
        
#         def get_context_data(self, slug, **kwargs):
#                 data = super(HeadlineDetailView, self).get_context_data(**kwargs)
#                 return data

def headline_detail(request, slug):
        headline = get_object_or_404(Headline, slug=slug)
        headline.hit += 1
        headline.save()
        return render(request, 'mainfeed/home_detail.html', context={'headline' : headline})