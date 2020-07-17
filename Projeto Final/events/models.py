from django.db import models


LEVEL_CHOICES = [
    ('critical', 'critical.'),
    ('debug', 'debug'),
    ('error', 'error'),
    ('warning', 'warning'),
    ('information', 'info'),
]

ENVIRONMENT_CHOICES = [
    ('produção', 'produção'),
    ('homologação', 'homologação'),
    ('dev', 'dev'),


]


class Event(models.Model):
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    environment = models.CharField(max_length=20, choices=ENVIRONMENT_CHOICES)
    address = models.GenericIPAddressField(protocol='both')
    log = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.log
