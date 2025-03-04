from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from dashboard.consumers import DataConsumer  # Import your WebSocket Consumer
from django.core.asgi import get_asgi_application  # Import ASGI app

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r"ws/data/", DataConsumer.as_asgi()),  # WebSocket URL
        ])
    ),
})

