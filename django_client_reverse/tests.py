from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse


class ReverserTestCase(APITestCase):
    def setUp(self):
        super().setUp()

    def test_thing(self):
        response = self.client.post(reverse('reverser'), data={'ident': 'tests:root'})
        self.assertEqual(response.data, '/tests/')
