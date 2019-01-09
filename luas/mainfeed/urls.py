from django.urls import path, include, register_converter
from . import views


urlpatterns = [
    path('', views.AllFeedPopular.as_view(), name='all-feed-popular'),
    path('latest/', views.AllFeedLatest.as_view(), name='all-feed-latest'),
    path('news', views.NewsFeedPopular.as_view(), name='news-feed-popular'),
    path('news/latest', views.NewsFeedLatest.as_view(), name='news-feed-latest'),
    path('finance', views.FinanceFeedPopular.as_view(), name='finance-feed-popular'),
    path('finance/latest', views.FinanceFeedLatest.as_view(), name='finance-feed-latest'),
    path('scrape/', views.startup, name='scrape'),
    path('<slug:slug>/', views.headline_detail, name="detail"),
]

 