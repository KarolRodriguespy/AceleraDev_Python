from django.contrib.auth.models import User
from django.db import models


LEVEL_CHOICES = [
    ('critical', 'critical.'),
    ('debug', 'debug'),
    ('error', 'error'),
    ('warning', 'warning'),
    ('information', 'info'),
]


class Event(models.Model):
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    log = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.log
