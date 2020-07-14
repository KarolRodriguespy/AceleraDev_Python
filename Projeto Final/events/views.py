from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from events.models import Event

from events.serializers import EventModelSerializer


class EventApiViewSet(viewsets.ModelViewSet):
    serializer_class = EventModelSerializer
    permission_classes = [IsAuthenticated]

    queryset = Event.objects.all()


