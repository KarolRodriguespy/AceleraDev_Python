from django.core.validators import MinLengthValidator, EmailValidator, validate_ipv4_address
from django.db import models

LEVEL_CHOICES = [
    ('critical', 'critical.'),
    ('debug', 'debug'),
    ('error', 'error'),
    ('warning', 'warning'),
    ('information', 'info'),
]


class User(models.Model):
    objects = []
    name = models.CharField(max_length=50)
    email = models.EmailField(validators=[EmailValidator], null=True)
    password = models.CharField(max_length=50, validators=[MinLengthValidator])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Agent(models.Model):
    objects = []
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    address = models.GenericIPAddressField(validators=[validate_ipv4_address], null=True)
    status = models.BooleanField(default=False)
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Event(models.Model):
    objects = []
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    data = models.TextField(max_length=500)
    agent = models.OneToOneField(Agent, on_delete=models.PROTECT)
    arquivado = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.level +' in ' + self.agent.name

    class Meta:
        ordering = ['date']


