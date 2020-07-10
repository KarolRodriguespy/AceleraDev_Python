from rest_framework.serializers import ModelSerializer
from events.models import Event, Agent, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']


class AgentSerializer(ModelSerializer):
    class Meta:
        model = Agent
        fields = ['name', 'user', 'address', 'status', 'env', 'version']


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['level', 'data', 'agent', 'arquivado', 'date']


