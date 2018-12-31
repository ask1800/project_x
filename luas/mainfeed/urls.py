from django.urls import path, include, register_converter
from . import views


urlpatterns = [
    path('', views.HomeFeed.as_view(), name='home-feed'),
    path('scrape/', views.scrape, name='scrape'),
    path('<slug:slug>/', views.headline_detail, name="detail"),
    path('news', views.NewsFeed.as_view(), name='news-feed'),
    path('finance', views.FinanceFeed.as_view(), name='finance-feed'),
]

 