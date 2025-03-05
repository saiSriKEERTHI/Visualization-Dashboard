from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DataEntry
from .serializers import DataEntrySerializer

def home(request):
    return JsonResponse({"message": "Welcome to the API!"})  # ✅ Fix for home view

@api_view(['GET'])
def get_data(request):
    entries = DataEntry.objects.all()
    serializer = DataEntrySerializer(entries, many=True)
    return Response(serializer.data)

