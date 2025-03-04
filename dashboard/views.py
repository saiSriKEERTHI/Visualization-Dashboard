from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DataEntry
from .serializers import DataEntrySerializer

@api_view(['GET'])
def get_data(request):
    entries = DataEntry.objects.all()
    serializer = DataEntrySerializer(entries, many=True)
    return Response(serializer.data)
