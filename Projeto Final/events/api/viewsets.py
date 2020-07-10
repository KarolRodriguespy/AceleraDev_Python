from rest_framework.viewsets import ModelViewSet
from events.models import User, Agent, Event
from .serializers import EventSerializer, UserSerializer, AgentSerializer


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AgentsViewSet(ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class EventsViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
