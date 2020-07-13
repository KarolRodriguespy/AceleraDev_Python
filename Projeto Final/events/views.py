from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from events.models import Event

from events.serializers import EventModelSerializer


class EventApiViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]

    queryset = Event.objects.all()
    serializer_class = EventModelSerializer
