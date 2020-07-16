from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APITestCase


# Create your tests here.


class IntegrationTests(APITestCase):

    def test_create_event(self):
        self.client = APIClient()

        data = {'level': 'warning',
                'log': 'teste'}
        request = self.client.post('http://127.0.0.1:8000/events/', data=data, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_detail_event(self):
        self.client = APIClient()
        request = self.client.get('http://127.0.0.1:8000/events/', format='json')
        self.assertEquals(request.status_code, status.HTTP_200_OK)

    def test_deleted_event(self):
        self.client = APIClient()
        request = self.client.delete('http://127.0.0.1:8000/events/18/', format='json')
        self.assertEquals(request.status_code, status.HTTP_204_NO_CONTENT)
