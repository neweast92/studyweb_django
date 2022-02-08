from unicodedata import name
from django.urls import path

from base.views import createRoom, deleteRoom, home, room, updateRoom

urlpatterns = [
    path('', home, name="home"),
    path('room/<str:pk>', room, name="room"),
    path('create-room/', createRoom, name='create-room'),
    path('update-room/<str:pk>', updateRoom, name='update-room'),
    path('delete-room/<str:pk>', deleteRoom, name='delete-room')
]