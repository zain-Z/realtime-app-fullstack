from django.urls import path

from . import consumers

websocket_urlpattern = [
    path('ws/notes', consumers.NoteConsumer)
]
