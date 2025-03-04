from django.urls import re_path
from dashboard.consumers import DataConsumer  # Import the WebSocket Consumer

websocket_urlpatterns = [
    re_path(r'ws/data/', DataConsumer.as_asgi()),  # WebSocket URL
]

