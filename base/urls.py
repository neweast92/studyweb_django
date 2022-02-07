from unicodedata import name
from django.urls import path

from base.views import home, room

urlpatterns = [
    path('', home, name="home"),
    path('room/<str:pk>', room, name="room"),
]