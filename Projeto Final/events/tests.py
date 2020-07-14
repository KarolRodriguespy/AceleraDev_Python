

# Create your tests here.

from django.test import TestCase

from .models import Event

class EventModelTestCase(TestCase):

    def test_return_string(self):
        event = Event.objects.create(
            level='information',
            log='Teste'

        )
        self.assertEqual(str(event), 'Teste')
