from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse


class ReverserTestCase(APITestCase):
    def setUp(self):
        super().setUp()

    def test_reverser(self):
        response = self.client.post(reverse('reverser'), data={'ident': 'tests:root'})
        self.assertEqual(response.data, reverse('tests:root'))

    def test_invalid(self):
        response = self.client.post(reverse('reverser'), data={'ident': 'tests:not_a_thing'})
        self.assertEqual(response.status_code, 404)
