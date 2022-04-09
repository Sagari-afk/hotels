from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from hotel_app.models import Hotel
from hotel_app.serializers import HotelsSerializer


@api_view(["Get"])
def api_hotels(request):
    for i in Hotel.objects.all():
        serializer = HotelsSerializer(i)
        return Response(serializer.data)
