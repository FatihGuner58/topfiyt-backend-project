from django.urls import path 
from .views import (
    LandingPageContentDetail, SliderItemList,
    WhatIsTopfiytItemList, TopfiytForWhoItemList, FooterView
)

urlpatterns = [
    path('landing/', LandingPageContentDetail.as_view(), name='landing-detail'),
    path('slider-items/', SliderItemList.as_view(), name='slider-items'),
    path('topfiytforwho/', TopfiytForWhoItemList.as_view(), name='topfiytforwho-list'),
    path('whatistopfiyt/', WhatIsTopfiytItemList.as_view(), name='whatistopfiyt-list'),
    path('footer/', FooterView.as_view(), name='footer-api'),
]