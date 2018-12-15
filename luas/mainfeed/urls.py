from django.urls import path, include, register_converter
from . import views


urlpatterns = [
    path('', views.ObjectFeeds.as_view(), name='home-feed'),
    path('scrape/', views.scrape, name='scrape'),
    path('<slug:slug>/', views.headline_detail, name="detail"),
]

 