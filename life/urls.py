from django.urls import path
from .views import Hero, Story, Iron, Thor, USA

urlpatterns = [
    path('', Hero.as_view(), name='hero'),
    path('story/', Story.as_view(), name='story'),
    path('story/iron/', Iron.as_view(), name='iron'),
    path('story/thor/', Thor.as_view(), name='thor'),
    path('story/usa/', USA.as_view(), name='usa'),
    
]