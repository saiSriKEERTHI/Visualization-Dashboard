import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Data  # Import your Django model

class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()  # Accept the WebSocket connection
        await self.send_data()  # Send initial data

    async def disconnect(self, close_code):
        print("WebSocket Disconnected:", close_code)

    async def receive(self, text_data):
        data = json.loads(text_data)
        print("Received from WebSocket:", data)

    async def send_data(self):
        # Fetch data from the database
        records = list(Data.objects.values("id", "topic", "sector", "country", "relevance", "likelihood"))
        
        # Send JSON data to WebSocket
        await self.send(text_data=json.dumps(records))
