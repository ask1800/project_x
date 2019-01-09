from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
import schedule
import time
from .models import Headline
from .scrape import scrape
from django.http import Http404
from django.contrib.auth.models import User


#test comment
def startup(request):
        if not request.user.is_staff:
                raise Http404
        else:
                scrape()
                schedule.every(1).minutes.do(scrape)
    
                while 1:
                        schedule.run_pending()
                        time.sleep(1)

        
class AllFeedPopular(ListView):
        model = Headline
        context_object_name = 'headlines'
        template_name = 'mainfeed/home.html'
        ordering = ['-hit']

class AllFeedLatest(ListView):
        model = Headline
        context_object_name = 'headlines'
        template_name = 'mainfeed/home.html'
        ordering = ['-created_at']

#Object filtering not yet fixed (currently in templates)
class NewsFeedPopular(ListView):
        model = Headline
        context_object_name = 'headlines'
        template_name = 'mainfeed/news.html'
        ordering = ['-hit']

class NewsFeedLatest(ListView):
        model = Headline
        context_object_name = 'headlines'
        template_name = 'mainfeed/home.html'
        ordering = ['-created_at']

class FinanceFeedPopular(ListView):
        model = Headline
        context_object_name = 'headlines'
        template_name = 'mainfeed/finance.html'
        ordering = ['-hit']

class FinanceFeedLatest(ListView):
        model = Headline
        context_object_name = 'headlines'
        template_name = 'mainfeed/finance.html'
        ordering = ['-created_at']

def headline_detail(request, slug):
        headline = get_object_or_404(Headline, slug=slug)
        headline.hit += 1
        headline.save()
        return render(request, 'mainfeed/home_detail.html', context={'headline' : headline})