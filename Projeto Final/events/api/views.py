# Create your views here.
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.decorators import api_view

from events.models import Event

from events.api.serializers import EventModelSerializer


@api_view(['POST'])
def create_event(request):
    event= Event()
    serializer = EventModelSerializer(event, data=request.data)
    data = {}

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()

    return Response('log deletado', status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    serializer = EventModelSerializer(event, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def detail_event(request, event_id):
    event = Event.objects.filter(pk=event_id)
    serializer = EventModelSerializer(event, many=True)
    return Response(serializer.data)



class EventApiListView(ListAPIView):
    serializer_class = EventModelSerializer
    permission_classes = [IsAuthenticated]

    queryset = Event.objects.all()
